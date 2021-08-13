""" 

Falo for nos permite percorrer os itens de uma coleção e para cada um deles, 
executar um bloco de código declarado no loop

"""
""" 
#primeiro argumento do range é o inicio 100, depois o fim 0 e por ultimo o incremento/decremento -10
for n in range(100,0,-10):
    print(n)
 """
 
 #continue - Pula para o proximo laço
 #break - Termina o laço 
 
texto = 'Python'
nova_string = ''


for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)
    