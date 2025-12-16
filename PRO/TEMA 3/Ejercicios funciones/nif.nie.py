#CREAR UNA FUNCION DE NOMBRE 
#verificarNIF_NIE
#Parametros (nif_nie)
#retornaa TRUE/FALSE

def verificar_NIF_NIE(valor:str)-> bool:
    """"Verificar que valor sea un NIF o NIE correcto.
    valor es el nif o nie a validad"""
    #PRIMERO HABRA QUE COMPROBAR SI EL NIF O NIE TIENE LONGITUD DE 9 CARACTERES INCLUIDA LA LETRA

    alfabeto_nif = "TRWAGMYFPDXBNJZSQVHLCKE"
    
    if len(valor_leido) != 9:
        return False
    if valor[:8].isdigit():
        if alfabeto_nif[int(valor[:8])% 23] != valor [-1]:
            return False
    else:
        

    return True

if __name__ == "__main__":
    valor_leido = input("NIF/NIE ==> ")
    print(f"El valor leido del nif/nie {valor_leido} es {verificar_NIF_NIE(valor_leido)}")