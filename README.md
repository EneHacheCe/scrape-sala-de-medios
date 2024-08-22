# Scrape Sala de Medios
## Cómo usar este script
### Descargar los datos
1. Asegurate de tener python instalado en tu computadora
```
python --version
```
o bien
```
python3 --version
```
[Cómo instalar python](https://www.python.org/downloads/)

2. Cloná o descargá este repositorio

3. En el archivo `sala_de_medios.py` modificá las siguientes líneas según tus preferencias
```
#Comenzar en la página
START_AT_PAGE = 0
# Detenerse al llegar a este archivo 
STOP_AT_FILE = "20240716dicimouyplr61.jpg"
#Detenerse al llegar a las N páginas escrapeadas
SCARPE_MAX_N_PAGES = 10
#Caption en español por defecto para las imágenes que no tienen título definido en la web de Sala de Medios
DEFAULT_CAPTION = "Fotografía de la Sala de Medios de la Intendencia de Montevideo"
```
4. Abrí la terminal y movete a la carpeta del proyecto
5. Asegurate de tener permisos para ejecutar el archivo `run.sh`
```
chmod +x run.sh
```
6. Ejecutá el archivo `run.sh`. Este script instalará todas las dependencias en un ambiente virtual y ejecutará el script de scrapping.
```
./run.sh
```
7. El script crea un archivo `imagenes.csv` en la misma carpeta donde nos encontramos. Si el archivo ya existía, el script agrega nuevas filas a este mismo archivo.

### Filtar fotos y mejorar los metadatos
8. Importar `imagenes.csv` en Google Sheets. Los pasos 8 al 12 aparecen en [este video](https://drive.google.com/file/d/1Htg9Gv3I7LKEqXcqtvO664k5Dy2r5yJ4/view?usp=sharing)
9. En la columna "previsualización", que aparecerá vacía, agregar la formula `=IMAGE(A:A)`.
10. Google Sheets nos va a pedir permiso para cargar URLS externas. Hay que tocar el botón "Permitir acceso".
11. Arrastrar la fórmula a todas las filas.
12. Ensanchar la columna de previsuaizaciones según necesite
13. Recorrer la planilla chequeando los thumbnails. En caso de necesitar ver la foto en tamaño completo, podés clicar el enlace de la columna "enlace_web". Podés eliminar las filas de las fotos que no necesitamos subir, o bien crear una nueva columna en la que marcar las fotos que no van. También puede ser un buen momento para mejorar o corregir los contenidos de las columas `fecha`, `caption_es`, `wikitext`, `copyright`,
    `autor`. Tené en cuenta que:
    - Particularmente con las fotos scrapeadas de últimas páginas es probable que la fecha sea incorrecta, y que la fecha correcta se encuentre en la columna `palabras_clave`.
    - Utiliza el formato `YYYY(-mm(-dd))` para las fechas.
    - Es inútil modificar `palabras_clave` (Openrefine no utilizará esa columna).
    - No es buena idea modificar el `nombre_de_archivo_para_commons`, así nos aseguramos de cotejar correctamente contra Wikimedia Commons y no subir archivos duplicados.
    - NO DEBEMOS MODIFICAR: `enlace_web`, `nombre_archivo_original` y `enlace_descarga`.

### Reconciliar y subir imágenes
14. Abrir OpenRefine, preferentemente [con bastante memoria asignada](https://openrefine.org/docs/manual/installing#increasing-memory-allocation)
15. Crear un nuevo proyecto en Open Refine y abrir el .CSV descargado.
16. Seleccionar instancia de Wikibase = Wikimedia Commons.
17. Si la planilla aún contiene fotos que no deberían ser subidas a Wikimedia Commons, crear una faceta para filtrarlas.
18. Reconciliar columna `nombre_de_archivo_para_commons`: Cotejar / Inicia cotejo.
19. Utilizar la faceta generada por el cotejo para para excluír los archivos que ya están en Commons.
20. Crear nuevos archivos para los archivos no entontrados: Cotejar / Acciones / Crear un nuevo elemento para cada celda
21. Crear el esquema de esta forma:
![esquema](readme-esquema.png)
22. Cargar ediciones en Wikimedia Commons. Extensiones Wikidata / Cargar ediciones en Wikidata
## To do
[en este doc](https://docs.google.com/document/d/1at_0rbG2jGkm4pLKOaLI98anqZWGFZfCr8gW1YfLqw8/edit#heading=h.7xnc92h81px)
