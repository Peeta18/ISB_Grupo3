Elaboración individual - Etefany Valverde Salinas 

# Análisis de Señales EMG y ECG

<div align="justify">

Este documento presenta un análisis detallado de señales electromiográficas (EMG) y electrocardiográficas (ECG) seleccionadas de laboratorios anteriores. Cada señal ha sido elegida para representar diversas actividades y ha sido procesada mediante filtros de respuesta impulsiva finita (FIR) o infinita (IIR) para su análisis en los dominios del tiempo y de la frecuencia. En este archivo, se incluyen gráficas comparativas de las señales originales y filtradas, análisis en el dominio de la frecuencia. Adicionalmente, se ofrece un estudio de los filtros aplicados, ilustrando cada uno mediante diagramas de polos y ceros, así como diagramas de Bode que detallan la magnitud y la fase. Finalizamos con una justificación de la elección de estos filtros, destacando su relevancia y eficacia en el tratamiento de las señales EMG y ECG para los objetivos de este estudio.

</div>


## Tabla de Contenidos
-  [Introducción](#Introducción)
-  [Objetivos](#objetivos)
-  [Análisis de Señales EMG](#análisis-de-señales-emg)
    - [EMG en Reposo](#emg-en-reposo)
    - [EMG Movimiento Voluntario](#emg-en-movimiento-voluntario)
    - [EMG Movimiento Forzado](#emg-en-movimiento-forzado)
- [Análisis de Señales ECG](#análisis-de-señales-ecg)
  - [ECG Estado Basal](#ecg-estado-basal)
  - [ECG Luego de Respiración](#ecg-luego-de-respiración)
  - [ECG Luego de Ejercicio](#ecg-luego-de-ejercicio)
- [Referencias bibliograficas](#referencias-bibliograficas)
### Introducción

### Filtros
<div align="justify">
Un filtro es un dispositivo o algoritmo que transforma una señal de entrada para producir una señal de salida con características específicas, como la reducción de ruido o la selección de ciertas frecuencias. Los filtros son esenciales en el procesamiento de señales, ya que permiten mejorar, limpiar o extraer información relevante de las señales que provienen de diversas fuentes, como sensores biomédicos, sistemas de comunicación o dispositivos de audio.
</div>

### Filtros Analógicos y Digitales
<div align="justify">
Los filtros se dividen en dos categorías principales: analógicos y digitales. Los filtros analógicos trabajan con señales continuas en el tiempo y se implementan utilizando componentes electrónicos como resistencias, capacitores e inductores. Estos filtros son comunes en aplicaciones en tiempo real, como sistemas de radio y audio, donde la velocidad de respuesta es crucial. En contraste, los filtros digitales operan con señales discretas en el tiempo y se implementan mediante algoritmos matemáticos en sistemas digitales, como microcontroladores o procesadores de señales digitales (DSP). A diferencia de los filtros analógicos, los digitales ofrecen mayor flexibilidad y precisión, ya que sus parámetros pueden ajustarse y optimizarse fácilmente para diferentes aplicaciones sin necesidad de modificar el hardware.[1][2]
</div>

### Filtros FIR e IIR
<div align="justify">
Dentro de los filtros digitales, se distinguen dos categorías principales: FIR (Finite Impulse Response) y IIR (Infinite Impulse Response). Cada uno posee características particulares que los hacen más adecuados para distintas aplicaciones de procesamiento de señales. Los filtros FIR tienen una respuesta de impulso finita, lo que significa que su salida eventualmente llega a cero después de un tiempo finito. Son conocidos por su estabilidad inherente y por no introducir distorsión de fase, lo que los hace ideales en aplicaciones donde la precisión y la estabilidad son fundamentales, como en la corrección de imágenes o en ciertos sistemas de comunicación. Por otro lado, los filtros IIR tienen una respuesta de impulso infinita, es decir, su salida puede continuar indefinidamente. Aunque estos filtros suelen ser más eficientes en términos de cálculo debido a que requieren menos coeficientes, pueden introducir distorsión de fase y ser menos estables si no se diseñan adecuadamente. Sin embargo, su capacidad para imitar características de los filtros analógicos los hace útiles en aplicaciones donde la eficiencia computacional es crucial, como en el procesamiento de audio en tiempo real.[3].
</div>


### Objetivos 
<div align="justify">
El objetivo principal de este laboratorio es aplicar filtros digitales a señales electromiográficas (EMG) y electrocardiográficas (ECG) obtenidas en sesiones previas, con el fin de:
</div>

<div align="justify">
- Eliminar componentes de ruido y mejorar la calidad de las señales.
- Analizar el efecto de distintos tipos de filtros (FIR e IIR) sobre las señales de entrada.
- Evaluar el desempeño de los filtros tanto en el dominio del tiempo como en el dominio de la frecuencia.
- Comprender las diferencias en los resultados obtenidos entre los diferentes filtros seleccionados.
</div>


### EMG en REPOSO

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica respuesta de frecuencia filtro pasa alta**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/respuesta%20de%20frecuencai%20filtro%20pasa%20alto.png) |
| **Gráfica de señal original y filtrada**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/se%C3%B1ale%20original%20y%20filtrada.png) |
| **Gráfica de análisis de frecuencia original y filtrada** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/analisis%20frecuencia%20origial%20y%20filtrada.png) |
| **Espectograma**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/espectograma.png)                 |
| **Diagrama de polos y ceros**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/diagrama%20polos%20y%20ceros.png)                 |
| **Diagrama de Bode**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/diagrama%20de%20bode.png)                 |

**Análisis de Señales EMG en Reposo con Filtro FIR Pasa Banda**
El filtro FIR pasa banda es utilizado para procesar señales EMG en reposo principalmente para eliminar interferencias de baja frecuencia y ruido de línea base, lo cual es esencial para obtener una representación clara de la actividad muscular intrínseca. La gráfica de respuesta de frecuencia del filtro muestra una atenuación efectiva de las frecuencias por debajo de un umbral, lo cual ayuda a centrar la señal alrededor de cero y a eliminar artefactos que podrían distorsionar el análisis. Las imágenes ilustran cómo el filtro limpia la señal, haciendo que la actividad eléctrica muscular real sea más distinguible y la medición más precisa, especialmente útil en escenarios clínicos o de investigación donde la exactitud es crucial.

**Elección y Beneficios del Filtro FIR Pasa Banda**
Los filtros FIR son preferidos en el tratamiento de señales EMG debido a sus características de fase lineal, que son fundamentales para mantener la integridad temporal y la forma de la señal original. Este tipo de filtro no solo asegura la estabilidad sin riesgo de oscilaciones, como se observa en el diagrama de polos y ceros, sino que también permite un diseño de respuesta en frecuencia altamente controlable y ajustable a las necesidades específicas del análisis EMG. El diagrama de Bode refleja cómo el filtro preserva las características de la señal dentro de un rango de frecuencia definido mientras atenúa efectivamente el ruido y otras señales no deseadas fuera de este rango, optimizando así la calidad de la señal para su posterior evaluación y análisis.



### EMG en Movimiento voluntario

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica respuesta de frecuencia filtro pasa alta**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/VOLUNTARIO/analisis%20de%20frecuencia.png) |
| **Gráfica de señal original y filtrada**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/VOLUNTARIO/se%C3%B1al%20original%20y%20filtrada.png) |
| **Gráfica de análisis de frecuencia original y filtrada** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/REPOSO/analisis%20frecuencia%20origial%20y%20filtrada.png) |
| **Espectograma**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/VOLUNTARIO/espectograma.png)                 |
| **Diagrama de polos y ceros**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/VOLUNTARIO/diagrama%20de%20polos%20y%20ceros.png)                 |
| **Diagrama de Bode**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/VOLUNTARIO/diagrama%20de%20bode.png)                 |


