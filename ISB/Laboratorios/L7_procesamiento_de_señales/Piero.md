# Análisis de Señales EMG y ECG

Este repositorio contiene el análisis de tres señales EMG y tres señales ECG, que han sido procesadas y filtradas para su comparación en el dominio del tiempo y de la frecuencia. A continuación se presentan los gráficos, el análisis de los filtros aplicados y la justificación de su uso para cada señal.

## Tabla de Contenidos
- [Análisis de Señales EMG](#análisis-de-señales-emg)
  - [EMG en Reposo](#emg-en-reposo)
  - [EMG Movimiento Voluntario](#emg-movimiento-voluntario)
  - [EMG Movimiento Forzado](#emg-movimiento-forzado)
- [Análisis de Señales ECG](#análisis-de-señales-ecg)
  - [ECG Estado Basal](#ecg-estado-basal)
  - [ECG Luego de Respiración](#ecg-luego-de-respiración)
  - [ECG Luego de Ejercicio](#ecg-luego-de-ejercicio)

---

## Análisis de Señales EMG

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

### EMG Movimiento Voluntario

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica en el Dominio del Tiempo**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/raw.png) |
| **Gráfica en el Dominio de la Frecuencia (Señal Raw)**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/freq.png) |
| **Gráfica en el Dominio de la Frecuencia (Filtrada)** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/freq-filter.png) |
| **Comparación de Señales**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/comparacion.png)                 |

| **Transformada Corta de Fourier de la Señal Filtrada** |
|-------------------------------------------------------|
| ![Transformada Corta de Fourier](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/FTSC.png) |
| **Descripción:** La transformada revela que la energía se concentra principalmente en torno a los 50 Hz, reflejando una frecuencia dominante en la señal. Además, se nota una disminución significativa en las frecuencias por encima de los 100 Hz, lo que sugiere que el filtro aplicado eliminó efectivamente las componentes de alta frecuencia no deseadas. |

| Título | Imagen | Descripción |
|--------|--------|-------------|
| **Diagrama de Bode del Filtro IIR** | ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/7bec849c48436463974002153f90f98ecf6ab26a/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/bode.png) | Podemos observar cómo la magnitud se atenúa para frecuencias por debajo de la banda de paso, mientras que la fase cambia de manera abrupta alrededor de la frecuencia de corte. Esto indica que el filtro es efectivo para suprimir frecuencias fuera del rango deseado. |
| **Diagrama de Polos y Ceros del Filtro IIR** | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/7bec849c48436463974002153f90f98ecf6ab26a/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/diagrama.png) | Los polos se encuentran distribuidos dentro del círculo unitario, asegurando estabilidad, y los ceros se posicionan de manera que suprimen las frecuencias no deseadas. Esta configuración sugiere que el filtro diseñado tiene una respuesta adecuada para eliminar componentes específicas de la señal. |

#### **Justificación de los Filtros:**
- **Justificación del Filtro Pasa-Alto (30 Hz)**: El filtro pasa-alto con frecuencia de corte de 30 Hz fue utilizado para eliminar las componentes de baja frecuencia y el ruido DC presentes en la señal. 
- **Justificación del Filtro Notch (50 Hz)**: El filtro Notch en 50 Hz se aplicó para suprimir la interferencia de la frecuencia de línea eléctrica, que puede contaminar la señal. 
- **Justificación del Filtro Pasa-Bajo (150 Hz)**: El filtro pasa-bajo se utilizó para eliminar las componentes de alta frecuencia (>150 Hz) que no contienen información relevante para la actividad muscular.

---

### EMG Movimiento Forzado

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica en el Dominio del Tiempo**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/raw.png) |
| **Gráfica en el Dominio de la Frecuencia (Señal Raw)**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/ft.png) |
| **Gráfica en el Dominio de la Frecuencia (Filtrada)** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/ft-filter.png) |
| **Comparación de Señales**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/comparison.png)                 |

