import base64
import socket
import json
from io import StringIO

'''
Este cliente desenha uma estrela na cor vermelha.
'''
def enviar(socket, request, SERVIDOR="localhost", PORTA= 8880):
	requestJson = json.dumps(request)
	socket.sendto( requestJson.encode() , (SERVIDOR, PORTA))


print('Iniciando cliente')


##----------------Instaciando nosso Socket----------------------------

socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketCliente.settimeout(3)

##-----------Definindo uma funcao --------------------------


request = {"funcao": "color", "valor": "red"}
enviar(socketCliente, request)


for x in range(360):
	request = {"funcao": "forward", "valor": 200}
	enviar(socketCliente, request)
	
	request = {"funcao": "left", "valor": 170}
	enviar(socketCliente, request)


while True:
	dado, endereco = socketCliente.recvfrom(1024)
	if not dado: break
	print("Resposta do servidor: ", dado.decode())

socketCliente.close()