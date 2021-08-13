"""
******************************************************************************
* Criar variáveis para nome (str), idade (int)                               *
* Altura (float) e peso de uma pessoa                                        *
* Criar variável com o ano atual (int)                                       *
* Obter o ano de nascimento da pessoa (Baseado na idade e no ano atual)      *
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura das pessoas)  *
* Exibir um texto com todos os valores na tela usando o F-String (com chaves)*
******************************************************************************
"""

nome = 'João'
idade = 30
altura = 1.80
peso = 90
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'O seu nome é {nome}, idade = {idade}, altura = {altura:.2f}, peso = {peso}, ano de nascimento = {ano_nascimento} e IMC = {imc:.2f}')