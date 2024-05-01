import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address ('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(5)

print("Server ", server_address)

while True:
    client_socket, client_address = server_socket.accept()
    try:
        print("Terhubung > ", client_address)
        data = client_socket.recv(1824)
        print("Menerima:", data.decode())
        client_socket.sendall(b"Terima kasihl")
    finally:
        client_socket.close()
