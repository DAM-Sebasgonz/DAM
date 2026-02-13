def analizaLista(lista_rec):
    if lista_rec == []:
        return [], []
    
    mivalor =lista_rec[0]
    num_rec_total, letras_rec_total =  analizaLista(lista_rec[1:])

    if type(mivalor) == int:
        num_rec_total.append(mivalor)
        # num_rec_total.sort()
    elif type(mivalor) == str:
        letras_rec_total.append(mivalor)
    else:
        num_rec_iteracion, letras_rec_iteracion =  analizaLista(mivalor)
        num_rec_total.extend(num_rec_iteracion)
        letras_rec_total.extend(letras_rec_iteracion)

    return sorted(num_rec_total) , sorted(letras_rec_total)

if __name__ == "__main__":
    lista = [2, "a", [1, "b"], "d", "c", 3, ["z", "a", 4], 5]
    print(analizaLista(lista))