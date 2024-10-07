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

---

## Introducción

### Filtros

Un filtro es un sistema que permite modificar la señal de entrada en función de sus componentes frecuenciales, de manera que ciertas frecuencias sean atenuadas, amplificadas o eliminadas por completo. Los filtros juegan un papel fundamental en el procesamiento de señales, permitiendo la eliminación de ruido o la separación de señales de interés. El concepto de filtrado se puede aplicar tanto en el dominio de las señales continuas (analógicas) como en el de las discretas (digitales), y dependiendo de su implementación y diseño, los filtros pueden clasificarse en varias categorías.

### Filtros Analógicos y Digitales

Los filtros analógicos operan sobre señales continuas y se construyen utilizando componentes electrónicos como resistencias, capacitores y bobinas. Estos filtros son usados principalmente en el procesamiento de señales en tiempo real, como señales de audio y radiofrecuencia. Por otro lado, los filtros digitales operan sobre señales discretas y se implementan mediante algoritmos matemáticos en sistemas digitales. Estos filtros son más flexibles, ya que se pueden reconfigurar y ajustar con facilidad, y son capaces de manejar señales complejas y realizar operaciones avanzadas, como filtrado en tiempo real y análisis en el dominio de la frecuencia.

### Filtros FIR e IIR

Los filtros digitales pueden clasificarse en dos grandes tipos: FIR (Finite Impulse Response) e IIR (Infinite Impulse Response), cada uno con características y aplicaciones particulares. A continuación, se describen sus principales características y subtipos.

#### Subtipos de Filtros FIR

Los filtros FIR tienen una respuesta al impulso finita, lo que significa que la salida del filtro responde a la entrada por un periodo de tiempo limitado. Son conocidos por su estabilidad inherente y su fase lineal, lo que los hace ideales para aplicaciones donde la distorsión de fase es crítica. Los filtros FIR se pueden diseñar utilizando diferentes ventanas para moldear su respuesta en frecuencia.

| Subtipos de Filtros FIR | Descripción                                     |
|-------------------------|-------------------------------------------------|
| **Ventana Rectangular**  | Ventana simple y eficiente, pero con mucho "rippling" en la respuesta. |
| **Ventana de Hamming**   | Reduce el "rippling", mejora la atenuación en las bandas. |
| **Ventana de Hanning**   | Ventana suave, utilizada para reducir los efectos de las discontinuidades en los bordes. |
| **Ventana de Blackman**  | Proporciona una mejor atenuación de las bandas laterales. |
| **Ventana de Kaiser**    | Ventana ajustable que permite controlar el ancho de banda y el nivel de atenuación. |

#### Subtipos de Filtros IIR

Los filtros IIR se caracterizan por tener una respuesta infinita al impulso, es decir, su salida depende no solo de las entradas presentes, sino también de las entradas y salidas pasadas. Estos filtros son más eficientes que los FIR en términos de número de coeficientes para una misma especificación de diseño, pero pueden ser inestables y no siempre tienen una fase lineal. Existen varios tipos de filtros IIR, cada uno con propiedades particulares.

| Subtipos de Filtros IIR | Descripción                                     |
|-------------------------|-------------------------------------------------|
| **Filtro Butterworth**   | Filtro con una respuesta en frecuencia lo más plana posible en la banda de paso. |
| **Filtro Chebyshev I**   | Presenta una respuesta con rizado en la banda de paso para obtener una transición más rápida. |
| **Filtro Chebyshev II**  | Tiene rizado en la banda de rechazo en lugar de la banda de paso. |
| **Filtro Elíptico**      | Ofrece la transición más rápida entre la banda de paso y la banda de rechazo, a cambio de rizado en ambas bandas. |
| **Filtro Bessel**        | Optimiza la respuesta de fase, con una transición lenta en frecuencia. |

### Objetivos del Laboratorio

El objetivo principal de este laboratorio es aplicar filtros digitales sobre señales electromiográficas (EMG) y electrocardiográficas (ECG) obtenidas en sesiones anteriores para eliminar componentes de ruido y mejorar la calidad de las señales. Se busca analizar el efecto de diferentes tipos de filtros (FIR e IIR) en las señales de entrada, evaluando su desempeño tanto en el dominio del tiempo como en el dominio de la frecuencia. A través de este proceso, se pretende comprender mejor la aplicación de técnicas de filtrado y las diferencias en los resultados obtenidos entre los diferentes filtros seleccionados.

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
| ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/e978bb50de06bc5385ebe88109682c92ebe0ab9b/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/img-piero/volunt/raw.png)
