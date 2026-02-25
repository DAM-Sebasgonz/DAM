class formateadorMayusculas:
    def formatea (self, cadena):
        return cadena.upper()

class formateadorMinusculas:
    def formatea (self, cadena):
        return cadena.lower ()

def formatear(objeto, cadena):
    return objeto.formatea(cadena)

if __name__ == '__main__':
    f_may = formateadorMayusculas()
    f_min = formateadorMinusculas()

    print('\n'+ formatear(f_may, 'Esto Tiene Letras De Los Dos Tipos'))
    print('\n'+ formatear(f_min, 'Esto Tiene Letras De Los Dos Tipos' ))