from http.server import SimpleHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080

class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Если запрашивается корневой URL, отдаем index.html
        if self.path == "/":
            self.path = "/index.html"
        return super().do_GET()

    def end_headers(self):
        # Устанавливаем правильные MIME-типы для CSS, JS и других файлов
        if self.path.endswith(".css"):
            self.send_header("Content-Type", "text/css")
        elif self.path.endswith(".js"):
            self.send_header("Content-Type", "application/javascript")
        elif self.path.endswith(".html"):
            self.send_header("Content-Type", "text/html")
        elif self.path.endswith(".json"):
            self.send_header("Content-Type", "application/json")
        elif self.path.endswith(".svg"):
            self.send_header("Content-Type", "image/svg+xml")
        elif self.path.endswith(".png"):
            self.send_header("Content-Type", "image/png")
        elif self.path.endswith(".jpg") or self.path.endswith(".jpeg"):
            self.send_header("Content-Type", "image/jpeg")
        elif self.path.endswith(".gif"):
            self.send_header("Content-Type", "image/gif")
        super().end_headers()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started at http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
