import socket


class WebSocket:

  # initiatin the connection ...
  def __init__(self, aConnection):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.bind(aConnection)
    self.sock.listen(1)
    self.conn = None
    self.addr = None
    self.stream = ''
    self.header = '\
HTTP/1.1 101 Web Socket Protocol Handshake\r\n\
Upgrade: WebSocket\r\n\
Connection: Upgrade\r\n\
Origin: null\r\n\
Location: ws://%s:%d/\r\n\
' % aConnection


  # Sending messages :
  def sendMSG(self, aMsg):
    self.conn.send(aMsg)

  # Receiving message , the default size is 1024
  def recvMSG(self, aSize = 1024):
    self.stream = self.conn.recv(aSize)
    return self.stream

  # Execute the handshake protocole.
  def genAcceptKey(self, aClientWSHeader):
    headerInfos = aClientWSHeader.split('\r\n')
    body = aClientWSHeader.split('\r\n\r\n')[1]
    key = ''
    cc = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    # Extracting the request handshake key from the header
    for hi in headerInfos:
      if hi.startswith('Sec-WebSocket-Key:'):
        key = hi[19:]
      else:
        continue

    # Generating the handshake key to tell client that we accept it's request
    import hashlib
    import base64
    sha = hashlib.sha1()
    sha.update(key+cc)
    hashed = sha.digest()
    return base64.b64encode(hashed)

  # Executing the handshake protocol.
  def handShake(self, clientWSHeader):
#clientWSHeader = self.recvMSG(4094)
    serverWSHeader = self.header
    serverWSHeader += 'Sec-WebSocket-Accept:'+ str(self.genAcceptKey(clientWSHeader)) + '\r\n\r\n'          
    self.sendMSG(serverWSHeader)  
  
  # Decode the stream:
  def decodeStream(self): 
    encodedStream = self.stream
    # convert the string into numeric values
    byteStream = [ord(char) for char in encodedStream]
    # decode the data length:
    dLength = byteStream[1] & 127
    iFirstMask = 2 #default index fist mask
    if dLength == 126: # 2 bytes are used for length
      iFirstMask = 4
    elif dLength == 127: # 8 bytes are used for length
      iFirstMask = 10

    masks = [m for m in byteStream[iFirstMask: iFirstMask+4]]
    iFirstDataByte = iFirstMask + 4
    decodedStream = []
    i = iFirstDataByte
    j = 0

    while i < len(byteStream):
      decodedStream.append(chr(byteStream[i] ^ masks[j % 4]))
      i += 1
      j += 1

    return ''.join(decodedStream)
                   

# Serve forever ...
  def serve_forever(self,  aCustomClass, aSize = 1024):
    while True:
      self.conn, self.addr = self.sock.accept()
      msg = self.recvMSG(4096)
      if(msg):
        self.handShake(msg)
        print 'Accepted !'
        while True:
          msg = self.recvMSG(aSize)
          if(msg):
            msgToSend, wantToSend = aCustomClass.onRecieve(self.decodeStream())
            if(wantToSend):
              continue #Send is not supported yet
  


    
