# Crea un programa que solicite el precio de un producto y el porcentaje de descuento.
# Muestra el importe del descuento y el precio a pagar. 

prc_producto = float(input("Ingrese el precio del producto: "))
dsc_producto = int(input("Introduzca el descuento del producto: "))

importe_dscont = (prc_producto*dsc_producto) / 100

importe_pagar = prc_producto - importe_dscont

print(f"El importe a pagar es {importe_pagar} y el descuento ha sido de {importe_dscont}")
