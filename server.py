import socket
from io import StringIO

##-----------------------Função Main ---------------------------------##

print('Iniciando servidor')

socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketServidor.bind(('', 8888))

socketServidor.listen(1)

print("...esperando conexoes ...")
conexao, endereco = socketServidor.accept()
resposta = '200'

while True:
	dado = conexao.recv(1024)
	if not dado: break
	print (dado)
	conexao.sendall(resposta.encode())
socketServidor.close()
