# verificar pangrama

#pangrama es un texto que tiene todas las letras del abecedario

def verificarPangrama(texto:str) -> bool:
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    texto = texto.lower().replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("u","ú")

    for letra in alfabeto:
        if letra not in texto:
            return False
        
    return True
