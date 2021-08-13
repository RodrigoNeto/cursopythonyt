"""
COntas a quantidade de caracteres com a função Len

"""

usuario = input('Digite o seu usuario')
senha = input('Digite a sua senha')

senha_validada = len(senha)


if senha_validada >= 6:
    print('Login bem sucedido')
else:
    print('Senha com poucos caracteres')


print(usuario.__len__())
minusculo = usuario.lower()


print(usuario.islower())

print(minusculo)