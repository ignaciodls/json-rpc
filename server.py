import socket

class Server:
    def __init__(self, host="127.0.0.1", port=8080):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.methods = {}

    def serve(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Servidor escuchando en {self.host}:{self.port}")

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Conexión aceptada de {addr}")
            client_socket.close()

    def add_method(self, method, name = None):
        self.methods[name if name else method.__name__] = method
        print(f'Mtodo {name if name else method.__name__} agregado.')

    def shutdown(self):
        self.server_socket.close()
        print("Servidor detenido.")

