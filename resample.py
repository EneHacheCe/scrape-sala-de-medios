import os
import pandas as pd

# Configurar los directorios
input_folder = 'planillas de cualquier tamaño'  # Carpeta que contiene los archivos de entrada CSV
output_folder = 'planillas resampled'  # Carpeta donde se guardarán los nuevos CSV divididos

# Crear carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Número máximo de filas por archivo de salida
MAX_ROWS_PER_FILE = 1500

# Listar todos los archivos CSV en la carpeta de entrada
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
csv_files.sort()
print(csv_files)

main_df = pd.DataFrame()
# Procesar cada archivo CSV
for file in csv_files:
    file_path = os.path.join(input_folder, file)
    
    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv(file_path)

    main_df = pd.concat([main_df,df])
    print(df.columns)
    print(len(main_df))
    
# Calcular el número de archivos necesarios para dividir las filas
num_files = (len(main_df) // MAX_ROWS_PER_FILE) + 1

# Crear archivos divididos de 3000 filas
for i in range(num_files):
    start_row = i * MAX_ROWS_PER_FILE
    end_row = (i + 1) * MAX_ROWS_PER_FILE
    df_chunk = main_df.iloc[start_row:end_row]  # Dividir el DataFrame

    # Definir el nombre del archivo de salida
    output_file_name = f"planilla {i+1}.csv"
    output_file_path = os.path.join(output_folder, output_file_name)
    
    # Guardar el DataFrame dividido en un archivo CSV
    df_chunk.to_csv(output_file_path, index=False)
    
    print(f"Archivo guardado: {output_file_path}")

print("Acá me detengo.")