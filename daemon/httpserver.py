from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
HOST_NAME = ''
PORT = 4567

class Handler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def _set_failure(self):
        self.send_response(500)
    def do_GET(self):
        self._set_response()
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print("------------------body--------------\n",body)
        req,res = self.parse_json(body)
        if not res:
            self._set_failure()
            return None
        print("parse : ",req.get('test'),req.get('fake'))
        self._set_response()
    def parse_json(self,byte_msg):
        try:
            data = json.loads(byte_msg.decode('utf-8'))
        except ValueError as e:
            return None,False
        return data,True

if __name__ == '__main__':
    server = HTTPServer((HOST_NAME,PORT), Handler)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()