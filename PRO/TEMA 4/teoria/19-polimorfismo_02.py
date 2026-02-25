class NumeroDecimal:
    def __init__(self, numero_original):
        self._num = numero_original

    def numero(self):
        return self._num

class NumeroBinario(NumeroDecimal):

    def numero(self):
        return bin(self._num)

class NumeroHexadecimal(NumeroDecimal):
    def numero (self):
        return hex(self._num)

if __name__ == '__main__':

    b = NumeroBinario(78)
    h = NumeroHexadecimal(78)

    print( '\n' + b.numero())
    print( '\n' + h.numero())