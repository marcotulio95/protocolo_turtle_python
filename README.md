Aluno: Marco Túlio Macedo Rodrigues;
Matricula: 135834;
Professor: Ricardo Rocha;

Projeto desenvolvido para disciplina de Redes de Computadores 2 na Universidade Federal De Goiás.

Nesse projeto será desenvolvido um protocolo de comunicação entre um Client e um Server para aplicação Turle do Python.

Client: Envia uma mensagem informando uma intrução para a turtle.

Exemplo de mensagem: 

request = {"funcao": "color", "valor": "red"}, onde que:
	funcao: recebe o nome da funcao desejada
	valor: recebe o valor que deve ser aplicado a funcao.

Server: Recebe a instrução  proveniente do Client e desenha na tela a respectiva instrução e desvolve
algum tipo de resposta ao client.
