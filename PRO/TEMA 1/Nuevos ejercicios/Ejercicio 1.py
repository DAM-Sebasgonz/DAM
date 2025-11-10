# EJERCICIO 1 CALCULADORA DE IMC CON DIAGNOSTICO

peso = float(input('Introduzca su peso (Kg) --> '))
altura = float(input('Introduzca su altura (m) --> '))

imc = peso/pow(altura, 2)

if imc < 18.5:
    print('El paciente tiene un peso bajo')
elif 18.5 <= imc < 25.0:
    print('El paciente tiene un peso normal')
elif 25.0 <= imc < 30.0:
    print('El paciente tiene sobrepeso')
elif 30.0 <= imc:
    print('El paciente tiene obesidad')