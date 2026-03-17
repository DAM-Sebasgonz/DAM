#!/bin/bash

Repositorios
REPOS="/mnt/datos_escuela"
REPOSITORIOS=("Fotografía" "Dibujo" "Imágenes")

Log de archivos eliminados
DESCARTADOS_LOG="./descartados.log"

Fecha actual
FECHA=$(date +"%d.%m.%Y")

Procesar todos los repositorios
for REPO in "${REPOSITORIOS[@]}"; do
    RUTA="$REPOS/$REPO"

    for ARCHIVO in "$RUTA"/; do
        EXT="${ARCHIVO##.}"
        TIPO_REAL=$(file -i "$ARCHIVO" 2>/dev/null)

        if [[ "$TIPO_REAL" == "jpeg" ]]; then
            EXT_REAL="jpg"
        elif [[ "$TIPO_REAL" == "png" ]]; then
            EXT_REAL="png"
        elif [[ "$TIPO_REAL" == "gif" ]]; then
            EXT_REAL="gif"
        else
            PROPIETARIO=$(stat -c '%U' "$ARCHIVO")
            GRUPO=$(stat -c '%G' "$ARCHIVO")
            NOMBRE=$(basename "$ARCHIVO")
            rm "$ARCHIVO"
            echo "$PROPIETARIO;$GRUPO;$FECHA;$NOMBRE" >> "$DESCARTADOS_LOG"
            continue
        fi

        if [ "$EXT" != "$EXT_REAL" ]; then
            NUEVO="${ARCHIVO%.*}.$EXT_REAL"
            mv "$ARCHIVO" "$NUEVO"
        fi

    done
done

Backup de todos los repositorios al final del proceso
for REPO in "${REPOSITORIOS[@]}"; do
    RUTA="$REPOS/$REPO"
    DESTINO="/tmp/${REPO}backup$(date +%Y%m%d%H%M%S).tar.gz"
    tar -czf "$DESTINO" -C "$REPOS" "$REPO"
    echo "Backup del repositorio '$REPO' realizado en $DESTINO"
done

echo "Procesamiento completado."