| **Transformada Corta de Fourier de la Señal Filtrada** |
|-------------------------------------------------------|
| ![Transformada Corta de Fourier](https://github.com/Peeta18/ISB_Grupo3/blob/e59ccaa802254dee79663aca656c7e91cb51d4f4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/spectogram.png) |
| **Descripción:** El espectrograma revela cómo la energía de la señal se distribuye a lo largo del tiempo en diferentes bandas de frecuencia. Se observa una concentración significativa de energía entre 50 y 100 Hz. La variabilidad temporal en las intensidades sugiere cambios en la actividad de la señal durante el tiempo de adquisición. |

| Título | Imagen | Descripción |
|--------|--------|-------------|
| **Diagrama de Bode del Filtro IIR** | ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/ba3c8922fa47ad62734755753370f7176e1575bd/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/bode.png) | La magnitud presenta una respuesta plana en el rango de la banda de paso (alrededor de 100 a 300 Hz) y una fuerte atenuación fuera de este rango. La fase cambia de manera no lineal en las frecuencias de transición, indicando la selectividad del filtro y cómo afecta la señal en dichas frecuencias. |
| **Diagrama de Polos y Ceros del Filtro IIR** | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/4acf6339e67c70a71f6b6a7b2c42868fbe10be68/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/ceros.png) | Los ceros y polos se distribuyen de manera que forman la banda de paso deseada y suprimen las frecuencias no deseadas. Los polos ubicados cerca del eje real aseguran estabilidad, mientras que la posición de los ceros ayuda a eliminar componentes específicas de la señal. |

#### **Justificación de los Filtros:**
- **Filtro FIR Pasa-Alto (30 Hz)**: Seleccionado para eliminar componentes de baja frecuencia, incluyendo el ruido de base y el componente DC. 
- **Filtro IIR Pasa-Bajo (150 Hz)**:Elimina componentes de alta frecuencia, manteniendo la energía de la señal entre el rango de interés. 
- **Filtro IIR Pasa-Banda (30-150 Hz)**: Ajusta la señal al rango típico de frecuencias de EMG, manteniendo la información relevante y eliminando residuos.

---

## Análisis de Señales ECG

### ECG Estado Basal

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica en el Dominio del Tiempo**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/raw.png) |
| **Gráfica en el Dominio de la Frecuencia (Señal Raw)**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/ft.png) |
| **Gráfica en el Dominio de la Frecuencia (Filtrada)** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/ft-filter.png) |
| **Comparación de Señales**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/comparison.png)                 |

| **Transformada Corta de Fourier de la Señal Filtrada** |
|-------------------------------------------------------|
| ![Transformada Corta de Fourier](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/spectro.png) |
| **Descripción:** La transformada revela que las componentes de alta frecuencia (por encima de 150 Hz) se han reducido, indicando que el filtro aplicado ha logrado mitigar ruido de alta frecuencia. La mayor densidad de energía se concentra en las bandas por debajo de 100 Hz, lo que sugiere que las características principales de la señal se han preservado. |

| Título | Imagen | Descripción |
|--------|--------|-------------|
| **Diagrama de Bode del Filtro IIR** | ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/bode.png) | El gráfico de magnitud presenta una rápida atenuación fuera de la banda de paso y un comportamiento oscilatorio, reflejando un diseño de filtro con alta selectividad. La fase varía linealmente dentro de la banda de paso, manteniendo la coherencia de fase. |
| **Diagrama de Polos y Ceros del Filtro IIR** | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/ceros.png) | Los polos están distribuidos en el círculo unitario, y los ceros están posicionados estratégicamente para cancelar frecuencias no deseadas, mostrando que el filtro FIR es selectivo y de alta estabilidad. |

#### **Justificación de los Filtros:**
   - **Filtro Pasa-Alto FIR (0.5 Hz)**: Elimina la fluctuación de línea base (cambios lentos), mejorando la claridad del ECG.
   - **Filtro Pasa-Bajo FIR (40 Hz)**: Atenúa componentes de alta frecuencia, manteniendo solo las frecuencias de interés en el ECG.
   - **Filtros FIR**: Seleccionados por su estabilidad y respuesta lineal en fase, lo cual es crucial en señales ECG para conservar la forma de onda.

---

