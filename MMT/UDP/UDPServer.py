from socket import *

server_name = '127.0.0.2'
server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((server_name, server_port))

print('The server is ready to receive')
while True:
    message, client_address = server_socket.recvfrom(2048)
    
    if not message:
        break
    
    modified_message = message.upper()
    server_socket.sendto(modified_message, client_address)