import socket

sock_server = socket.socket()
addr = ('127.0.0.1',18888)
sock_server.bind(addr)
sock_server.listen(100)
while True:
    client_socker , client_addr = sock_server.accept()
    request = client_socker.recv(1024)
    print(request.decode('utf-8'))
