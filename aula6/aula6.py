"""
Iniciar com letra, pode conter números, separar _, letras minúsculas

"""

nome = input('Qual o seu nome ? \n')
idade = input('Qual a sua idade ? \n')  #int
altura = float(input('Qual a sua altura ? \n'))  #float
#e_maior = idade > 18  #boolean
peso = int(input('Quantos KG você tem ? \n'))

imc = peso / altura ** 2

print(imc)

if imc >= 16 and imc <= 16.9:
     print(f'Olá {nome} você tem: {idade} anos de idade e seu imc é: {imc} Muito abaixo do peso --> Queda de cabelo, infertilidade, ausência menstrual')

elif imc >= 17 and imc <= 18.4:
    print(f'Olá {nome} você tem: {idade} anos de idade e seu imc é: {imc} Abaixo do peso --> Fadiga, stress, ansiedade')

elif imc >= 18.5 and imc <= 24.9:
    print(f'Olá {nome} você tem: {idade} anos de idade e seu imc é: {imc} Pesso Normal --> Menor risco de doenças cardíacas e vasculares')

elif imc >= 25 and imc <= 29.9:
    print(f'Olá {nome} você tem: {idade} anos de idade e seu imc é: {imc}  Acima do peso --> Fadiga, má circulação, varizes')

elif imc >= 30 and imc <= 34.9:
    print(f'Olá {nome} você tem: {idade} anos de idade e seu imc é: {imc}  Obesidade Grau I --> Diabetes, angina, infarto, aterosclerose')

elif imc >= 35 and imc <= 40:
    print(f'Olá {nome} você tem: {idade} anos de idade e seu imc é: {imc}  Obesidade Grau II --> Apneia do sono, falta de ar')

elif imc > 40:
    print(f'Olá {nome} você tem: {idade} anos de idade e seu imc é: {imc}  Obesidade Grau III --> Refluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC')





