Elaboración individual - Etefany Valverde Salinas 

# Análisis de Señales EMG y ECG

<div align="justify">

Este documento presenta un análisis detallado de señales electromiográficas (EMG) y electrocardiográficas (ECG) seleccionadas de laboratorios anteriores. Cada señal ha sido elegida para representar diversas actividades y ha sido procesada mediante filtros de respuesta impulsiva finita (FIR) o infinita (IIR) para su análisis en los dominios del tiempo y de la frecuencia. En este archivo, se incluyen gráficas comparativas de las señales originales y filtradas, análisis en el dominio de la frecuencia. Adicionalmente, se ofrece un estudio de los filtros aplicados, ilustrando cada uno mediante diagramas de polos y ceros, así como diagramas de Bode que detallan la magnitud y la fase. Finalizamos con una justificación de la elección de estos filtros, destacando su relevancia y eficacia en el tratamiento de las señales EMG y ECG para los objetivos de este estudio.

</div>


## Tabla de Contenidos
-  [Introducción]
-  [Objetivos] 
-  [Análisis de Señales EMG](#análisis-de-señales-emg)
  - [EMG en Reposo](#emg-en-reposo)
  - [EMG Movimiento Voluntario](#emg-movimiento-voluntario)
  - [EMG Movimiento Forzado](#emg-movimiento-forzado)
- [Análisis de Señales ECG](#análisis-de-señales-ecg)
  - [ECG Estado Basal](#ecg-estado-basal)
  - [ECG Luego de Respiración](#ecg-luego-de-respiración)
  - [ECG Luego de Ejercicio](#ecg-luego-de-ejercicio)
   
## Introducción

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


## Objetivos del Laboratorio
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

