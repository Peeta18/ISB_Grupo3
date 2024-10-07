Elaboración individual - Etefany Valverde Salinas 

# Análisis de Señales EMG y ECG

<div align="justify">

Este documento presenta un análisis detallado de señales electromiográficas (EMG) y electrocardiográficas (ECG) seleccionadas de laboratorios anteriores. Cada señal ha sido elegida para representar diversas actividades y ha sido procesada mediante filtros de respuesta impulsiva finita (FIR) o infinita (IIR) para su análisis en los dominios del tiempo y de la frecuencia. En este archivo, se incluyen gráficas comparativas de las señales originales y filtradas, análisis en el dominio de la frecuencia. Adicionalmente, se ofrece un estudio de los filtros aplicados, ilustrando cada uno mediante diagramas de polos y ceros, así como diagramas de Bode que detallan la magnitud y la fase. Finalizamos con una justificación de la elección de estos filtros, destacando su relevancia y eficacia en el tratamiento de las señales EMG y ECG para los objetivos de este estudio.

</div>


## Tabla de Contenidos
- [Análisis de Señales EMG](#análisis-de-señales-emg)
  - [EMG en Reposo](#emg-en-reposo)
      - Gráfica en el dominio del tiempo
      - Gráfica en el dominio de la frecuencia
      - Análisis de Filtros
      - Justificación de filtro
  - [EMG Movimiento Voluntario](#emg-movimiento-voluntario)
      - Gráfica en el dominio del tiempo
      - Gráfica en el dominio de la frecuencia
      - Análisis de Filtros
      - Justificación de filtro
  - [EMG Movimiento Forzado](#emg-movimiento-forzado)
      - Gráfica en el dominio del tiempo
      - Gráfica en el dominio de la frecuencia
      - Análisis de Filtros
      - Justificación de filtro
- [Análisis de Señales ECG](#análisis-de-señales-ecg)
  - [ECG Estado Basal](#ecg-estado-basal)
      - Gráfica en el dominio del tiempo
      - Gráfica en el dominio de la frecuencia
      - Análisis de Filtros
      - Justificación de filtro
  - [ECG Luego de Respiración](#ecg-luego-de-respiración)
      - Gráfica en el dominio del tiempo
      - Gráfica en el dominio de la frecuencia
      - Análisis de Filtros
      - Justificación de filtro
  - [ECG Luego de Ejercicio](#ecg-luego-de-ejercicio)
      - Gráfica en el dominio del tiempo
      - Gráfica en el dominio de la frecuencia
      - Análisis de Filtros
      - Justificación de filtro
   


### EMG en REPOSO

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica respuesta de frecuencia filtro pasa alta**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/respuesta%20de%20frecuencai%20filtro%20pasa%20alto.png) |
| **Gráfica de señal original y filtrada**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/se%C3%B1ale%20original%20y%20filtrada.png) |
| **Gráfica de análisis de frecuencia original y filtrada** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/analisis%20frecuencia%20origial%20y%20filtrada.png) |
| **Espectograma**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/espectograma.png)                 |
| **Diagrama de polos y ceros**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/diagrama%20polos%20y%20ceros.png)                 |
| **Diagrama de Bode**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/diagrama%20de%20bode.png)                 |

