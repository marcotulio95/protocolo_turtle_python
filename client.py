import base64
import socket

SERVIDOR = 'localhost'
PORTA = 8888

dado = b'GET'


print('Iniciando cliente')

socketCliente = 	socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketCliente.connect((SERVIDOR, PORTA))

socketCliente.sendall(dado) 

while True:
	dado = socketCliente.recv(1024)
	if not dado: break
	print("Resposta do servidor: ", dado)