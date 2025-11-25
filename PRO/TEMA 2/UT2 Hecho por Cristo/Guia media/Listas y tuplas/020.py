'''Crea  una  lista  de  caracteres  que  contenga  de  la  ‘A’  a  la  ‘Z’  (sólo  las 
mayúsculas). Después, ve pidiendo posiciones de la lista por teclado y si la posición es 
correcta, se añadira el carácter a una cadena que se mostrara al final, se dejará de insertar 
cuando se introduzca un -1. 
 
Por ejemplo, si escribo los siguientes números: 
 
0 //Añadira la ‘A’ 
5 //Añadira la ‘F’ 
25 //Añadira la ‘Z’ 
50 //Error, inserte otro numero 
-1 //fin 
 
Cadena resultante: AFZ'''
abecedario=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print(len(abecedario))
caracteres=''
while True:
    n=int(input("Escribe un nº de posición entre 0 y 26: "))
    if n==-1:
        break
    elif n>=0 and n<=len(abecedario):
        caracteres+=abecedario[n]
    elif n>len(abecedario):
        print("Error, inserte otro numero.")
print(caracteres)
