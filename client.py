import base64
import socket
import json
from io import StringIO

def enviar(socket, request):
	requestJson = json.dumps(request)
	socket.sendall(requestJson.encode())


print('Iniciando cliente')

##----------Dados da Conexao----------------------------------
conexao ={
        "SERVIDOR": "localhost",
        "PORTA": 8880
}

##----------------Instaciando nosso Socket----------------------------
socketCliente = 	socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketCliente.connect((conexao['SERVIDOR'], conexao['PORTA']))


##-----------Definindo uma funcao --------------------------
request = {"funcao": "color", "valor": "red"}
enviar(socketCliente, request)
request = {"funcao": "forward", "valor": 100}
enviar(socketCliente, request)

while True:
	dado = socketCliente.recv(1024)
	if not dado: break
	print("Resposta do servidor: ", dado.decode())
socketCliente.close()