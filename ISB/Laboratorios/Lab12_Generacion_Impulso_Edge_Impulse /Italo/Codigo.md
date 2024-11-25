import os
import pandas as pd
import numpy as np
import csv

def funcion_leer(nombre):
    # Leer el archivo
    with open(nombre, 'r') as file:
        # Saltar las líneas de encabezado hasta que termine el EndOfHeader
        while True:
            line = file.readline()
            if "EndOfHeader" in line:
                break
        
        # Cargar los datos en un DataFrame
        data = pd.read_csv(file, delimiter='\t', header=None)
        
    # Seleccionar solo la quinta columna (índice 5, ya que Python empieza desde 0)
    columna_5 = data.iloc[:, 5]
    # Convertir la columna a un array de NumPy
    array_np = np.array(columna_5)
    return array_np

# Carpeta donde están los archivos txt
folder_path = r"C:\Users\italo\Desktop\ISB_Lab_13\codigos"

# Nombres exactos de los archivos txt
nombres_txt = [
    "Ejercicio I deriv",
    "Ejercicio II deriv",
    "Ejercicio III deriv",
    "Estado basal  III deriv",
    "Estado Basal I Deri",
    "Estado basal Toma 1 II deriv",
    "Estado basal Toma 2 I deriv",
    "Estado basal Toma 3 I deriv",
    "Estado con Respiracion I deriv",
    "Estado con Respiracion II deriv",
    "Estado con Respiracion III deriv",
    "Estado sin Respiracion I deriv",
    "Estado sin Respiracion II deriv",
    "Estado sin Respiracion III deriv",
    "Simulacion 60 bpm",
    "Simulacion 90 bpm",
    "Simulacion 120pbm",
    "Simulacion 150 bpm"
]

# Convertir cada archivo txt a csv
for txt_name in nombres_txt:
    txt_path = os.path.join(folder_path, txt_name + ".txt")
    csv_path = os.path.join(folder_path, txt_name + ".csv")  # Nombre del CSV será igual al TXT

    # Leer los datos del archivo txt
    variable = funcion_leer(txt_path)
    tiempo = np.arange(len(variable))

    # Escribir los datos en un archivo CSV
    with open(csv_path, mode="w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        
        # Escribir el encabezado
        escritor_csv.writerow(["tiempo", "variable"])
        
        # Escribir los datos de tiempo y señal en columnas
        for t, s in zip(tiempo, variable):
            escritor_csv.writerow([t, s])

    print(f"Convertido: {txt_name}.txt -> {txt_name}.csv")

print("Todos los archivos han sido convertidos exitosamente.")
