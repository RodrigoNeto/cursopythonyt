""" 
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario descrito, exiba a saudação apropriada. 
Ex.
Bom dia 0-11, 
Boa tarde  12-17, 
Boa Noite 18-23

"""

horario = input('Que horas são agora? ')

if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('Horario deve ser entre 0 e 23')
    else:
        if horario <= 11:
            print('Bom Dia !')
        elif horario <= 17:
            print('Bom Tarde !')
        else:
            print('Boa Noite !')       
else:
    print('Horario deve ser entre 0 e 23')