### EMG en MOVIMIENTO FORZADO

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica respuesta de frecuencia filtro pasa alta**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/MAX/respuesta%20de%20frecuencia%20pasa%20alto.png) |
| **Gráfica de señal original y filtrada**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/MAX/se%C3%B1al%20original%20y%20filtrada.png) |
| **Gráfica de análisis de frecuencia original y filtrada** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/MAX/analisis%20de%20frecuencia.png) |
| **Espectograma**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/MAX/espectograma.png)                 |
| **Diagrama de polos y ceros**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/MAX/diagrama%20de%20polos%20y%20ceros.png)                 |
| **Diagrama de Bode**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/MAX/diagrama%20de%20bode.png)                 |


**Análisis de Señales EMG Durante Movimiento Voluntario**
La gráfica de respuesta de frecuencia del filtro pasa alta muestra una efectiva eliminación de frecuencias bajas, lo cual es esencial para aislar las frecuencias asociadas con la contracción muscular activa en el EMG durante el movimiento voluntario. Esta señal filtrada revela una reducción significativa en el ruido y las fluctuaciones de línea base, permitiendo una visualización más clara de la actividad muscular genuina. El uso de un filtro FIR pasa banda en el procesamiento de EMG se justifica por su capacidad para preservar la integridad de la señal mientras se eliminan interferencias no deseadas es especialmente adecuado para señales EMG debido a su fase lineal, lo que garantiza que no se introduzcan distorsiones temporales en la señal, preservando así las características temporales exactas de las señales de activación muscular. El diagrama de Bode y el espectrograma muestran cómo este filtro atenúa adecuadamente el ruido mientras mantiene la estructura esencial de la señal, facilitando análisis más detallados y precisos de la actividad muscular.



