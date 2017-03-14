'''
Formas Geometricas é um cliente para que faz requisições ao nosso serve Turtle.
Ele faz requicoes de maneira a forma 3 formas Geometricas diferentes de acordo com a funcao desejada.
'''

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
def DesenharQuadrado(): ## Desenha um quadrado
	for x in range(4):
		request = {"funcao": "forward", "valor": [100]}
		enviar(socketCliente, request)
		request = {"funcao": "left", "valor": [90]}
		enviar(socketCliente, request)

def DesenharTriangulo(): ## Desenha um triangulo
	for x in range(4):
		request = {"funcao": "forward", "valor": [100]}
		enviar(socketCliente, request)
		request = {"funcao": "left", "valor": [120]}
		enviar(socketCliente, request)

def DesenharCirculo(): ## Desenha circulo atraves da instrução circle
	request = {"funcao": "circle", "valor": [100]}
	enviar(socketCliente, request)

##---------Aqui deve ser chamado a funcao desejada -----------
DesenharCirculo()

while True:
	dado, endereco = socketCliente.recvfrom(1024)
	if not dado: break
	print("Resposta do servidor: ", dado.decode())

socketCliente.close()