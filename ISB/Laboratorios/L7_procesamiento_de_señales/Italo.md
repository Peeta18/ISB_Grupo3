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
| ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Reposo/1.jpg) | ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Reposo/2.jpg) | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Reposo/3.jpg) | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Reposo/4.jpg) |

#### Análisis del Filtro

| Diagrama de Bode | Diagrama de Polos y Ceros |
|------------------|---------------------------|
| ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Reposo/5.jpg) | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Reposo/6.jpg) |

#### Justificación de los Filtros
He elegido usar un filtro Butterworth bandpass de orden 4 con frecuencias de corte en 20 Hz y 450 Hz porque este filtro permite que pasen las frecuencias importantes para la señal EMG mientras elimina el ruido de frecuencias más bajas y más altas. El filtro Butterworth es ideal porque mantiene la forma de la señal sin distorsionarla, y con un orden de 4 logra una buena separación entre las frecuencias que queremos conservar y las que necesitamos eliminar. Esto resulta en una señal más limpia y precisa para analizar.

---

### EMG Movimiento Voluntario

#### Gráficas de la Señal

| Dominio del Tiempo | Dominio de la Frecuencia (Raw) | Dominio de la Frecuencia (Filtrada) | Comparación de Señales |
|--------------------|---------------------------------|-------------------------------------|------------------------|
| ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Voluntario/1.jpg) | ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Voluntario/2.jpg) | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Voluntario/3.jpg) | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Voluntario/4.jpg) |

#### Análisis del Filtro

| Diagrama de Bode | Diagrama de Polos y Ceros |
|------------------|---------------------------|
| ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Voluntario/5.jpg) | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Voluntario/6.jpg) |

#### Justificación de los Filtros
He seleccionado un filtro pasa altos FIR a 40 Hz y un filtro pasa bajos Butterworth a 140 Hz para procesar las señales EMG durante un movimiento voluntario. El filtro FIR pasa altos elimina las componentes de baja frecuencia que pueden incluir desplazamientos de DC y artefactos de movimiento, asegurando que solo las frecuencias relevantes de la actividad muscular sean consideradas. Por otro lado, el filtro Butterworth pasa bajos atenúa las frecuencias superiores a 140 Hz, eliminando ruido de alta frecuencia sin distorsionar significativamente la señal EMG gracias a su respuesta en frecuencia plana. Esta combinación de filtros permite obtener una señal EMG más limpia y precisa, facilitando un análisis más fiable de la actividad muscular durante el movimiento voluntario.

---

### EMG Movimiento Forzado

#### Gráficas de la Señal

| Dominio del Tiempo | Dominio de la Frecuencia (Raw) | Dominio de la Frecuencia (Filtrada) | Comparación de Señales |
|--------------------|---------------------------------|-------------------------------------|------------------------|
| ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Forzado/1.jpg) | ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Forzado/2.jpg) | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Forzado/3.jpg) | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Forzado/4.jpg) |

#### Análisis del Filtro

| Diagrama de Bode | Diagrama de Polos y Ceros |
|------------------|---------------------------|
| ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Forzado/5.jpg) | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/EMG/Forzado/6.jpg) |

#### Justificación de los Filtros
He seleccionado tres filtros distintos para procesar las señales EMG durante un movimiento forzado: un filtro FIR pasa bajos a 140 Hz para eliminar el ruido de alta frecuencia sin distorsionar la señal, un filtro IIR Butterworth pasa altos a 40 Hz para eliminar componentes de baja frecuencia como desplazamientos de DC y artefactos de movimiento, y un filtro IIR Butterworth pasa banda entre 40 Hz y 140 Hz para aislar únicamente las frecuencias relevantes de la señal EMG. Esta combinación permite obtener una señal EMG más limpia y precisa, facilitando un análisis más fiable de la actividad muscular durante el movimiento forzado.

---

## Análisis de Señales ECG

### ECG Estado Basal

#### Gráficas de la Señal

| Dominio del Tiempo | Dominio de la Frecuencia (Raw) | Dominio de la Frecuencia (Filtrada) | Comparación de Señales |
|--------------------|---------------------------------|-------------------------------------|------------------------|
| ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/ECG/Basal/1.jpg) | ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/ECG/Basal/2.jpg) | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/ECG/Basal/3.jpg) | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/ECG/Basal/4.jpg) |

#### Análisis del Filtro

| Diagrama de Bode | Diagrama de Polos y Ceros |
|------------------|---------------------------|
| ![Diagrama de Bode](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/ECG/Basal/5.jpg) | ![Diagrama de Polos y Ceros](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Italo/ECG/Basal/6.jpg) |

#### Justificación de los Filtros
He seleccionado un filtro IIR pasa altos a 1 Hz para eliminar las componentes de baja frecuencia como desplazamientos de DC y artefactos de movimiento, un filtro FIR pasa bajos a 50 Hz para reducir el ruido de alta frecuencia sin distorsionar la señal ECG, y un filtro notch a 50 Hz para eliminar interferencias de la línea de alimentación eléctrica. Esta combinación de filtros asegura que la señal ECG en estado basal sea lo más limpia y precisa posible, facilitando un análisis fiable al eliminar tanto el ruido no deseado como las interferencias específicas sin afectar las características esenciales de la señal.

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
