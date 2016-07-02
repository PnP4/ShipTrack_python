import socket
import threading

connections={}

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                print connections
                if data :
                    fromid=data.split("&")[0]  #from&to^data
                    toid=data.split("&")[1].split("^")[0]

                    if (not connections.has_key(fromid)):
                        connections[fromid]=client

                    if(connections.has_key(toid)):
                        response = data
                        connections[toid].send(response)
                    else:
                        print "recever not present"

                else:
                    raise socket.error('Client disconnected')
            except Exception, e:
                print e
                client.close()
                return False

if __name__ == "__main__":
    port_num = 4000
    ThreadedServer('',port_num).listen()