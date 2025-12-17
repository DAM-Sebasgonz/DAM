def muestraVocales(texto:str) -> dict:
    if texto == "":
        lista = [0,0,0,0,0]
        return lista
    
    lista_retornada = muestraVocales(texto[1:])
     

if __name__ == "__main__":
    diccionario = muestraVocales("murcielago")
    for i in diccionario.items():
        print(i)