### ECG Luego de Respiración

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica en el Dominio del Tiempo**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/respir/raw.png) |
| **Gráfica en el Dominio de la Frecuencia (Señal Raw)**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/respir/ft.png) |
| **Gráfica en el Dominio de la Frecuencia (Filtrada)** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/respir/ft-filter.png) |
| **Comparación de Señales**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/respir/comparison.png)                 |

| Título | Imagen | Descripción |
|--------|--------|-------------|
| **Diagrama de Bode del Filtro IIR** | ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/respir/bode.png) | El gráfico de magnitud presenta una rápida atenuación fuera de la banda de paso y un comportamiento oscilatorio, reflejando un diseño de filtro con alta selectividad. La fase varía linealmente dentro de la banda de paso, manteniendo la coherencia de fase. |
| **Diagrama de Polos y Ceros del Filtro IIR** | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/respir/ceros.png) | Los polos están distribuidos en el círculo unitario, y los ceros están posicionados estratégicamente para cancelar frecuencias no deseadas, mostrando que el filtro FIR es selectivo y de alta estabilidad. |

#### **Justificación de los Filtros:**
   - **Filtro Pasa-Bajo (Butterworth)**: Se aplicó para atenuar el ruido de alta frecuencia en la señal de reposo. Dado que no se esperaban movimientos significativos en la señal, el filtro pasa-bajo mantuvo la señal sin distorsión.
   - **Filtro Notch**: Utilizado para eliminar la frecuencia de línea de 50/60 Hz. Como el equipo puede introducir esta interferencia en estado de reposo, se optó por eliminarla.
   - **Filtro Pasa-Alto (FIR)**: Aplicado para suprimir cualquier componente de baja frecuencia que pudiera alterar el análisis.

---

### ECG Luego de Ejercicio

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica en el Dominio del Tiempo**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/ejerc/raw.png) |
| **Gráfica en el Dominio de la Frecuencia (Señal Raw)**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/ejerc/ft.png) |
| **Gráfica en el Dominio de la Frecuencia (Filtrada)** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/ejerc/ft-filter.png) |
| **Comparación de Señales**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/ejerc/comparison.png)                 |

| Título | Imagen | Descripción |
|--------|--------|-------------|
| **Diagrama de Bode del Filtro IIR** | ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/ejerc/bode.png) | El gráfico de magnitud presenta una rápida atenuación fuera de la banda de paso y un comportamiento oscilatorio, reflejando un diseño de filtro con alta selectividad. La fase varía linealmente dentro de la banda de paso, manteniendo la coherencia de fase. |
| **Diagrama de Polos y Ceros del Filtro IIR** | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/ejerc/ceros.png) | Los polos están distribuidos en el círculo unitario, y los ceros están posicionados estratégicamente para cancelar frecuencias no deseadas, mostrando que el filtro FIR es selectivo y de alta estabilidad. |

#### **Justificación de los Filtros:**
   - **Filtro Pasa-Alto FIR**: Elimina fluctuaciones de línea base a frecuencias muy bajas.
   - **Filtro Pasa-Bajo FIR**: Retiene las características principales de la señal ECG eliminando ruido de alta frecuencia.
   - **Filtro Notch IIR**: Elimina el ruido de 50 Hz, si es necesario.
  
---

### Bibliografía
1. Lian, J., & Wang, Z. (2023). Stages-Based ECG Signal Analysis From Traditional Signal Processing to Machine Learning. IEEE Transactions on Biomedical Engineering, 70(1), 12-22.
2. Moreira, D., Fonseca, J., & Lourenço, A. (2020). Characterization and Differentiation of Electromyographic Signals Acquired Using the BITalino Platform. IEEE Access, 8, 102981-102993.
3. Acharya, U. R., Faust, O., & Suri, J. S. (2021). Biomedical Signal Processing: An ECG Application. En Advances in Cardiac Signal Processing (pp. 117-142). Springer.
4. Rodríguez, I., Parra, C., & González, E. (2019). Experience of Use of the BITalino Kit for Biomedical Signals Recording. IEEE Latin America Transactions, 17(12), 2022-2030.
