nome = 'João'
idade = 35  #int
altura = 1.80  #float
peso = 100

print('O seu nome é ' + nome + ' e você tem ' + str(idade) + ' anos de idade e sua altura é ' + str(altura))
print(f'O seu nome é {nome} e você tem {idade} anos de idade e sua altura é {altura:.2f}')  #Forma correta de realizar formatação
print('O seu nome é {} e você tem {} anos de idade e sua altura é {:.2f}'.format(nome, idade, altura))  #Forma correta de realizar formatação