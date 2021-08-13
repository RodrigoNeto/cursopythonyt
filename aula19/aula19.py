""" 
uma condição for verdadeira

Requisitos: Entender condições e operadores 
"""
x = 0 # Coluna

while x <= 10:
    y = 0 # Linha
    
    while y <= 5:
        print(f'({x},{y})')
        y += 1
        
    x += 1 # x = x+1 
    
print('Acabou o código !!!')