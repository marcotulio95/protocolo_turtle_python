import socket
from io import StringIO
import json
from io import StringIO

##-----------------------Definindo o Objeto Turtle--------------------------------##
class Tartaruga(object):
	
	def hello(self):
		print ("hello world !")
	
def error404():
		print("Error 404")

##-----------------------Funcão Processa Request ---------------------------------##

def processa(dado):
	
	t1 = Tartaruga()
	dict = {"hello" : t1.hello}

	JsonDado =  json.loads(dado.decode())
	funcao = JsonDado['funcao']

	def switch( x ):
		try:
			dict[x]()
		except:
			error404()

	switch(funcao)

##-----------------------Função Main ---------------------------------##

print('Iniciando servidor')

socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketServidor.bind(('', 8888))

socketServidor.listen(1)

print("...esperando conexoes ...")
conexao, endereco = socketServidor.accept()
resposta = '200\n'

while True:
	dado = conexao.recv(1024)
	if not dado: break
	processa(dado)
	conexao.sendall(resposta.encode())
socketServidor.close()
