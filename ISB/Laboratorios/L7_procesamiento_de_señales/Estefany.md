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
