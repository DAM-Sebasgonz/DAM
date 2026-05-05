import json

def muestraResumenPorAula(nombre_fichero):
    with open(nombre_fichero, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    
    asignaturas = datos[0].keys()
    resumen = {}
    
    for asig in asignaturas:
        notas = [alumno[asig] for alumno in datos]
        min_n = min(notas)
        max_n = max(notas)
        media = sum(notas) / len(notas)
        resumen[asig] = [('min', min_n), ('max', max_n), ('media', media)]
    
    nombre_aula = nombre_fichero.replace(".json", "")
    print(f"Resultados para {nombre_aula}")
    for asig, stats in resumen.items():
        print(f"{asig}: min {stats[0][1]}, max {stats[1][1]}, average {stats[2][1]}")
    print("-" * 30)
    
    return resumen

def comparaAulas(aula_a, aula_b):
    resultado = []
    asignaturas = aula_a.keys()
    
    for asig in asignaturas:
        d_asig = {"materia": asig}
        
        # Comparar Minima, Maxima y Media
        for i, metrica in enumerate(["minima", "maxima", "media"]):
            val_a = aula_a[asig][i][1]
            val_b = aula_b[asig][i][1]
            
            if val_a == val_b:
                aula_top = "ambas"
                nota_top = val_a
            elif (metrica == "minima" and val_a < val_b) or (metrica != "minima" and val_a > val_b):
                aula_top = "eso01a"
                nota_top = val_a
            else:
                aula_top = "eso01b"
                nota_top = val_b
                
            d_asig[metrica] = {"nota": round(nota_top, 1), "aula": aula_top}
        
        resultado.append(d_asig)
    
    with open('resumen_eso01.json', 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=3, ensure_ascii=False)

# Ejecución
resumen_a = muestraResumenPorAula("eso01a.json")
resumen_b = muestraResumenPorAula("eso01b.json")
comparaAulas(resumen_a, resumen_b)