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
Exemplo de mensagem:
    ```bash
        $ request = {"funcao": "color", "valor": "red"} 
    ```
Onde que:
*   funcao: deve ser informado o nome da funcao desejada
*   valor: deve ser informado o valor para a funcao que esa sendo informada.

## Server: 
Recebe a instrução  proveniente do Client e desenha na tela a respectiva instrução e desvolve algum tipo de resposta ao client.
Repostas:
*   200: OK (Função existe no servidor)
*   404: NOK (Função não foi encontrada no servidor)
