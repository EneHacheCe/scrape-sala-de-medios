#!/bin/bash
#DOWNLOAD_FOLDER="descargas"

# Crear el entorno virtual, usando python3 si está disponible, de lo contrario usa python
if command -v python3 &>/dev/null; then
    python3 -m venv .
elif command -v python &>/dev/null; then
    python -m venv .
else
    echo "Python no está instalado."
    exit 1
fi

# Activar el entorno virtual
source bin/activate

# Instalar los paquetes desde requirements.txt
pip install -r requirements.txt

echo "Entorno virtual creado y paquetes instalados."

# Crear el entorno virtual, usando python3 si está disponible, de lo contrario usa python
if command -v python3 &>/dev/null; then
    python3 scrape.py
elif command -v python &>/dev/null; then
    python scrape.py
fi

#crear la carpeta de descargas
#mkdir -p $DOWNLOAD_FOLDER

#wget -i "image_urls.txt" -P $DOWNLOAD_FOLDER -q -nc -nd -c --content-disposition

