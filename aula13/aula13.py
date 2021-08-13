num1 = input('Digite um numero ')
num2 = input('Digite um numero ')
""" 
# isnumeric isdigit isdecimal Verificam se uma varivel contem um numero

print(num1.isdecimal())

#Testa se todos os caracteres são numericos (123456) retornando True caso seja float vai retornar False
print(num2.isnumeric())

 """
 
""" if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    resultado = num1 + num2
    print(f'O resultado é {resultado}')
else:
    print('Você precisa digitar apenas numeros')  """

try: #Tente executar esse bloco
    num1 = int(num1)
    num2 = int(num2)
    resultado = num1 + num2
    print(f'O resultado é {resultado}')
except: #Caso não consiga execute esse aqui
    print('Erro: Você não digitou numeros validos')

