# INFORME LABORATORIO 8

## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Marco teórico](#2-marco-teórico)
3. [Objetivos](#3-objetivos)
4. [Materiales y equipos](#4-materiales-y-equipos)
5. [Metodología](#5-metodología)
6. [Conclusiones](#7-conclusiones)
7. [Bibliografía](#8-bibliografía)


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
La transformada de Wavelet destaca por una serie de características únicas que la hacen adecuada para el análisis de señales no estacionarias: [1][2][4]

- Localización tiempo-frecuencia: A diferencia de la transformada de Fourier, que transforma una señal al dominio de la frecuencia, la transformada Wavelet proporciona información tanto en el dominio del tiempo como en el de la frecuencia. Esto es crucial para señales no estacionarias, que presentan cambios en la frecuencia a lo largo del tiempo. La Wavelet divide la señal en diferentes componentes de frecuencia, mientras mantiene la localización temporal, permitiendo identificar cuándo ocurren eventos específicos en la señal​.

- Análisis multiresolución: Uno de los aspectos más poderosos de la transformada Wavelet es su capacidad para realizar un análisis multiresolución. Esto significa que la señal se analiza a diferentes escalas, utilizando ventanas más amplias para bajas frecuencias y más estrechas para altas frecuencias. Esto es especialmente útil en el análisis de señales como EEG, ECG o EMG, donde los eventos de interés pueden variar en su frecuencia y duración​.

- Adaptabilidad: La Wavelet es capaz de ajustar dinámicamente el tamaño de la ventana de análisis según la frecuencia de la señal. Para bajas frecuencias, donde es importante obtener información de largo plazo, se utilizan ventanas más largas. En cambio, para altas frecuencias, donde se requiere una mayor precisión temporal, se utilizan ventanas más cortas. Esta adaptabilidad ofrece una ventaja sobre la transformada de Fourier con ventana, que utiliza un tamaño de ventana fijo.

- Capacidad de detección de transitorios: Las señales transitorias, como picos, rupturas o eventos cortos en una señal, son mejor detectadas por la Wavelet, que puede enfocarse en los cambios abruptos de la señal. Esto es particularmente importante en áreas como la sismología, la medicina y la ingeniería eléctrica​.

- Invertibilidad: La transformada Wavelet, al igual que la transformada de Fourier, es invertible, lo que significa que una señal puede ser reconstruida a partir de sus coeficientes de Wavelet sin pérdida de información, siempre y cuando no se alteren estos coeficientes​


**2.3 ¿Cuál es su clasificación?**
La transformada de Wavelet se clasifica en diferentes tipos según cómo se implemente y utilice para el análisis de señales. [4][2][3]
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

El análisis de señales ECG es crucial en la medicina actual, ya que permite la detección y monitoreo de una amplia variedad de condiciones cardíacas de manera precisa y no invasiva. Con el avance de la tecnología y los métodos de procesamiento de señales, la capacidad de analizar y diagnosticar problemas cardíacos se ha vuelto más eficiente, mejorando la calidad de vida de millones de personas.

#### Aplicación del Filtro Wavelet
Para el procesamiento de las señales ECG, se implementó un enfoque basado en la transformada wavelet, utilizando específicamente la wavelet biortogonal 3.1 debido a sus propiedades de simetría y efectividad en el manejo de señales no estacionarias [2]. El proceso se divide en varias etapas clave:

1. **Descomposición Wavelet:**
   - La descomposición de la señal ECG se realiza utilizando la transformada wavelet biortogonal 3.1, como se sugiere en el paper. Esta wavelet es adecuada por sus propiedades de simetría, lo cual ayuda a preservar las características importantes de la señal ECG, como los picos y las transiciones abruptas. En el código proporcionado, utilizaste 'db6', que también es una opción válida, pero si queremos seguir estrictamente el paper, debemos cambiar a 'bior3.1' para la descomposición.

2. **Umbralización:**
   - El paper menciona una técnica de umbralización suave basada en la fórmula: `umbral= std(señal)*sqrt(2 * log(número de muestras))`. Esto es congruente con lo que se hizo en el código proporcionado. Este umbral ayuda a reducir el ruido sin perder información relevante de la señal, como los picos del complejo QRS. Es importante asegurarse de que el nivel de umbral sea lo suficientemente bajo para atenuar el ruido pero no tan alto como para eliminar detalles importantes de la señal.

3. **Reconstrucción:**
   - Una vez aplicados los umbrales, los coeficientes wavelet modificados se reconstruyen para formar la señal filtrada. Este paso es crucial para mantener las características esenciales de la señal, y el uso de wavelets biortogonales (como 'bior3.1') permite una reconstrucción precisa sin distorsión de las formas de onda clave del ECG.

4. **Evaluación de la Frecuencia:**
   - Finalmente, el análisis de la señal filtrada se realiza utilizando la Transformada Rápida de Fourier (FFT) para verificar la preservación de los picos y características relevantes del ECG. Esto es fundamental para evaluar las frecuencias relacionadas con eventos cardíacos, como el complejo QRS, y es esencial para diagnósticos clínicos precisos.

#### Visualización

Las señales, tanto crudas como procesadas con el filtro wavelet, fueron visualizadas para permitir una comparación directa de los efectos del filtrado. Este análisis visual enfatizó la capacidad del filtro wavelet para preservar las formas características de la señal ECG y su efectividad en la eliminación del ruido, mejorando así la calidad de la señal para usos clínicos y de investigación.


| Momento             | Señal Cruda   |
|---------------------|---------------|
| Reposo            | ![ECG](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab8_Wavelet/Se%C3%B1al_reposo_ECG.jpeg)         
| Estado basal    | ![ECG](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab8_Wavelet/Se%C3%B1al_estadobasal_ECG.jpeg)   | 
| Ejercicio  | ![ECG](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab8_Wavelet/Se%C3%B1al_ejercicio_ECG.jpeg)   |



### 5.2. Análisis de Señales EMG:

#### Aplicación del Filtro Wavelet
Para el procesamiento de las señales EMG, se implementó un enfoque basado en la transformada wavelet, utilizando específicamente la wavelet Daubechies de séptimo orden y descomposición wavelet de cuarto nivel, debido a su buena capacidad de extracción de características [5]

![Descomposición](https://github.com/Peeta18/ISB_Grupo3/blob/ac4cebe0ba4a354e3936559b5b1755d379d2ab3f/ISB/Laboratorios/Lab8_Wavelet/images/coef-1.png)
![Descomposición](https://github.com/Peeta18/ISB_Grupo3/blob/ac4cebe0ba4a354e3936559b5b1755d379d2ab3f/ISB/Laboratorios/Lab8_Wavelet/images/coef-2.png)

- **Coeficientes de Detalle (Niveles 1 a 5)**: Los detalles en niveles superiores capturan cambios más lentos. Niveles como el 1 y 2 capturan las variaciones de alta frecuencia (ruido o cambios rápidos), mientras que los niveles 4 y 5 se concentran en componentes más suaves.
- **Coeficientes de Aproximación**: Se aprecia cómo las componentes de baja frecuencia tienen una amplitud más constante, y se suavizan los detalles presentes en las otras gráficas.

#### Incorporación de ruido para evaluación del filtro Wavelet

En este estudio se evaluaron dos técnicas de denoising (hard y soft thresholding) aplicadas a señales EMG con diferentes niveles de ruido. Los resultados mostraron que, en términos de SNR post-denoising, la técnica de soft thresholding logra una mejor reducción del ruido residual en todos los niveles de SNR evaluados, con una diferencia significativa en condiciones de ruido elevado (SNR < -10 dB). Por lo tanto, se recomienda el uso de soft thresholding para aplicaciones en las que la preservación de la señal es crítica y el ruido es significativo

![Descomposición](https://github.com/Peeta18/ISB_Grupo3/blob/ac4cebe0ba4a354e3936559b5b1755d379d2ab3f/ISB/Laboratorios/Lab8_Wavelet/images/comp-2.png)
![Descomposición](https://github.com/Peeta18/ISB_Grupo3/blob/ac4cebe0ba4a354e3936559b5b1755d379d2ab3f/ISB/Laboratorios/Lab8_Wavelet/images/comp-3.png)

- **SNR = -3 dB (Alto Nivel de Ruido)**: La señal ruidosa tiene una amplitud mucho mayor y cubre por completo la señal original (primer gráfico de la izquierda). En el denoised con Hard Thresholding (gráfico central superior), se ve que se ha eliminado parte del ruido, pero aún se observan picos pronunciados y la morfología de la señal original no se preserva completamente. En el denoised con Soft Thresholding (gráfico superior derecho), la señal está menos distorsionada y se observa que los picos son menos prominentes en comparación con el hard thresholding, lo que sugiere que soft thresholding podría estar preservando mejor la estructura de la señal original a pesar del ruido.

- **SNR = -8 dB (Nivel Moderado de Ruido)**: La señal ruidosa tiene un alto nivel de variación (gráfico inferior izquierdo) que complica la visualización de la señal original. En el denoised con Hard Thresholding (gráfico inferior central), hay una eliminación considerable de ruido, pero también se observa pérdida de información (picos importantes de la señal original parecen haber sido suavizados o eliminados). En el denoised con Soft Thresholding (gráfico inferior derecho), la señal denoised sigue manteniendo algunas de las variaciones de la señal original, lo que sugiere una mejor preservación de las características de la señal en comparación con hard thresholding.

![Descomposición](https://github.com/Peeta18/ISB_Grupo3/blob/ac4cebe0ba4a354e3936559b5b1755d379d2ab3f/ISB/Laboratorios/Lab8_Wavelet/images/comp-1.png)

Ninguna de las técnicas probadas logra mejorar significativamente el SNR post-denoising en condiciones extremas de ruido (SNR inicial menor a -10 dB), lo cual sugiere que técnicas más avanzadas, como umbrales adaptativos o métodos basados en aprendizaje profundo, podrían ser necesarias para aplicaciones de EMG en entornos de alto ruido.

### 5.3. Análisis de Señales EEG:







### 6. Conclusiones






## 7. Bibliografía

1. A. Fernández-Lavín and E. Ovando-Shelley, "Método de Filtrado con Wavelet para el Análisis de Señales," Conference Paper, Nov. 2019. [Online]. Available: https://www.researchgate.net/publication/337447627. [Accessed: Oct. 2024].
2. D. M. Ballesteros Larrotta, "Aplicación de la transformada wavelet discreta en el filtrado de señales bioeléctricas," Umbral Científico, vol. 5, pp. 92-98, Dec. 2004. [Online]. Available: http://www.redalyc.org/articulo.oa?id=30400512. [Accessed: Oct. 2024].
3. O. J. Olarte Rodríguez and D. A. Sierra Bueno, "Determinación de los Parámetros Asociados al Filtro Wavelet por Umbralización Aplicado a Filtrado de Interferencias Electrocardiográficas," Revista de la Facultad de Ingenierías Físico Mecánicas, vol. 6, no. 2, pp. 33-44, Dec. 2007.
4. S. Kouro and R. Musalem, "Tutorial introductorio a la teoría de Wavelet," Técnicas Modernas en Automática, Universidad Técnica Federico Santa María, Jul. 2002.
5. A. Phinyomark, C. Limsakul, and P. Phukpattaranont, “Application of Wavelet Analysis in EMG Feature Extraction for Pattern Classification,” Measurement Science Review, vol. 11, no. 2, Jan. 2011, doi: https://doi.org/10.2478/v10048-011-0009-y.
‌
