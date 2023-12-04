# this is customer side code



import socket

# The ip of the server we want to send what we want to order to
server_ip=('127.0.0.1')
# The port we using
port=('37373')

# ipv4, tcp socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to the server
sock.connect((server_ip, port))
# send the data (I left it empty but you should add in strings to send here.)
sock.send()
