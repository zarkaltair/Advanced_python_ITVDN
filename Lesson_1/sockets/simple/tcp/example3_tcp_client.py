# example 3 (TCP client socket)
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8888))
sock.send(b'Test message')
sock.close()
