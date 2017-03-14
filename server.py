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

	def hello(self, valor1, valor2):
		print ("Valor1: ", valor1)
		print ("Valor2: ", valor2)
	
	def TurtleForward(self, valor):
		forward(valor)
		
	def TurtleBackward(self, valor):
		backward(valor)
		
	def TurtleLeft(self, valor):
		left(valor)
		
	def TurtleRith(self, valor):
		right(valor)

	def TurtleColor(self, valor):
		color(valor)
	
	def TurtleGoto(self, valor1, valor2):
		goto(valor1,valor2)
	def TurtleHome(self):
		home()
	def TurtleCircle(self, valor):
		circle(valor)
	def TurtleDot(self, valor, cor):
		dot(valor,cor)
		
	
def error404(x):
		print("Error 404, Função: ", x, " não foi encontrada \n")


##-----------------------Funcão Processa Request ---------------------------------##

def processa(dado):
	
	try:
		JsonDado =  json.loads(dado.decode()) ## Recupera o JSON
		funcao = JsonDado['funcao']  ## Recupera todas a funcao passada
		shape =  "turtle" ## Recupera o shape que se deseja, Ex: turtle = tartaruga, arrow = seta, square = quadrado
		speed = 5  ## Recupera a velocidade com que a tartaruga desenha
	except json.decoder.JSONDecodeError:
		return ("Error 4756: Requisicao Invalida \n")

	t1 = Tartaruga(shape, speed)
	
	dict = {
			"hello" : t1.hello, 
			"forward": t1.TurtleForward, 
			"backward": t1.TurtleBackward,
			"left": t1.TurtleLeft, 
			"right": t1.TurtleRith,
			"color": t1.TurtleColor,
			"goto": t1.TurtleGoto,
			"home": t1.TurtleHome,
			"circle": t1.TurtleCircle,
			"dot": t1.TurtleDot
			}

	def switch( funcao ):
		try:
			valor = JsonDado['valor'] ## Recupera o valor para funcao
			
			dict[funcao](*valor)

			return ("OK: 200\n")
		except:
			error404(funcao)
			return("Error: 404\n")

			
	resposta = switch(funcao)
	return (resposta)
##-----------------------Função Main ---------------------------------##

print('Iniciando servidor')
											 	##Definindo como Socket UDP
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketServidor.bind(('', 8880))

print("...esperando conexoes ...")

while True:
	dado, enderecoCliente = socketServidor.recvfrom(1024)
	print (dado, " de: ", enderecoCliente)
	if not dado: break
	resposta = processa(dado)
	socketServidor.sendto(resposta.encode(), enderecoCliente)

socketServidor.close()

