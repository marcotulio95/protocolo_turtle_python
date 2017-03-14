import base64
import socket
import json
from io import StringIO

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
request = {"funcao": "forward", "valor": 100}
enviar(socketCliente, request)

while True:
	dado, endereco = socketCliente.recvfrom(1024)
	if not dado: break
	print("Resposta do servidor: ", dado.decode())

socketCliente.close()