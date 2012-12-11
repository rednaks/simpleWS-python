from simpleWSpy.server import WebSocketServer

class myClass:
  def __init__(self):
    self.msg = ''

  def _onRecieve(self, msg):
    print 'Msg printed from my Custom Class '
    print msg
    #return "Response", 1  # if I want to send something to the server
    return None, 0

  
if __name__ == '__main__':
  myInstance = myClass()
  ws = WebSocketServer.WebSocket(('localhost', 9000))
  ws.serve_forever(myInstance)
