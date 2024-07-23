# Scrape Sala de Medios
## Cómo usar este script
### Descargar los datos
1. Asegurate de tener python instalado en tu computadora
```
python3 --version
```
[Ver cómo instalar](https://www.python.org/downloads/)
2. Asegurate de tener instalados los módulos de python `requests`, `os`, `pandas` y `BeautifulSoup`. Podés instalarlos así:
```
python3 -m pip install requests
python3 -m pip install os
python3 -m pip install pandas
python3 -m pip install BeautifulSoup
```
o así
```
apt install python3-requests
apt install python3-os
apt install python3-pandas
apt install python3-BeautifulSoup
```
o buscá más información [acá](https://docs.python.org/3/installing/index.html)
3. Cloná este repositorio o descargá el archivo `sala_de_medios.py`

4. En `sala_de_medios.py` modificá las siguientes líneas según tus preferencias
```
#Comenzar en la página
START_AT_PAGE = 0
# Detenerse al llegar a este al archivo, por ejemplo: 20240716dicimouyplr61.jpg
STOP_AT_FILE = ""
#Detenerse al llegar a las N páginas
SCARPE_MAX_N_PAGES = 10
#Caption en español para las imágenes que no tienen título definido en la web de sala de medios
DEFAULT_CAPTION = "Fotografía de la Sala de Medios de la Intendencia de Montevideo"
```
5. Abrí la terminal y movete a la carpeta donde tenés el archivo `sala_de_medios.py`
6. Ejecutá el script con python
```
python3 sala_de_medios.py
```
6. Se genera un archivo `imagenes.csv` en la misma carpeta. Si el archivo ya existía, se le suman nuevas filas a este mismo archivo. En caso de que el archivo ya existiera, la ejecución del script se detiene al encontrar una foto que ya había sido procesada.
### Filtar fotos y mejorar los metadatos
7. Importar el CSV en Google Sheets. Los pasos 7 al 11 aparecen en [este video](https://drive.google.com/file/d/1Htg9Gv3I7LKEqXcqtvO664k5Dy2r5yJ4/view?usp=sharing)
8. En la columna "previsualización", que aparecerá vacía, agregar la formula `=IMAGE(A:A)`.
9. Google Sheets nos va a pedir permiso para cargar URLS externas. Hay que tocar el botón "Permitir acceso".
10. Arrastrar la fórmula a todas las filas.
11. Ensanchar la columna de previsuaizaciones según necesite
12. Recorrer la planilla chequeando los thumbnails. En caso de necesitar ver la foto en tamaño completo, podés clicar el enlace de la columna "enlace_web". Podés eliminar las filas de las fotos que no necesitamos subir, o bien crear una nueva columna en la que marcar las fotos que no van. También puede ser un buen momento para mejorar las descripciones.
### Reconciliar y subir imágenes
13. Abrir OpenRefine, preferentemente [con bastante memoria asignada](https://openrefine.org/docs/manual/installing#increasing-memory-allocation)
14. Crear un nuevo proyecto en Open Refine y abrir el .CSV descargado.
15. Seleccionar instancia de Wikibase = Wikimedia Commons.
16. Si la planilla aún contiene fotos que no deberían ser subidas a Wikimedia Commons, crear una faceta para filtrarlas.
17. Reconciliar columna `nombre_de_archivo_para_commons`. Cotejar / Inicia cotejo.
18. Crear nuevos archivos para los archivos no entonctados. Cotejar / Acciones / Crear un nuevo elemento para cada celda
19. Crear el esquema de esta forma:
![esquema](readme-esquema.png)
20. Cargar ediciones en Wikimedia Commons. Extensiones Wikidata / Cargar ediciones en Wikidata
## To do
[en este doc](https://docs.google.com/document/d/1at_0rbG2jGkm4pLKOaLI98anqZWGFZfCr8gW1YfLqw8/edit#heading=h.7xnc92h81px)
