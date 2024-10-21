# INFORME LABORATORIO 8

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Marco teórico](#2-marco-teórico)
4. [Objetivos](#3-objetivos)
5. [Materiales y equipos](#4-materiales-y-equipos)
6. [Metodología](#5-metodología)
7. [Resultados](#6-resultados)
8. [Discusión](#7-discusión)
9. [Conclusiones](#8-conclusiones)
10. [Bibliografía](#9-bibliografía)


## 1. Introducción

El procesamiento de bioseñales ha avanzado considerablemente, especialmente en el análisis de señales como EMG, EEG y ECG, fundamentales para el monitoreo de funciones musculares, cardíacas y cerebrales. La transformada Wavelet ha surgido como una herramienta clave para descomponer estas señales en sus componentes de frecuencia, lo que permite eliminar ruido y mejorar la precisión del análisis.

El presente informe revisa los principios de los filtros wavelet, su aplicación en el procesamiento de señales biomédicas, y evalúa los resultados obtenidos, ofreciendo una visión integral sobre cómo esta técnica puede ser utilizada tanto en la investigación como en el entorno clínico.

## 2. Marco teórico




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


### 5.2. Análisis de Señales EMG:

#### Adquisición de las señales

Se obtuvieron las señales de EMG en diferentes actividades músculares: Oposición, Reposo, Extensión y Flexión. Las señales se almacenaron en formato de texto y se muestrearon a una frecuencia de 1000 Hz. Para analizar las señales y reducir el ruido inherente a las mediciones de EMG, se aplicaron filtros DWT.g

#### Preprocesamiento de las señales

Aplicamos un filtro pasa-bajos para eliminar la alta frecuencia no deseada.

#### Aplicación del Filtro Wavelet

  1. **Descommposición mediante la Transformada de Wavelet**: escogemos una wavelet madre     adecuada, como la wavelet Daubechies (db4) o Symlet (syms5), según las características de tus señales EMG. Después, se descompone la señal EMG en varios niveles utilizando la Transformada Wavelet Discreta (DWT). Por ejemplo, se puede descomponer la señal en 5 niveles: $$\text{coeff} = [ca_5, cd_5, cd_4, cd_3, cd_2, cd_1]$$ donde `ca` son los coeficientes de aproximación y `cd` son los coeficientes de detalle [3].

  2. **Reducción de Ruido (Denoising)**: Acá se analizan los coeficientes de wavelet para estimar el nivel del reuido presente en la señal, y luego aplicamos un umbral suave o duro a los coeficientes de wavelet. El método de umbral suave reduce los coeficientes por una cantidad fija, mientras que el umbral duro elimina completamente si esetán por debajo de cierto valor [3].
     * **Modelo de Señal con Ruido**: La señal EMG con ruido se modela como: $$f(t)=s(t)+n(t)$$ donde s(t) es la señal de EMG y n(t) es el ruido Gaussiano blanco.
       
  4. **Umbralización**:
  * **Umbral suave (Soft Thresholding)**: Reduce gradualmente los coeficientes: $$w' = \text{sign}(w) \cdot (\lvert w \rvert - \lambda)_+$$
  * **Umbral duro (Hard Thresholding)**: Elimina completamente los coeficientes por debajo del umbral:

![Fórmula](https://latex.codecogs.com/png.latex?w%27%3D%5Cbegin%7Bcases%7D%20w%20%26%20%5Ctext%7Bsi%7D%20%7Cw%7C%20%5Cgeq%20%5Clambda%20%5C%5C%200%20%26%20%5Ctext%7Bsi%7D%20%7Cw%7C%20%3C%20%5Clambda%5Cend%7Bcases%7D)

donde `w` son los coeficientes wavelet y `lambda` es el valor del umbral.

  3. **Reconstrucción de la señal**: Se utiliza los coeficientes wavelet ajustados (post-umbralización) para reconstruir la señal EMG utilizando la inversa de la Transformada Wavelet Discreta (IDWT) [3]. 

  4. **Extracción y Análisis**: Acá se calcula la energía de los coeficientes wavelet en cada nivel de descomposición como características: $$E_j = \sum_{k} (\text{coeff}_{j,k})^2$$
Una vez con ello, se forma un vector de características con las energías de los diferentes niveles y otras posibles características relevantes [3]. 

### 5.3. Análisis de Señales EEG:
Las señales de electroencefalograma (EEG) fueron adquiridas durante diferentes condiciones experimentales: en estado basal (reposo), durante ciclos de abrir y cerrar ojos, y durante la resolución de preguntas matemáticas. Estas señales se almacenaron en formato de texto y se muestrearon a una frecuencia de 1000 Hz.
    

#### Aplicación del Filtro Wavelet

Para el procesamiento de las señales EEG, se aplicó un filtro Wavelet Daubechies8 (db8), con 4 niveles de descomposición. Según bibliografía [4], este proceso nos ofrece una buena forma de eliminación de ruino en señales obtenidas de sujetos sanos. Este filtro está nfocado en la diferencia cuadrática media para encontrar la utilidad de la eliminación de ruido. Debido a sus propiedades de simetría y efectividad en el manejo de señales no estacionarias. En el proceso se tomó en cuenta lo siguiente: 


  1. **Descomposición:**

  Se utilizó la db8, la cual es la octaba familia de Daubechies, la cual tiene 16 coeficientes en su filtro de descomposición. Este número de coeficientes determina la longitud de la Wavelet y afecta su capacidad para capturar detalles de la señal. 

  2. **Umbralización:**

  Se aplicó una técnica de umbralización suave a los coeficientes wavelet para atenuar o eliminar el ruido. El valor del umbral se puede ponderar de acuerdo con los valores de los coeficientes por escala, de esta forma el umbral puede ser dependiente del ruido encontrado por niveles [5]. Por tanto, se utilizó la ponderación de primer nivel, en donde se calcula el nivel del ruido de los coedificientes del primer nivel de descomposición a partir de las fórmulas:

![desviación absoluta mediana](https://latex.codecogs.com/png.image?\dpi{110}\delta_{\text{mad}}=\frac{\text{median}\{|c_0|,|c_1|,\ldots,|c_{n-1}|\}}{0.6745})

![Umbral](https://latex.codecogs.com/png.image?\dpi{110}\text{Threshold},\tau=\delta_{\text{mad}}\sqrt{\ln(N)}), donde |C<sub>0</sub>|, |C<sub>1</sub>|,…,|C<sub>corte</sub> - 1| son los coeficientes wavelet y 0,6745 en el denominador cambia la escala del numerador para que sea un estimador adecuado para la desviación estándar del ruido blanco gaussiano.

  3. **Reconstrucción de la señal**:
  Los coeficientes modificados se utilizan para reconstruir la señal original. Esta señal reconstruida tiene menos ruido y conserva las características esenciales de la señal original. Además, la función pywt.waverec realiza esta reconstrucción a partir de los coeficientes umbralizados.

