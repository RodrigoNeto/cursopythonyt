"""
+, *, /, //, **, %, ()
"""
print('Multiplicação *', 10 * 10)
print('Repetição de String *', 10 * 'Rodrigo ')
print('Adição +', 10 + 10)
print('Subtração -', 10 - 10)
print('Divisão /', 10 / 10)
print('Divisão sem sobra //', 25 // 10 )
print('Potenciação **', 2 ** 2 )
print('Módulo/Resto da divisão %', 25 % 10)

idade = 30

#Não é recomendado formatar dessa forma
print('Eu tenho ' + str(idade) + ' anos de idade!')  # Fazendo casting na idade convertendo para string

print('Alteração de prescedência das operações ()', 5+2*10)
print('Alteração de prescedência das operações ()', (5+2)*10)

