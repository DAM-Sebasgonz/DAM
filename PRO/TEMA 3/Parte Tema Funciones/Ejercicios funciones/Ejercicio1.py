def numeroIntervalo(valor, limite_inferior, limite_superior):
    if valor >= limite_inferior and valor <= limite_superior:
        return True
    return False


if __name__ == "__main__":
    valor = int(input("Introduzca Valor: "))
    lim_inf = int(input("Introduzcs limite Inferior: "))
    lim_sup = int(input("Introduzca limite Superior: "))
    if lim_inf > lim_sup:
        print("Error .... los limites no son correctos")
        exit(0)

    valor_retornado = numeroIntervalo(valor, lim_inf, lim_sup )
    print(f"{valor} esta dentro del intervarlo") if valor_retornado else print(f"{valor} no esta dentro del intervalo")
