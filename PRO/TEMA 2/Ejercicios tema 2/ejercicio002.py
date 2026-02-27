# ─────────────────────────────────────────────
# EJERCICIO 002 - TOKENIZADOR DE TEXTO
# ─────────────────────────────────────────────

texto = "Hola mundo. Adiós mundo, hola de nuevo. Otr0 m3nud@ 23"

# Lista con minúsculas (pos 0-25) y mayúsculas (pos 26-51) para convertir con replace()
LETRAS = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

DIGITOS = ['0','1','2','3','4','5','6','7','8','9']

# ─────────────────────────────────────────────
# PASO 1: REEMPLAZAR LETRAS ACENTUADAS
# ─────────────────────────────────────────────

sustituciones = [
    ('á', 'a'), ('é', 'e'), ('í', 'i'), ('ó', 'o'), ('ú', 'u'),
    ('Á', 'a'), ('É', 'e'), ('Í', 'i'), ('Ó', 'o'), ('Ú', 'u'),
    ('ü', 'u'), ('Ü', 'u'),
    ('ñ', 'n'), ('Ñ', 'n'),
]

texto_limpio = texto
for par in sustituciones:
    texto_limpio = texto_limpio.replace(par[0], par[1])

pos_may = 26
while pos_may <= 51:
    mayus = LETRAS[pos_may]
    minus = LETRAS[pos_may - 26]
    texto_limpio = texto_limpio.replace(mayus, minus)
    pos_may += 1

# ─────────────────────────────────────────────
# PASO 3: REEMPLAZAR SIGNOS (no letras ni dígitos) POR ESPACIOS
# ─────────────────────────────────────────────

texto_sin_signos = ""
for c in texto_limpio:
    if c in LETRAS[0:26] or c in DIGITOS or c == ' ':
        texto_sin_signos += c
    else:
        texto_sin_signos += ' '
texto_limpio = texto_sin_signos

# ─────────────────────────────────────────────
# PASO 4: DIVIDIR EN PALABRAS MANUALMENTE
# ─────────────────────────────────────────────

palabras_raw = []
palabra_actual = ""
for c in texto_limpio:
    if c == ' ':
        if palabra_actual != "":
            palabras_raw.append(palabra_actual)
            palabra_actual = ""
    else:
        palabra_actual += c
if palabra_actual != "":
    palabras_raw.append(palabra_actual)

# ─────────────────────────────────────────────
# PASO 5: ELIMINAR PALABRAS QUE CONTENGAN DÍGITOS
# ─────────────────────────────────────────────

palabras_limpias = []
for palabra in palabras_raw:
    tiene_digito = False
    for c in palabra:
        if c in DIGITOS:
            tiene_digito = True
    if not tiene_digito:
        palabras_limpias.append(palabra)

# ─────────────────────────────────────────────
# PASO 6: CREAR VOCABULARIO
# ─────────────────────────────────────────────

vocabulario = {}
contador = 0

for palabra in palabras_limpias:
    if palabra not in vocabulario:
        vocabulario[palabra] = contador
        contador += 1

# ─────────────────────────────────────────────
# PASO 7: MOSTRAR VOCABULARIO
# ─────────────────────────────────────────────

print("--- VOCABULARIO ---")
for palabra in vocabulario:
    print(palabra + " > " + str(vocabulario[palabra]))

# ─────────────────────────────────────────────
# PASO 8: CODIFICAR EL TEXTO ORIGINAL
# ─────────────────────────────────────────────

texto_codificado = []
for palabra in palabras_limpias:
    texto_codificado.append(vocabulario[palabra])

print("\nTexto codificado: " + str(texto_codificado))
