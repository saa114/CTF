import SocketServer, subprocess


HOST = '0.0.0.0'
PORT = 4000


class handler(SocketServer.BaseRequestHandler):
   
    def handle(self):
        filename = open("/home/catchthemall/textfile.txt", "rb")
        text = filename.read()
        filename.close()
        self.request.send(text)
        subprocess.Popen(["python", "/home/catchthemall/handler.py"])

if __name__ == "__main__":
    server = SocketServer.TCPServer((HOST,PORT), handler)
    server.allow_reuse_address = True
    server.serve_forever()

