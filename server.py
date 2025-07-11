from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if self.path == "/":
            self.wfile.write(b"<html><body><h1>Hola, mundo!</h1><p>Ruta: /</p></body></html>")
        elif self.path == "/test":
            self.wfile.write(b"<html><body><h1>Ruta de prueba</h1><p>Ruta: /test</p></body></html>")
        else:
            self.wfile.write(b"<html><body><h1>Ruta no encontrada</h1></body></html>")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else b''
        self._set_headers()
        response = f"<html><body><h1>Datos POST recibidos</h1><pre>{post_data.decode('utf-8')}</pre></body></html>"
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor HTTP corriendo en http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Servidor detenido.")

if __name__ == '__main__':
    run()
