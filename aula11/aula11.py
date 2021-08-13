"""
Operadores lógicos
and, or, not
in e not in
"""
# a = ''
# b = 0
# nome = 'João'
#
# # Ferificando se a variavel a foi preenchida
# if not b:
#     print('Por favor, preencha o valor')
#
# #Verificando se contem uma letra especifica em uma variavel com o IN
# if 'R' in nome:
#     print('Seu nome tem a letra R')
# else:
#     print('Seu nome não tem a letra R')

# Login de um sistema exemplo

usuario = input('Digite o usuario')
senha = input('Digite a sua senha')

usuario_db = 'Rodrigo'
senha_db = '123'

if senha_db == senha and usuario_db == usuario:
    print('Você esta logado no sistema')
else:
    print('Usuario ou senha estão incorretos')



