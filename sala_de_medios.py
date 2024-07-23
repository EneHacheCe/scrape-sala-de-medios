import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

#Comenzar en la página
START_AT_PAGE = 2133
# Detenerse al llegar a este al archivo, por ejemplo: 20240716dicimouyplr61.jpg
STOP_AT_FILE = "NO REAL FILE!"
#Detenerse al llegar a las N páginas
SCARPE_MAX_N_PAGES = 427
#Caption en español para las imágenes que no tienen título definido en la web de sala de medios
DEFAULT_CAPTION = "Fotografía de la Sala de Medios de la Intendencia de Montevideo"

# URL base de la sala de medios
BASE_URL = "https://montevideo.gub.uy/institucional/sala-de-medios"

#Set headers so that the web does not identify us a bot
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

# Cargar la planilla existente si existe
CSV_FILE = "imagenes.csv"
if os.path.exists(CSV_FILE):
    df_existing = pd.read_csv(CSV_FILE)
    existing_files = df_existing['nombre_archivo_original'].tolist()
else:
    df_existing = pd.DataFrame(columns=['previsualizacion_src','previsualizacion','enlace_web', 'nombre_de_archivo_para_commons', 'fecha', 'palabras_clave', 'caption_es', 'wikitext', 'scrapeada_de_la_pagina_numero','nombre_archivo_original', 'enlace_descarga'])
    existing_files = []

# Obtener el HTML de una página
def get_html(url):
    response = requests.get(url, headers=headers)
    return response.text

# Scrapear una página
def scrape_page(page_number):
    url = f"{BASE_URL}?filename=&field_file_image_title_text_value=&field_categorias_tid_1=&page={page_number}"
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    fotos = soup.find('div',class_='view-biblioteca-de-imagenes').find_all('td')
    print("encontré " + str(len(fotos)) + " fotos en la página " + str(page_number))
    nuevos_datos = []
    
    for foto in fotos:
        nombre_archivo_original = foto.find('div', class_='views-field-filename').find('span', class_='field-content').text.strip()
        
        if nombre_archivo_original in existing_files or nombre_archivo_original == STOP_AT_FILE:
            print("Llegamos a una foto que fue scrappeada anteriormente")
            return nuevos_datos, True
        
        previsualizacion_src = foto.find('img')['src'] if foto.find('img')['src'] else "no se encontró thumnail"
        enlace_descarga = foto.find('div', class_='views-field-download').find('a')['href']
        enlace_web = "https://montevideo.gub.uy" + foto.find('div', class_='views-field-rendered').find('a')['href']
        titulo = foto.find('div', class_='views-field-field-file-image-title-text').find('span', class_='field-content').text.strip()
        nombre_de_archivo_para_commons = titulo + " - " + nombre_archivo_original if titulo else nombre_archivo_original
        fecha = foto.find('div', class_='views-field-timestamp').find('span', class_='field-content').text.strip()
        categorias_im = foto.find('div', class_='views-field-field-categorias').find('span', class_='field-content').text.strip()
        palabras_clave = categorias_im

        # Crear el caption_es
        caption_es = titulo if titulo else DEFAULT_CAPTION 
        
        # Crear wikitext
        wikitext = f"""'=={{{{int:filedesc}}}}==
{{{{Information
|other fields = {{{{Information field|name=Colección|value={{{{Institution:Sala de Medios Intendencia de Montevideo}}}}}}}}
|other fields 1 = {{{{Information field|name=Palabras clave|value={palabras_clave}}}}}
}}}}
=={{{{int:license-header}}}}==
{{{{cc-by-sa-4.0}}}}

[[Category:Files_provided_by_Sala_de_Medios_Intendencia_de_Montevideo]]
"""
        nuevos_datos.append([previsualizacion_src,"",enlace_web, nombre_de_archivo_para_commons, fecha, palabras_clave, caption_es, wikitext, page_number, nombre_archivo_original, enlace_descarga])
        
    return nuevos_datos, False

# Iterar sobre las páginas y scrapear
# modificar este número para empezar en otra página
page_number = START_AT_PAGE
stop_at_page = START_AT_PAGE + SCARPE_MAX_N_PAGES
encontrado_existente = False
nuevos_datos = []

while not encontrado_existente and page_number < stop_at_page:
    nuevos_datos_pagina, encontrado_existente = scrape_page(page_number)
    nuevos_datos.extend(nuevos_datos_pagina)
    page_number += 1

# Si hay nuevos datos, guardarlos en el CSV
if nuevos_datos:
    df_nuevos = pd.DataFrame(nuevos_datos, columns=['previsualizacion_src','previsualizacion','enlace_web', 'nombre_de_archivo_para_commons', 'fecha', 'palabras_clave', 'caption_es', 'wikitext', 'scrapeada_de_la_pagina_numero','nombre_archivo_original','enlace_descarga'])
    df_nuevos['fecha'] = pd.to_datetime(df_nuevos['fecha'], format='%d.%m.%Y').dt.strftime('%Y-%m-%d')
    df_final = pd.concat([df_existing, df_nuevos], ignore_index=True)
    df_final.to_csv(CSV_FILE, index=False)
    print("Nuevos datos añadidos al CSV.")
else:
    print("No se encontraron nuevas imágenes.")