### ECG EN ESTADO BASAL

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica respuesta de frecuencia filtro IIR PASA BANDA**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/BASALECG/respuesta%20frecuencia%20pasa%20banda.png) |
| **Gráfica de señal original y filtrada**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/BASALECG/se%C3%B1al%20original%20y%20filtrada.png) |
| **Gráfica de análisis de frecuencia original y filtrada** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/BASALECG/analisis%20de%20frecuencia.png) |
| **Espectograma**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/BASALECG/espectograma.png)                 |
| **Diagrama de polos y ceros**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/BASALECG/diagrama%20de%20polos.png)                 |
| **Diagrama de Bode**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/BASALECG/diagrama%20de%20bode.png)                 |


### ECG LUEGO DE RESPIRACIÓN

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica respuesta de frecuencia filtro IIR PASA BANDA**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/RESPIRACION/respuesta%20de%20frecuencia.png) |
| **Gráfica de señal original y filtrada**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/RESPIRACION/se%C3%B1al%20original%20y%20filtrada.png) |
| **Gráfica de análisis de frecuencia original y filtrada** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/RESPIRACION/analisis%20de%20frecuencia.png) |
| **Espectograma**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/RESPIRACION/espectograma.png)                 |
| **Diagrama de polos y ceros**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/BASALECG/diagrama%20de%20polos.png)                 |
| **Diagrama de Bode**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/RESPIRACION/diagrama%20de%20polos%20y%20ceros.png)                 |


### ECG LUEGO DE EJERCICIO

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Gráfica respuesta de frecuencia filtro IIR PASA BANDA**                  | ![Dominio del Tiempo](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/EJERCICIO/respuesta%20de%20frecuencia.png) |
| **Gráfica de señal original y filtrada**| ![Dominio de la Frecuencia Raw](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/EJERCICIO/se%C3%B1al%20original%20y%20filtrada.png) |
| **Gráfica de análisis de frecuencia original y filtrada** | ![Dominio de la Frecuencia Filtrada](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/EJERCICIO/analisis%20de%20frecuencia.png) |
| **Espectograma**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/EJERCICIO/espectograma.png)                 |
| **Diagrama de polos y ceros**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/EJERCICIO/diagrama%20de%20polos%20y%20ceros.png)                 |
| **Diagrama de Bode**                            | ![Comparación](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_se%C3%B1ales/Imagenes_Estefany/EJERCICIO/diagrama%20de%20bode.png)                 |

**JUSTIFICACIÓN**
El uso de un filtro IIR pasa banda en el análisis de señales ECG se justifica por su capacidad para aislar de manera efectiva las frecuencias de interés mientras se eliminan las interferencias y el ruido fuera de este rango. Este filtro es útil en aplicaciones médicas donde la precisión y la claridad de la señal son críticas, como en el caso de las señales ECG, que pueden verse afectadas por artefactos de movimiento, interferencia electromagnética, u otras señales biológicas como la respiración. La configuración pasa banda permite centrarse en las frecuencias que caracterizan los componentes cardíacos principales, como los picos QRS, eliminando frecuencias que podrían distorsionar la interpretación clínica.

En las gráficas mostradas por ejemplo del estado basal, la respuesta en frecuencia del filtro demuestra una atenuación efectiva de señales por debajo de 0.5 Hz y por encima de 150 Hz, lo cual es adecuado para señales ECG donde el interés principal radica entre estos rangos. Esto es vital para minimizar la influencia de señales de baja frecuencia como las derivadas de movimientos corporales lentos y la alta frecuencia del ruido eléctrico o electrónico. Así, el filtrado pasa banda IIR se confirma como una elección acertada, facilitando una visión más limpia y enfocada de la actividad eléctrica cardíaca esencial para diagnósticos precisos.







**REFERENCIAS BIBLIOGRAFICAS**
1. A. V. Oppenheim and R. W. Schafer, Discrete-Time Signal Processing, 3rd ed., Pearson, 2009.
2. S. Karris, The Scientist and Engineer's Guide to Digital Signal Processing, California Technical Publishing, 1997.
3. A. V. Oppenheim, Signals and Systems, 2nd ed., Prentice Hall, 1996.
