# This is the server side code.



import socket

# defining host ip
host = ('127.0.0.1')
# port to bind to (work on)
port = ('37373')
# maximum connections
max_conn=int(1)

# ipv4, tcp socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binding (connecting) on a ip, and port
sock.bind((host, port))
# listenning for connection requests. Limited to 2 connect at a time.
sock.listen(max_conn)
