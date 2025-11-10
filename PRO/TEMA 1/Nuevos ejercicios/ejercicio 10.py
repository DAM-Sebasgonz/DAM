# Calculadora de Impuestos Progresiva
# Escribe un programa que calcule el impuesto sobre la renta según: 
# Salario anual, estado civil (soltero/casado como string), 
# número de dependientes, 
# tiene deducciones médicas (booleano). 
#
# Los tramos son: 
# 0% hasta $10,000, 
# 10% de $10,001-$30,000, 
# 20% de $30,001-$60,000, 
# 30% sobre $60,000. 
# Aplicar deducciones:
# $2,000 por dependiente, 
# $3,000 por ser casado, 
# $1,500 si tiene deducciones médicas.

salario_anual = float(input("introduzca salario anual bruto"))
estado_civil = input("introzuca estado civil")
dependientes = int(input("Introduzca el numero de personas a su cargo"))
deduccion = input("deducciones medicas?")

if salario_anual < 10000:
    impuesto = salario_anual * 0
elif 10001 < salario_anual <= 30000:
    impuesto = salario_anual * 0.1
elif 30001 < salario_anual <= 60000:
    impuesto = salario_anual * 0.2
elif salario_anual > 60000:
    impuesto = salario_anual * 0.3