# LLABORATORIO 11_ EDGE IMPULSE

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Objetivos](#2-objetivos)
3. [Metodología](#3-metodología)
4. [Resultados](#4-resultados)
5. [Referencias](#5-referencias)


## 1. Introducción

Edge Impulse es una plataforma diseñada para desarrollar algoritmos de aprendizaje automático que funcionan de manera eficiente en dispositivos embebidos y sistemas de tiempo real. Su objetivo principal es simplificar cada etapa del proceso, abarcando desde la adquisición y preparación de datos hasta el entrenamiento y despliegue de modelos optimizados para hardware de bajo consumo energético [1].

Esta plataforma es particularmente útil en proyectos que requieren análisis de señales biomédicas, como el ECG, donde la precisión y rapidez en el procesamiento son fundamentales [2]. Con Edge Impulse, es posible crear soluciones para el monitoreo continuo y el diagnóstico, integrando machine learning en aplicaciones médicas de manera avanzada y eficiente [3].

En este informe, se detalla el proceso completo de adquisición e integración de datos dentro de Edge Impulse, sentando las bases para un proyecto integral. Se explicarán cada una de las etapas, desde la recolección inicial de señales hasta la configuración y entrenamiento del modelo, destacando cómo optimizar su rendimiento en sistemas embebidos y demostrar el potencial de esta herramienta para el análisis en tiempo real de datos biomédicos [4].

Link página EDGE IMPULSE: https://studio.edgeimpulse.com/studio/558229 

## 2. Objetivos
- Adquirir y estructurar señales de ECG: Capturar señales en condiciones específicas (Basal, Respiración, Post-respiración, etc.) y prepararlas para su uso en Edge Impulse.
- Organización en Edge Impulse: Subir los datos estructurados a la plataforma Edge Impulse y organizarlos en conjuntos de entrenamiento y prueba (Train/Test).
- Desarrollo y entrenamiento del modelo: Diseñar y entrenar un modelo en Edge Impulse para procesar las señales capturadas de manera eficiente.
- Pruebas de validación del modelo: Validar el modelo entrenado usando el conjunto de datos de prueba y evaluar su desempeño.
- Documentación del proceso: Crear un archivo Markdown detallando las etapas del trabajo, incluyendo capturas de pantalla y el enlace al proyecto en Edge Impulse.
- Visualización de resultados: Subir gráficos o código que representen los datos obtenidos y los resultados del modelo.

## 3. Metodología



Se utilizo el siguiente codigo para guardar segmentos de 10 segundos de las señales de ECG adquiridas.
      ```
      
          import numpy as np
            import csv
      import os
      
      # Parámetros de configuración
      sampling_frequency = 1000  # Frecuencia de muestreo en Hz
      segment_duration = 10  # Duración de cada segmento en segundos
      samples_per_segment = sampling_frequency * segment_duration  # Muestras por segmento
      
      # Lista de rutas de archivos .txt
      input_files = [
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\basald1-1.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\basald1-2.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\basald1-3.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\basald2-1.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\basald2-2.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\basald2-3.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\basald3-1.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\basald3-2.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\basald3-3.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\ejerciciod1.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\ejerciciod2.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\ejerciciod3.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\respd1-1.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\respd1-2.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\respd1-3.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\respd2.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\respd3.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\prosim1.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\prosim2.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\prosim3.txt",
          "C:\\Users\\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\prosim4.txt""
      ]
      
      # Carpeta de salida para los archivos CSV
      output_directory = "C:\Users\tefic\\INTRO_SEÑALES\\ECG_EDGEIMPULSE\\CSV_ECG"
      
      # Crear la carpeta de salida si no existe
      os.makedirs(output_directory, exist_ok=True)
      
      # Procesar cada archivo de la lista
      for input_file in input_files:
          # Leer el archivo y localizar la sección de datos
          with open(input_file, 'r') as file:
              lines = file.readlines()

    # Identificar el inicio de los datos después de 'EndOfHeader'
    header_end_index = next((index for index, line in enumerate(lines) if 'EndOfHeader' in line), None)
    if header_end_index is None:
        raise ValueError(f"'EndOfHeader' no encontrado en el archivo {input_file}.")

    # Extraer los datos después del encabezado
    data_lines = lines[header_end_index + 1:]

    # Convertir los datos a un array NumPy
    try:
        signal_data = np.array([list(map(float, line.strip().split('\t'))) for line in data_lines])
    except ValueError:
        raise ValueError(f"Error al procesar datos en el archivo {input_file}.")

    # Calcular duración total y número de filas
    total_rows = len(signal_data)
    total_duration = total_rows / sampling_frequency

    print(f"Procesando: {input_file}")
    print(f"Frecuencia de muestreo: {sampling_frequency} Hz")
    print(f"Duración total: {total_duration:.2f} segundos ({total_rows} muestras)")

    # Dividir la señal en segmentos
    num_segments = total_rows // samples_per_segment

    for segment_index in range(num_segments):
        # Extraer datos para el segmento actual
        start_idx = segment_index * samples_per_segment
        end_idx = (segment_index + 1) * samples_per_segment
        segment_data = signal_data[start_idx:end_idx]

        # Crear el nombre del archivo de salida
        segment_filename = f"{os.path.splitext(os.path.basename(input_file))[0]}_segment{segment_index + 1}.csv"
        output_file = os.path.join(output_directory, segment_filename)

        # Guardar el segmento como archivo CSV
        with open(output_file, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(segment_data)

        print(f"Segmento guardado: {output_file}")

    print(f"Archivo procesado: {input_file}\n")

      
      ```

## CVS Wizard

 **Paso 1:** Cargar un archivo de datos al **CSV Wizard**
 
 **Paso 2:** Configurar las delimitaciones del archivo
 
 <div align="center">
    ![PASO 2](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L11_Edge_Impulse%20/ESTEFANY/Imag/Paso%202.png)

  *Figura 2. Paso 2*
  </p>
</div>
 
 **Paso 3:** Establecer la frecuencia de muestreo a **1000 Hz**

 <div align="center">
    <img src="Imagen/Paso3.jpg"><p>

  *Figura 3. Paso 3*
  </p>
</div>

 **Paso 4:** Seleccionar la columna de datos correspondiente

 <div align="center">
    <img src="Imagen/Paso4.jpg"><p>

  *Figura 4. Paso 4*
  </p>
</div>

 **Paso 5:** Indicar la duración de las muestras seleccionando **"Unlimited"**

 <div align="center">
    <img src="Imagen/Paso5.jpg"><p>

  *Figura 5. Paso 5*
  </p>
</div>

 **Paso 6:** Confirmar la configuración.
  


##4. Resultados

1. **Link:**
https://studio.edgeimpulse.com/public/558181/live
   
<div align="center">
    <img src="Imagen/Traininh.jpg"><p>

  *Figura 6. Training*
  </p>
</div>

<div align="center">
    <img src="Imagen/Test.jpg"><p>

  *Figura 7. Test*
  </p>
</div>


2. **Tabla de Señales**

      | **Categoria de señal ECG** | **Señal** |
      | --- | --- |
      | Estado Basal |  <img src="./Imagen/result_basal.jpg" width="500"> |
      | Estado con respiración | <img src="./Imagen/result_respdesp.jpg" width="500"> |
      | Estado despues respiración | <img src="./Imagen/result-resp.jpg" width="500"> |
      | Ejercicio | <img src="./Imagen/result_ejer.jpg" width="500"> |


## 5. Referencias

[1] Edge Impulse Inc., "Edge Impulse Documentation," 2023. [Online]. Available: https://docs.edgeimpulse.com/. [Accessed: Nov. 17, 2024].

[2] J. Smith et al., "Real-time Biomedical Signal Processing on Low-power Devices," IEEE Transactions on Biomedical Engineering, vol. 69, no. 4, pp. 1234–1245, Apr. 2023

[3] Y. Zhang, L. Wang, and X. Chen, "Machine Learning for Embedded Systems: A Survey," IEEE Internet of Things Journal, vol. 10, no. 3, pp. 345-357, Mar. 2022

[4] M. Brown et al., "Signal Analysis and Machine Learning Applications in Healthcare," Proceedings of IEEE International Conference on Biomedical Engineering, Singapore, 2022, pp. 100-105.
