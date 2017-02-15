import base64
import socket
import json
from io import StringIO

request = {
        "nomeOrigem": "MarcoTulio",
        "SERVIDOR": "localhost",
        "PORTA": 8888,
        "dado": ["arq1.txt", "arq2.txt"]
    }

print('Iniciando cliente')
requestJson = json.dumps(request)

socketCliente = 	socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketCliente.connect((request['SERVIDOR'], request['PORTA']))

socketCliente.sendall(requestJson.encode())

while True:
	dado = socketCliente.recv(1024)
	if not dado: break
	print("Resposta do servidor: ", dado)
socketCliente.close()