# Filtrado de Señales EMG y ECG

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

#### Gráficas de la Señal

| Dominio del Tiempo | Dominio de la Frecuencia (Raw) | Dominio de la Frecuencia (Filtrada) | Comparación de Señales |
|--------------------|---------------------------------|-------------------------------------|------------------------|
| ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/raw.png) | ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/ft_raw.png) | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/ft_filter.png) | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/comparison.png) |

#### Análisis del Filtro

| Diagrama de Bode | Diagrama de Polos y Ceros |
|------------------|---------------------------|
| ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/ba3c8922fa47ad62734755753370f7176e1575bd/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/bode.png) | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/4acf6339e67c70a71f6b6a7b2c42868fbe10be68/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/ceros.png) |

#### Justificación de los Filtros
Se emplearon un filtro pasa-bajo Butterworth para reducir el ruido de alta frecuencia, un filtro Notch para eliminar la interferencia de la frecuencia de línea eléctrica de 50/60 Hz, y un filtro pasa-alto FIR para suprimir componentes de baja frecuencia que podrían distorsionar el análisis, asegurando así una señal limpia y precisa para el estudio de la actividad muscular en reposo.

---

### EMG Movimiento Voluntario

#### Gráficas de la Señal

| Dominio del Tiempo | Dominio de la Frecuencia (Raw) | Dominio de la Frecuencia (Filtrada) | Comparación de Señales |
|--------------------|---------------------------------|-------------------------------------|------------------------|
| ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/raw.png) | ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/freq.png) | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/freq-filter.png) | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/comparacion.png) |

#### Análisis del Filtro

| Diagrama de Bode | Diagrama de Polos y Ceros |
|------------------|---------------------------|
| ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/7bec849c48436463974002153f90f98ecf6ab26a/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/bode.png) | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/7bec849c48436463974002153f90f98ecf6ab26a/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/diagrama.png) |

#### Justificación de los Filtros
Para el análisis del movimiento voluntario, se seleccionaron un filtro FIR pasa-alto de 30 Hz que elimina las componentes de baja frecuencia y el ruido DC, un filtro Notch de 50 Hz para suprimir las interferencias eléctricas, y un filtro pasa-bajo de 150 Hz que elimina las frecuencias altas no relevantes, permitiendo así una representación clara y precisa de la actividad muscular durante el movimiento voluntario.

---

### EMG Movimiento Forzado

#### Gráficas de la Señal

| Dominio del Tiempo | Dominio de la Frecuencia (Raw) | Dominio de la Frecuencia (Filtrada) | Comparación de Señales |
|--------------------|---------------------------------|-------------------------------------|------------------------|
| ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/raw.png) | ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/ft.png) | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/ft-filter.png) | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/comparison.png) |

#### Análisis del Filtro

| Diagrama de Bode | Diagrama de Polos y Ceros |
|------------------|---------------------------|
| ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/ba3c8922fa47ad62734755753370f7176e1575bd/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/bode.png) | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/4acf6339e67c70a71f6b6a7b2c42868fbe10be68/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/forzado/ceros.png) |

#### Justificación de los Filtros
En el caso del movimiento forzado, se implementaron un filtro FIR pasa-alto de 30 Hz para eliminar las bajas frecuencias y el ruido de fondo, un filtro IIR pasa-bajo de 150 Hz para atenuar las altas frecuencias que no aportan información relevante, y un filtro IIR pasa-banda de 30-150 Hz que ajusta la señal al rango típico de frecuencias de EMG, asegurando así una representación fiel y sin interferencias de la actividad muscular durante el movimiento forzado.

---

## Análisis de Señales ECG

### ECG Estado Basal

#### Gráficas de la Señal

| Dominio del Tiempo | Dominio de la Frecuencia (Raw) | Dominio de la Frecuencia (Filtrada) | Comparación de Señales |
|--------------------|---------------------------------|-------------------------------------|------------------------|
| ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/raw.png) | ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/ft.png) | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/ft-filter.png) | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/comparison.png) |

