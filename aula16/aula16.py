""" 
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario descrito, exiba a saudação apropriada. 
Ex.
Bom dia 0-11, 
Boa tarde  12-17, 
Boa Noite 18-23

"""

hora = input('Que horas são agora? ')

hora = int(hora)

if hora >= 0 and hora <= 11:
    print('Bom dia')
elif hora >= 12 and 17:
    print('Boa tarde')
elif hora >= 18 and 18 <= 23:
    print('Boa noite')   
    
     