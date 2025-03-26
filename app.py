from http.server import BaseHTTPRequestHandler, HTTPServer
import os


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        """Обработка  GET запросов"""
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        with open("index.html", "r", encoding="utf-8") as file:
            page = file.read()
        self.wfile.write(bytes(page, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started at http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")