from server import Server
import sys, threading, time

def test_server():

    host, port = "127.0.0.1", 8080

    def suma(a,b):
        return a+b

    def resta(a,b):
        return a-b
    
    server = Server(host, port)
    server.add_method(suma)
    server.add_method(resta)
    server_thread = threading.Thread(target=server.serve)
    server_thread.daemon = True
    server_thread.start()

    print(f"Servidor ejecutando: {host} : {port}")

    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        server.shutdown()
        print('Terminado')
        sys.exit()

if __name__ == "__main__":
    test_server()
