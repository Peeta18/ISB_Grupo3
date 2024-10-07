# Análisis de Señales EMG y ECG

## Tabla de Contenidos
1. [Introducción](#introducción)
   - [Filtros](#filtros)
   - [Filtros Analógicos y Digitales](#filtros-analógicos-y-digitales)
   - [Filtros FIR e IIR](#filtros-fir-e-iir)
     - [Subtipos de Filtros FIR](#subtipos-de-filtros-fir)
     - [Subtipos de Filtros IIR](#subtipos-de-filtros-iir)
2. [Objetivos del Laboratorio](#objetivos-del-laboratorio)
3. [Análisis de Señales EMG](#análisis-de-señales-emg)
   - [EMG en Reposo](#emg-en-reposo)
   - [EMG Movimiento Voluntario](#emg-movimiento-voluntario)
   - [EMG Movimiento Forzado](#emg-movimiento-forzado)
4. [Análisis de Señales ECG](#análisis-de-señales-ecg)
   - [ECG Estado Basal](#ecg-estado-basal)
   - [ECG Luego de Respiración](#ecg-luego-de-respiración)
   - [ECG Luego de Ejercicio](#ecg-luego-de-ejercicio)
5. [Bibliografía](#bibliografía)

---

## Introducción

### Filtros

Un **filtro** es un sistema que permite modificar una señal de entrada para obtener una señal de salida con ciertas características específicas, como la eliminación de ruido o la extracción de componentes de frecuencia particular [1]. Los filtros son fundamentales en el procesamiento de señales, ya que facilitan la mejora y la interpretación de las señales adquiridas de diversas fuentes, como sensores biomédicos, sistemas de comunicación y equipos de audio.

### Filtros Analógicos y Digitales

Los filtros se clasifican principalmente en **analógicos** y **digitales**. Los **filtros analógicos** operan sobre señales continuas en el tiempo y se implementan mediante componentes electrónicos como resistencias, capacitores e inductores. Son ampliamente utilizados en aplicaciones en tiempo real, como en sistemas de radio y audio, donde la respuesta rápida es esencial [2].

Por otro lado, los **filtros digitales** procesan señales discretas en el tiempo y se implementan mediante algoritmos matemáticos en sistemas digitales, como microcontroladores o procesadores de señales digitales (DSP). Los filtros digitales ofrecen mayor flexibilidad y precisión, ya que sus parámetros pueden ser fácilmente ajustados y optimizados para diferentes aplicaciones sin necesidad de modificar el hardware [3].

### Filtros FIR e IIR

Dentro de los filtros digitales, existen dos categorías principales: **FIR (Finite Impulse Response)** e **IIR (Infinite Impulse Response)**. Cada tipo tiene características y aplicaciones específicas que los hacen adecuados para diferentes escenarios de procesamiento de señales [4].

#### Subtipos de Filtros FIR

Los **filtros FIR** tienen una respuesta al impulso finita, lo que significa que su salida depende de un número limitado de muestras de la señal de entrada. Son conocidos por su **estabilidad inherente** y **fase lineal**, lo que los hace ideales para aplicaciones donde la distorsión de fase es crítica, como en el procesamiento de audio y señales biomédicas [5].

| Subtipos de Filtros FIR | Descripción                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Ventana Rectangular** | Ventana simple y eficiente, pero con altos niveles de "rizado" en la respuesta. |
| **Ventana de Hamming**  | Reduce el "rizado", mejorando la atenuación en las bandas no deseadas.       |
| **Ventana de Hanning**  | Ventana suave que minimiza las discontinuidades en los bordes de la señal.    |
| **Ventana de Blackman** | Proporciona una mejor atenuación de las bandas laterales, reduciendo el "rizado". |
| **Ventana de Kaiser**   | Ventana ajustable que permite controlar el ancho de banda y el nivel de atenuación. |

#### Subtipos de Filtros IIR

Los **filtros IIR** poseen una respuesta al impulso infinita, lo que significa que su salida depende tanto de las muestras actuales y pasadas de la señal de entrada como de las muestras pasadas de la señal de salida. Estos filtros son más eficientes que los FIR en términos de número de coeficientes necesarios para alcanzar una especificación de diseño determinada, pero pueden ser **inestables** y no ofrecen una **fase lineal** [6].

| Subtipos de Filtros IIR | Descripción                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Filtro Butterworth**   | Filtro con una respuesta en frecuencia lo más plana posible en la banda de paso. |
| **Filtro Chebyshev I**   | Presenta un "rizado" en la banda de paso para obtener una transición más rápida. |
| **Filtro Chebyshev II**  | Tiene "rizado" en la banda de rechazo en lugar de la banda de paso.         |
| **Filtro Elíptico**      | Ofrece la transición más rápida entre la banda de paso y de rechazo, con "rizado" en ambas bandas. |
| **Filtro Bessel**        | Optimiza la respuesta de fase, proporcionando una transición suave en frecuencia. |

## Objetivos del Laboratorio

El objetivo principal de este laboratorio es aplicar filtros digitales sobre señales electromiográficas (EMG) y electrocardiográficas (ECG) obtenidas en sesiones anteriores para eliminar componentes de ruido y mejorar la calidad de las señales. Se busca analizar el efecto de diferentes tipos de filtros (FIR e IIR) en las señales de entrada, evaluando su desempeño tanto en el dominio del tiempo como en el dominio de la frecuencia. A través de este proceso, se pretende comprender mejor la aplicación de técnicas de filtrado y las diferencias en los resultados obtenidos entre los diferentes filtros seleccionados.

---

## Análisis de Señales EMG

### EMG en Reposo

#### Gráficas de la Señal

| Dominio del Tiempo | Dominio de la Frecuencia (Raw) | Dominio de la Frecuencia (Filtrada) | Comparación de Señales |
|--------------------|---------------------------------|-------------------------------------|------------------------|
| ![Dominio del Tiempo]([Imagenes_Italo/EMG/Reposo/1.jpg)) | ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/ft_raw.png) | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/ft_filter.png) | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/EEG/reposo/comparison.png) |

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
| ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Reposo/1.jpg) | ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/freq.png) | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/freq-filter.png) | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/comparacion.png) |

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
[1]. J. G. Proakis and D. G. Manolakis, *Digital Signal Processing: Principles, Algorithms and Applications*, 4th ed., Pearson, 2010.

[2]. A. V. Oppenheim and R. W. Schafer, *Discrete-Time Signal Processing*, 3rd ed., Pearson, 2009.

[3]. S. Karris, *The Scientist and Engineer's Guide to Digital Signal Processing*, California Technical Publishing, 1997.

[4]. A. V. Oppenheim, *Signals and Systems*, 2nd ed., Prentice Hall, 1996.

[5]. P. P. Vaidyanathan, *Multirate Systems and Filter Banks*, Prentice Hall, 1993.

[6]. R. W. Schafer and A. V. Oppenheim, *Discrete-Time Signal Processing*, 3rd ed., Pearson, 2007.
