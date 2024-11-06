# LABORATORIO 10: – Procesamiento de señales ECG

## Contenido de la sesión

1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Metodología](id3)
4. [Resultados](#id4)  
5. [Discusión](#id5)  
6. [Conclusiones](#id6)  
7. [Bibliografia](#id7)
***


## Introducción <a name="id1"></a>
<div align="justify">

El electrocardiograma (ECG) se ha convertido en una herramienta esencial en la medicina moderna, utilizada ampliamente para diagnosticar y monitorear enfermedades cardiovasculares, una de las principales causas de muerte a nivel global. Su facilidad de aplicación y método no invasivo lo hacen especialmente útil para detectar alteraciones en el ritmo y la forma del pulso cardíaco, facilitando el diagnóstico de condiciones como arritmias, hipertensión y enfermedades isquémicas. Una interpretación precisa de estas señales es fundamental, especialmente en situaciones de alto riesgo, donde la identificación temprana de anomalías puede evitar complicaciones graves y, en muchos casos, salvar vidas.
</p>

Este informe examina los métodos contemporáneos para el procesamiento de señales ECG, abarcando tanto enfoques clásicos como sistemas impulsados por aprendizaje automático. Se detallan las etapas esenciales en el tratamiento de la señal y se analizan las técnicas utilizadas para implementarlas en sistemas de monitoreo en tiempo real, ofreciendo una visión completa sobre el estado actual y las posibles innovaciones futuras en el análisis automatizado de ECG con fines diagnósticos.


## Objetivos <a name="id2"></a>
* Aplicar ecg_clean() para preprocesar y limpiar la señal ECG.
* Utilizar ecg_analyze() para extraer características clave de la señal ECG.
* Integrar preprocesamiento y análisis mediante ecg_process().
* Evaluar la efectividad de Neurokit2 comparado con otras herramientas de procesamiento ECG.
* Desarrollar habilidades prácticas en el análisis de señales biomédicas utilizando Python.

## Metodología <a name="id3"></a>
<p style="text-align: justify;"> 

En este laboratorio se empleó la biblioteca "Neurokit2" en Python, utilizando funciones específicas que facilitan el trabajo del programador. Primero, se usará la función ecg_clean(), la cual elimina el ruido de la señal para mejorar su precisión.

Luego, se aplicará la función ecg_peaks(), que, de acuerdo con la documentación, convierte los datos de una lista en un dataframe que muestra la ubicación de los picos R, marcados según el número de muestra analizado.

Después, se usará la función ecg_rate(), la cual calcula la frecuencia cardíaca basándose en el número de muestra de la señal.

Finalmente, el proceso se divide en dos secciones para comparar las gráficas finales y su presentación. La diferencia es que una sección utiliza la función ecg_quality, lo que permite obtener una visualización mejorada y distinta en los resultados.

## Resultados: <a name="id4"></a>



## Discusión <a name="id5"></a>

## Conclusión <a name="id6"></a>



## Bibliografía<a name="id7"></a>



## Referencias
