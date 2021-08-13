""" 
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um Número
inteiro, informe que não é um numero inteiro
"""


numero_inteiro = input('Digite um numero ')
print('- - - - - - - - - - - - - - - - ')

    
if numero_inteiro.isdigit():
    numero_usuario = int(numero_inteiro)
         
    if numero_usuario % 2 == 0:         
       print(f'Perfeito, você digitou o numero {numero_inteiro} que é inteiro e par')
    else:
        print(f'Perfeito, você digitou o numero {numero_inteiro} que é inteiro e impar')  
else:
        print(f'{numero_inteiro} não é um numero')
        
        
        
        
        

    
    

    
    
  