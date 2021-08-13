''' 
Formatando valores com modificadores

:s ----- Strings (strings)
:d ----- Inteiros (int)
:f ----- Número de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:.(CARACTERES) (> ou < ^) (QUANTIDADE) (TIPO - s. d ou f)

> -------- Esquerda
< -------- Direita
^ -------- Centro
'''

num_1 = 10
num_2 = 3

divisao = num_1 / num_2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')


num_3 = 1
print(f'{num_3:0>10}')

num_4 = 1150
print(f'{num_4:0<10}')

texto = 'Python_s2'

for letra in texto:
    print(letra)


