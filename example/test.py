from simpleWSpy.server import WebSocketServer

def mySuperFunction(msg):
  print 'Msg printed from my super function'
  print msg

if __name__ == '__main__':
  ws = WebSocketServer.WebSocket(('localhost', 9000))
  ws.serve_forever(mySuperFunction)
