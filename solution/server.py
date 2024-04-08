
from _socket import _RetAddress
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from urllib.parse import urlparse

#base de datos
productos = {}

class Producto:
    self.producto_type = producto_type
    self.client = client
    self.status = status
    self.payment = payment

class Fisico(self, client, status, payment, shipping, products):
    self.client = client
    self.status = status
    self.payment = payment
    self.shipping = shipping
    self.products = products 
    
class Digital(self, client, status, payment, code, expiration):
    self.client = client
    self.status = status
    self.payment = payment
    self.code = code 
    self.expiration = expiration

class FactoryProducto(self, producto_type):
    if producto_type == "fisico":
        return Fisico(self, client, status, payment, shipping, products)
    elif producto_type == "digital":
        return Digital(self, client, status, payment, code, expiration)
    else:
        raise f"Producto no encontrado"

class ProductoRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, client, status, payment):
        super().__init__(self, client, status, payment)

    def do_POST(self):
        if self.path.starswitch == "/productos"
    
    def do_GET(self):
        if self.path == "/productos"
    
    def do_PUT(self):
        if self.path.starwitch == "/productos/"

    def do_DELETE(self):
        if self.path.starwitch == "/productos/"


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    try:
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()   
    except KeyboardInterrupt:
        print(f"Apagando el servidor...")
        httpd.socket.close()

if __main__ == __name__:
    run()