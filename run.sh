#!/bin/bash

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
    python3 sala_de_medios.py
elif command -v python &>/dev/null; then
    python sala_de_medios.py
fi