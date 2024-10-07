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
   


### EMG en Reposo

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica en el Dominio del Tiempo**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/raw.png) |
| **Gráfica en el Dominio de la Frecuencia (Señal Raw)**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/ft_raw.png) |
| **Gráfica en el Dominio de la Frecuencia (Filtrada)** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/ft_filter.png) |
| **Comparación de Señales**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/comparison.png)                 |

| **Transformada Corta de Fourier de la Señal Filtrada** |
|-------------------------------------------------------|
| ![Transformada Corta de Fourier](https://github.com/Peeta18/ISB_Grupo3/blob/4858cfdc0d364deac5a4542dee6d533fae0321e8/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/FTSC.png) |
| **Descripción:** La transformada revela que las componentes de alta frecuencia (por encima de 150 Hz) se han reducido, indicando que el filtro aplicado ha logrado mitigar ruido de alta frecuencia. La mayor densidad de energía se concentra en las bandas por debajo de 100 Hz, lo que sugiere que las características principales de la señal se han preservado. |

| Título | Imagen | Descripción |
|--------|--------|-------------|
| **Diagrama de Bode del Filtro IIR** | ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/ba3c8922fa47ad62734755753370f7176e1575bd/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/bode.png) | Se observa una respuesta en magnitud que muestra ganancia nula a frecuencias bajas (<10 Hz), mientras que la fase se vuelve negativa en el rango de transición. La respuesta se estabiliza a frecuencias mayores, lo que confirma su efectividad para eliminar las componentes de baja frecuencia. |
| **Diagrama de Polos y Ceros del Filtro IIR** | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/4acf6339e67c70a71f6b6a7b2c42868fbe10be68/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/ceros.png) | El diagrama muestra polos distribuidos cerca del eje real, indicando que el filtro IIR tiene una fuerte atenuación fuera de su banda de paso. Los ceros, ubicados simétricamente, aseguran que se eliminen componentes específicas no deseadas |

#### **Justificación de los Filtros:**
   - **Filtro Pasa-Bajo (Butterworth)**: Se aplicó para atenuar el ruido de alta frecuencia en la señal de reposo. Dado que no se esperaban movimientos significativos en la señal, el filtro pasa-bajo mantuvo la señal sin distorsión.
   - **Filtro Notch**: Utilizado para eliminar la frecuencia de línea de 50/60 Hz. Como el equipo puede introducir esta interferencia en estado de reposo, se optó por eliminarla.
   - **Filtro Pasa-Alto (FIR)**: Aplicado para suprimir cualquier componente de baja frecuencia que pudiera alterar el análisis.

---
