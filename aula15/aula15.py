""" 
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um Número
inteiro, informe que não é um numero inteiro
"""


num1 = input('Digite um numero ')
print('- - - - - - - - - - - - - - - - ')

try:
    num = int(num1)
    resultado = num % 2
    if num1.isnumeric():
        print(f'Perfeito, você digitou o numero {num1}')
    else:
        print('Não é numero inteiro')

    if resultado == 0:
        print(f'{num1} é um numero par')
    else:
        print(f'{num1} é um numero impar')
except:
    print('Erro: Digite apenas numero')  
    
    

    
    
  