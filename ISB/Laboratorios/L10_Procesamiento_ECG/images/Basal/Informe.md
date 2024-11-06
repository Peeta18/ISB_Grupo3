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

En este laboratorio utilizamos la biblioteca **Neurokit2** en Python para procesar las señales ECG obtenidas. A continuación, se detalla el paso a paso que seguimos:

1. **Adquisición de la Señal ECG**  
   Las señales ECG fueron capturadas en el laboratorio 5 de este curso usando el kit **Bitalino** y el software **OpenSignals**. Estos dispositivos nos permitieron registrar la actividad eléctrica del corazón de manera precisa y eficiente.

2. **Conversión y Almacenamiento de Datos**  
   Los archivos de las señales ECG se obtuvieron en formato **.txt**. Para facilitar su manejo y análisis, convertimos estos archivos a formato **.csv**. Luego, subimos los archivos convertidos a **Google Drive**. Esto nos permitió acceder a ellos rápidamente desde **Google Colab** sin tener que subir los archivos manualmente cada vez que trabajábamos en el proyecto.

3. **Visualización Inicial de la Señal**  
   Antes de procesar las señales, graficamos las señales ECG en el dominio del tiempo para tener una primera impresión de su calidad. Esta visualización nos ayudó a identificar posibles ruidos o artefactos y a decidir si era necesario aplicar técnicas de filtrado para mejorar la señal.

4. **Preprocesamiento de la Señal ECG**  
   Utilizamos la función `ecg_clean()` de Neurokit2 para limpiar la señal ECG. Esta función elimina ruidos y artefactos, lo que nos permitió obtener una señal más clara y precisa para el análisis posterior.

5. **Análisis de la Señal ECG**  
   Después de limpiar la señal, aplicamos la función `ecg_analyze()` para extraer características importantes de la señal, como la frecuencia cardíaca y los intervalos PR, QRS y QT. Estas características son esenciales para evaluar el estado cardíaco y detectar posibles anomalías.

6. **Procesamiento Integrado de la Señal ECG**  
   Finalmente, utilizamos la función `ecg_process()` para realizar tanto el preprocesamiento como el análisis de la señal ECG en un solo paso. Esto hizo que el flujo de trabajo fuera más eficiente y nos permitió obtener resultados de manera más rápida.


</p>




## Discusión <a name="id5"></a>

## Conclusión <a name="id6"></a>



## Bibliografía<a name="id7"></a>



## Referencias
