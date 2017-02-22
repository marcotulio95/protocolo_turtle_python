import base64
import socket
import json
import jsonpickle
from io import StringIO


##-----------------Definindo o objeto Request -------------------##

class Request (object):
	
	def __init__(self, nome, servidor, porta, funcao, valor):
		self.nome = nome
		self.servidor = servidor
		self.porta = porta
		self.funcao = funcao
		self.valor = valor


print('Iniciando cliente')

r1 = Request("Marco Tulio", "localhost", 8880, "move", 10)

r1Json = jsonpickle.encode(r1)

print (r1Json['nome'])

##r1Json = json.dumps(r1)

"""
socketCliente = 	socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketCliente.connect((r1.servidor, r1.porta))

socketCliente.sendall(r1Json.encode())

while True:
	dado = socketCliente.recv(1024)
	if not dado: break
	print("Resposta do servidor: ", dado)
socketCliente.close()
"""