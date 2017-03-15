## Dados do Aluno:

* Aluno: Marco Túlio Macedo Rodrigues;
* Matricula: 135834;
* Professor: Ricardo Rocha;

<br/>

Projeto desenvolvido para disciplina de Redes de Computadores 2 na Universidade Federal De Goiás.
Nesse projeto será desenvolvido um protocolo de comunicação entre um Client e um Server para aplicação Turle do Python.

<br/>

## Cliente:
Envia uma mensagem ao servidor informando a instrução desejada e seu respectivo valor.


Exemplo de mensagem com 1 parametro:
    
```bash
$ {"funcao": "color", "valor": ["red"]}
```
Onde que:
*   funcao: deve ser informado o nome da funcao desejada. (Ex: Color)
*   valor: deve ser informado o valor para a funcao que esa sendo informada. (Ex: Red )


Exemplo de mensagem com N parametros:

```bash
$ {"funcao": "nome_funcao", "valor": [param_1, param_2, ..., param_N]} 
```

## Server: 
Recebe a instrução  proveniente do Client e desenha na tela a respectiva instrução e devolve algum tipo de resposta ao client.

Repostas:
*   200: OK (Função existe no servidor)
*   404: NOK (Função não foi encontrada no servidor)
*	4756: Requisicão Inválida
