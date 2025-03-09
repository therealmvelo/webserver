import socket

HOST = "127.0.0.1"
PORT = 8080

RESPONSE = b"""\
HTTP/1.1 200 OK\r\n\
Content-Type: text/html\r\n\
Content-Length: 22\r\n\
Connection: close\r\n\
\r\n\
<h1>HELLO WORLD</h1>"""
    
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_sock:
    server_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST,PORT))
    server_sock.listen(5)

    print(f"listening on {HOST}:{PORT}")

    while True:
        client_sock,client_addr = server_sock.accept()
        print(f"new connection from {client_addr}")
        with client_sock:
            client_sock.sendall(RESPONSE)
            client_sock.shutdown(socket.SHUT_WR)