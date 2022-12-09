from socket import *

server_name = '127.0.0.2'
server_port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence: ')
client_socket.sendto(bytes(message, encoding='utf-8'), (server_name, server_port))

modified_message, server_address = client_socket.recvfrom(2048)
print('From server:', modified_message.decode('utf-8'))

client_socket.close()