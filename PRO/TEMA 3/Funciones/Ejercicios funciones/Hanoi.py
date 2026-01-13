#Ejercicio Recursividad.

def hanoi(inicial:str,final:str,auxiliar:str,n:int):
    if n != 0:
        hanoi(inicial,auxiliar,final, n-1)
        print(f"Disco {n} de {inicial} --> {final}")
        hanoi(auxiliar,final,inicial, n-1)

if __name__ == "__main__":
    hanoi("A", "C", "B", 4)