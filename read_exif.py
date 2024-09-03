import exiftool
import os
import pandas as pd

# Especifica el directorio que quieres leer
directorio = "descargas"

# Obtener una lista de todos los archivos en el directorio
nombres_archivos = os.listdir(directorio)
paths = ['descargas/{0}'.format(archivo) for archivo in nombres_archivos]

with exiftool.ExifToolHelper(executable="Image-ExifTool-12.93/exiftool") as et:
    metadata = et.get_metadata(paths)

imagenes = pd.read_csv('imagenes.csv')
imagenes.set_index("nombre_archivo_original", inplace=True)

terminos_a_eliminar_del_copyright = [
    "Intendencia de Montevideo",
    "Comunicación Desarrollo Ambiental",
    "Intendencia de montevideo",
    "/"
]

i = 0
for i in range(len(metadata)):

    artist = metadata[i].get('EXIF:Artist', '').replace(";"," ").replace("  "," ")
    copyright = metadata[i].get('EXIF:Copyright', '').replace(";"," ").replace("  "," ")

    # Si el campo artist está vacío, usar el copyright
    if not artist:
        artist = copyright
        for term in terminos_a_eliminar_del_copyright:
            artist = artist.replace(term,"")

    index = nombres_archivos[i]
    imagenes.loc[index, "fecha_exif"] = metadata[i].get('EXIF:DateTimeOriginal', '')
    imagenes.loc[index, "autor"] = artist
    imagenes.loc[index, "copyright_exif"] = copyright

imagenes.reset_index(inplace=True)
imagenes.to_csv('imagenes_con_exif.csv', index=False)