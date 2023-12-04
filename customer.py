# this is customer side code



import socket

# ipv4, tcp socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to the server
sock.connect((server_ip, port))
# send the data (I left it empty but you should add in strings to send here.)
sock.send()
