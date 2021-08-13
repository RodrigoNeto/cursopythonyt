""" 
uma condição for verdadeira

Requisitos: Entender condições e operadores 
"""

while True:
   
    print()
    nume_1 = input('Digite um numero: ')
    nume_2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')
    
    
    
   
    if not nume_1.isnumeric() or not nume_2.isnumeric():
        print('Você precisa digitar um numero')
        continue   
    
    nume_1 = int(nume_1)
    nume_2 = int(nume_2)
    
    # + - / *
    if operador == '+':
        print(nume_1 + nume_2)
    elif operador == '-':
        print(nume_1 - nume_2)
    elif operador == '/':
        print(nume_1 / nume_2)
    elif operador == '*':
        print(nume_1 * nume_2)
        
    sair = input('Degite [s] para sair e [n] para continua: ')    
    if sair == 's':
        break




    