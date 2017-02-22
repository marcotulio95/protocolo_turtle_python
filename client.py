import base64
import socket
import json
from io import StringIO

conexao ={
        "SERVIDOR": "localhost",
        "PORTA": 8888
}

request = {"funcao": "forward", "valor": 100 }

print('Iniciando cliente')

requestJson = json.dumps(request)

socketCliente = 	socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketCliente.connect((conexao['SERVIDOR'], conexao['PORTA']))

socketCliente.sendall(requestJson.encode())

while True:
	dado = socketCliente.recv(1024)
	if not dado: break
	print("Resposta do servidor: ", dado.decode())
socketCliente.close()