#### Análisis del Filtro

| Diagrama de Bode | Diagrama de Polos y Ceros |
|------------------|---------------------------|
| ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/bode.png) | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/basal/ceros.png) |

#### Justificación de los Filtros
Para el análisis del estado basal del ECG, se utilizaron filtros pasa-alto FIR de 0.5 Hz para eliminar las fluctuaciones de la línea base, filtros pasa-bajo FIR de 40 Hz que atenúan las altas frecuencias manteniendo las principales características del ECG, y filtros FIR en general debido a su estabilidad y respuesta lineal en fase, lo cual es esencial para preservar la integridad de las formas de onda del ECG.

---

### ECG Luego de Respiración

#### Gráficas de la Señal

| Dominio del Tiempo | Dominio de la Frecuencia (Raw) | Dominio de la Frecuencia (Filtrada) | Comparación de Señales |
|--------------------|---------------------------------|-------------------------------------|------------------------|
| ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/respir/raw.png) | ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/respir/ft.png) | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/respir/ft-filter.png) | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/respir/comparison.png) |

#### Análisis del Filtro

| Diagrama de Bode | Diagrama de Polos y Ceros |
|------------------|---------------------------|
| ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/respir/bode.png) | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/respir/ceros.png) |

#### Justificación de los Filtros
Al analizar el ECG luego de la respiración, se optó por un filtro pasa-bajo Butterworth para disminuir el ruido de alta frecuencia, un filtro Notch para eliminar la interferencia de la frecuencia de línea eléctrica de 50/60 Hz, y un filtro pasa-alto FIR para eliminar cualquier componente de baja frecuencia que pudiera distorsionar el análisis, garantizando así una señal limpia y adecuada para evaluar los efectos de la respiración en la actividad cardíaca.

---

### ECG Luego de Ejercicio

#### Gráficas de la Señal

| Dominio del Tiempo | Dominio de la Frecuencia (Raw) | Dominio de la Frecuencia (Filtrada) | Comparación de Señales |
|--------------------|---------------------------------|-------------------------------------|------------------------|
| ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/ejerc/raw.png) | ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/ejerc/ft.png) | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/ejerc/ft-filter.png) | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/ejerc/comparison.png) |

#### Análisis del Filtro

| Diagrama de Bode | Diagrama de Polos y Ceros |
|------------------|---------------------------|
| ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/ejerc/bode.png) | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/50916b5b13ef5b6e6cd05f640026ca95d59b2cb4/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/ECG/ejerc/ceros.png) |

#### Justificación de los Filtros
En el análisis del ECG luego de ejercicio, se implementaron filtros pasa-alto FIR para eliminar las fluctuaciones de la línea base a frecuencias muy bajas, filtros pasa-bajo FIR para conservar las características esenciales del ECG mientras se atenúa el ruido de alta frecuencia, y un filtro Notch IIR para eliminar eficazmente el ruido de 50 Hz cuando era necesario, asegurando así una señal de alta calidad para evaluar los efectos del ejercicio en la actividad cardíaca.

---

## Bibliografía
1. Lian, J., & Wang, Z. (2023). Stages-Based ECG Signal Analysis From Traditional Signal Processing to Machine Learning. IEEE Transactions on Biomedical Engineering, 70(1), 12-22.
2. Moreira, D., Fonseca, J., & Lourenço, A. (2020). Characterization and Differentiation of Electromyographic Signals Acquired Using the BITalino Platform. IEEE Access, 8, 102981-102993.
3. Acharya, U. R., Faust, O., & Suri, J. S. (2021). Biomedical Signal Processing: An ECG Application. En Advances in Cardiac Signal Processing (pp. 117-142). Springer.
4. Rodríguez, I., Parra, C., & González, E. (2019). Experience of Use of the BITalino Kit for Biomedical Signals Recording. IEEE Latin America Transactions, 17(12), 2022-2030.

