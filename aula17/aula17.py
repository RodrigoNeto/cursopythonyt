""" 
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
4 letras ou menos escreva 'seu nome é muito curto'; se tiver entre 5 e 6 letras, escreva
'Seu nome é normal'; maior que 6 escreva 'Seu nome pe muito grande' 
"""

primeiro_nome = input("Digite o seu primeiro nome: ")
print("- - - - - - - - - - - - - - - - - - - - - - ")

nome_counter = len(primeiro_nome)

if nome_counter <= 4:
    print(f'{primeiro_nome} seu nome é muito curto')
elif nome_counter <= 6:
    print(f'{primeiro_nome} seu nome é normal')
elif nome_counter > 6:
    print(f'{primeiro_nome} seu nome é muito grande')