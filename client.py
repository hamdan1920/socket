import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)
try:
    message = "ini klien"
    client_socket.sendall (message.encode())
    data = client_socket.recv(1024)
    print("Menerima dari server:", data.decode())
finally:
    client_socket.close()
