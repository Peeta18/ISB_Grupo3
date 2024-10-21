# INFORME LABORATORIO 8

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Marco teórico](#2-marco-teórico)
4. [Objetivos](#3-objetivos)
5. [Materiales y equipos](#4-materiales-y-equipos)
6. [Metodología](#5-metodología)
7. [Conclusiones](#7-conclusiones)
8. [Bibliografía](#8-bibliografía)


## 1. Introducción
<p align="justify">
El procesamiento de bioseñales ha avanzado considerablemente, especialmente en el análisis de señales como EMG, EEG y ECG, fundamentales para el monitoreo de funciones musculares, cardíacas y cerebrales. La transformada Wavelet ha surgido como una herramienta clave para descomponer estas señales en sus componentes de frecuencia, lo que permite eliminar ruido y mejorar la precisión del análisis.

El presente informe revisa los principios de los filtros wavelet, su aplicación en el procesamiento de señales biomédicas, y evalúa los resultados obtenidos, ofreciendo una visión integral sobre cómo esta técnica puede ser utilizada tanto en la investigación como en el entorno clínico.
</p>

## 2. Marco teórico

**2.1 ¿Qué es la transformada de Wavelet?**
<p align="justify">
La transformada de Wavelet es una técnica matemática de análisis de señales no estacionarias que permite descomponer una señal en diferentes niveles de frecuencia y tiempo, manteniendo la localización temporal de las características de la señal. A diferencia de la transformada de Fourier, que solo proporciona información en el dominio de la frecuencia, la transformada de Wavelet permite realizar un análisis multiresolución, lo que la hace adecuada para señales con variaciones bruscas o transitorias​. [1][2][3]
</p>

**2.2 ¿Cuáles son sus características?**
   
<p align="justify">
La transformada de Wavelet destaca por una serie de características únicas que la hacen adecuada para el análisis de señales no estacionarias:

- Localización tiempo-frecuencia: A diferencia de la transformada de Fourier, que transforma una señal al dominio de la frecuencia, la transformada Wavelet proporciona información tanto en el dominio del tiempo como en el de la frecuencia. Esto es crucial para señales no estacionarias, que presentan cambios en la frecuencia a lo largo del tiempo. La Wavelet divide la señal en diferentes componentes de frecuencia, mientras mantiene la localización temporal, permitiendo identificar cuándo ocurren eventos específicos en la señal​.

- Análisis multiresolución: Uno de los aspectos más poderosos de la transformada Wavelet es su capacidad para realizar un análisis multiresolución. Esto significa que la señal se analiza a diferentes escalas, utilizando ventanas más amplias para bajas frecuencias y más estrechas para altas frecuencias. Esto es especialmente útil en el análisis de señales como EEG, ECG o EMG, donde los eventos de interés pueden variar en su frecuencia y duración​.

- Adaptabilidad: La Wavelet es capaz de ajustar dinámicamente el tamaño de la ventana de análisis según la frecuencia de la señal. Para bajas frecuencias, donde es importante obtener información de largo plazo, se utilizan ventanas más largas. En cambio, para altas frecuencias, donde se requiere una mayor precisión temporal, se utilizan ventanas más cortas. Esta adaptabilidad ofrece una ventaja sobre la transformada de Fourier con ventana, que utiliza un tamaño de ventana fijo.

- Capacidad de detección de transitorios: Las señales transitorias, como picos, rupturas o eventos cortos en una señal, son mejor detectadas por la Wavelet, que puede enfocarse en los cambios abruptos de la señal. Esto es particularmente importante en áreas como la sismología, la medicina y la ingeniería eléctrica​.

- Invertibilidad: La transformada Wavelet, al igual que la transformada de Fourier, es invertible, lo que significa que una señal puede ser reconstruida a partir de sus coeficientes de Wavelet sin pérdida de información, siempre y cuando no se alteren estos coeficientes​


**2.3 ¿Cuál es su clasificación?**
La transformada de Wavelet se clasifica en diferentes tipos según cómo se implemente y utilice para el análisis de señales.
Las principales clasificaciones incluyen:

- Transformada Wavelet Continua (CWT):
La transformada Wavelet continua se utiliza para obtener una representación detallada de la señal en función de una escala continua de tiempo y frecuencia. Esta transformada es altamente redundante, ya que genera una gran cantidad de coeficientes que representan la señal en todas las posibles escalas y posiciones temporales. Aunque ofrece un análisis detallado, su alta redundancia la hace menos eficiente en términos de procesamiento y almacenamiento. La CWT es especialmente útil para aplicaciones donde se requiere una alta precisión en la localización tanto temporal como frecuencial​.

- Transformada Wavelet Discreta (DWT):
A diferencia de la CWT, la transformada Wavelet discreta trabaja con un conjunto discreto de escalas y posiciones. Esto reduce significativamente la redundancia y hace que la DWT sea más eficiente en términos de cálculo y almacenamiento. La DWT se basa en un banco de filtros que divide la señal en componentes de baja y alta frecuencia, aplicando submuestreo para eliminar redundancias. Este tipo de transformada es muy utilizada en el procesamiento de señales biomédicas y en la compresión de datos​.

- Transformada Wavelet Estacionaria (SWT):
La SWT, también conocida como transformada Wavelet invariante al desplazamiento, es una variante de la DWT que no utiliza submuestreo. Esto significa que no se pierde información sobre la localización temporal, lo que la hace especialmente útil cuando se requiere un análisis detallado sin la pérdida de datos por desplazamiento. Sin embargo, esta ventaja viene a costa de una mayor redundancia, lo que aumenta los requerimientos de almacenamiento y procesamiento​.

- Wavelet Shrinkage (Umbralización por Wavelet):
Este método se utiliza para la eliminación de ruido en señales. En el proceso de shrinkage, se aplican umbrales a los coeficientes Wavelet para suprimir los que contienen principalmente ruido, mientras se conservan aquellos que representan la señal útil. Esta técnica se emplea en señales como ECG y EEG, donde es fundamental eliminar interferencias y artefactos sin comprometer la integridad de la señal​.


## 3. Objetivos

1. Implementar los principios de los filtros wavelet para mejorar señales ECG, EMG y EEG.
2. Aplicar filtros wavelet para reducir ruido y extraer características relevantes en las señales.
3. Evaluar la eficacia de los filtros wavelet en la mejora y análisis de señales biomédicas.
   
## 4. Materiales y equipos

<div align="center">

|   Modelo      | Descripción   | Cantidad |
|---------------|---------------|----------|
| (R)EVOLUTION  | Kit BITalino  | 1        |
|      -      |Electrodos con gel| 3|
|       -       | Laptop o PC   | 1        |

</div>


## 5. Metodología

### 5.1. Análisis de Señales ECG

Las señales de electrocardiograma (ECG) fueron adquiridas durante diferentes condiciones experimentales: en estado basal (reposo), durante respiración controlada y después de ejercicio. Estas señales se almacenaron en formato de texto y se muestrearon a una frecuencia de 1000 Hz. Este muestreo asegura una adecuada captura de la dinámica cardíaca y cumple con el teorema de Nyquist, evitando la pérdida de información relevante durante el proceso de digitalización.

#### Aplicación del Filtro Wavelet
Para el procesamiento de las señales ECG, se implementó un enfoque basado en la transformada wavelet, utilizando específicamente la wavelet biortogonal 3.1 debido a sus propiedades de simetría y efectividad en el manejo de señales no estacionarias [2]. El proceso se divide en varias etapas clave:

1. **Descomposición Wavelet:**
   - La señal de ECG se descompuso utilizando la transformada wavelet biortogonal 3.1. Este proceso permite separar las componentes de frecuencia de la señal en diferentes niveles, aislando los detalles y las aproximaciones de frecuencia baja y alta.

2. **Umbralización:**
   - Se aplicó una técnica de umbralización suave a los coeficientes wavelet para atenuar o eliminar el ruido. El umbral utilizado se basó en la fórmula `sqrt(2 * log(longitud de la señal))` , optimizada para la reducción del ruido mientras se conservan las características fundamentales de la señal ECG.

3. **Reconstrucción:**
   - Utilizando los coeficientes wavelet modificados, se reconstruyó la señal filtrada. Este paso es crucial para asegurar que los elementos esenciales de la señal, como los picos R, Q y S del complejo QRS, se mantengan claros y bien definidos, facilitando su identificación y análisis.

4. **Evaluación de la Frecuencia:**
   - La señal filtrada fue analizada mediante la Transformada Rápida de Fourier (FFT) para verificar la preservación de los componentes de frecuencia relevantes, especialmente aquellos asociados con el complejo QRS, crucial para el diagnóstico cardíaco.

#### Visualización

Las señales, tanto crudas como procesadas con el filtro wavelet, fueron visualizadas para permitir una comparación directa de los efectos del filtrado. Este análisis visual enfatizó la capacidad del filtro wavelet para preservar las formas características de la señal ECG y su efectividad en la eliminación del ruido, mejorando así la calidad de la señal para usos clínicos y de investigación.


| Momento             | Señal Cruda   |
|---------------------|---------------|
| Reposo            | ![ECG](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab8_Wavelet/Se%C3%B1al_reposo_ECG.jpeg)         
| Estado basal    | ![ECG](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab8_Wavelet/Se%C3%B1al_estadobasal_ECG.jpeg)   | 
| Ejercicio  | ![ECG](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab8_Wavelet/Se%C3%B1al_ejercicio_ECG.jpeg)   |



### 5.2. Análisis de Señales EMG:







### 5.3. Análisis de Señales EEG:








## 8. Bibliografía

