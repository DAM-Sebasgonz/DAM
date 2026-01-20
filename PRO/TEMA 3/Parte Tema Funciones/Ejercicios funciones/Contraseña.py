#VERIFICAR LA CONTRASEÑA ENTRE 8  Y 12 CARACTERES 
#DEBE TENER AL MENOS UN DIGITO
#DEBE TENER AL MENOS UNA LETRA MINUSCULO
#DEBE TENER AL MENOS UNA LETRA MAYUSCULA
#DEBE TENER AL MENOS UNO DE ESTOS CARACTERES *$@#%&-

def verificarContraselña(valor:str) -> bool:

    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    digitos = "0123456789"
    signo = "*$@#%&_"

    if len(valor) < 8 or len(valor) > 12:
        return False
    
    for letra in valor:
        if letra in digitos:
            break
    else:
        return False
    
    for letra in valor:
        if letra in alfabeto.upper():
            break
    else:
        return False
    
    for letra in valor:
        if letra in signo:
            break
    else:
        return False

    return True
if __name__ == "__main__":
    valor_leido = input("NIF/NIE ==> ")
    print(f"El valor leido del nif/nie {valor_leido} es ")