import socket
from io import StringIO
import json
from io import StringIO
from turtle import *

##-----------------------Definindo o Objeto Turtle--------------------------------##
class Tartaruga(object):
	
	def __init__(self, shape, speed):
		self.shape = shape
		self.speed = speed

	def hello(self):
		print ("hello world !")
	
	def TurtleForward(self, valor):
		forward(valor)
		
	def TurtleBackward(self, valor):
		backward(valor)
		
	def TurtleLeft(self, valor):
		left(valor)
		
	def TurtleRith(self, valor):
		right(valor)

	
def error404(x):
		print("Error 404, Função: ", x, " não foi encontrada \n")


##-----------------------Funcão Processa Request ---------------------------------##

def processa(dado):
	
	
	JsonDado =  json.loads(dado.decode()) ## Recupera o JSON
	funcao = JsonDado['funcao']  ## Recupera todas a funcao passada
	shape =  "turtle" ## Recupera o shape que se deseja, Ex: turtle = tartaruga, arrow = seta, square = quadrado
	speed = 5  ## Recupera a velocidade com que a tartaruga desenha

	t1 = Tartaruga(shape, speed)

	dict = {
			"hello" : t1.hello, 
			"forward": t1.TurtleForward, 
			"backward": t1.TurtleBackward,
			"left": t1.TurtleLeft, 
			"right": t1.TurtleRith 
			}

	def switch( funcao ):
		try:
			valor = JsonDado['valor'] ## Recupera o valor para funcao
			dict[funcao](valor)
			return ("OK: 200\n")
		except:
			error404(funcao)
			return("Error: 404\n")
	resposta = switch(funcao)
	return (resposta)
##-----------------------Função Main ---------------------------------##

print('Iniciando servidor')

socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServidor.bind(('', 8880))

socketServidor.listen(1)

print("...esperando conexoes ...")
conexao, endereco = socketServidor.accept()
print("Conexão estabelecida com endereco: ", endereco)


while True:
	dado = conexao.recv(1024)
	print (dado)
	if not dado: break
	resposta = processa(dado)
	conexao.sendall(resposta.encode())
socketServidor.close()

