''' 
iteração de Strings usando while
passar por cada letra de uma string 
'''


frase = 'o rato roeu a roupa do rei de roma'
tamhanho_frase = len(frase)
contador = 0
nova_string = ''
input_do_usuario = input('Qual letra deseja colocar maiúscula: ') 

#Iteração <- Iterar


while contador < tamhanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string) 



