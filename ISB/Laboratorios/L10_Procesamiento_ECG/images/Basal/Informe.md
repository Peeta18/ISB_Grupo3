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

## Resultados <a name="id4"></a>

### Primera Derivada

#### Basal

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/1.png" alt="ECG Plot - Basal - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_raw_basal_primera_derivada.png" alt="Raw Signal - Basal - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_clean_basal_primera_derivada.png" alt="Clean Signal - Basal - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_process_basal_primera_derivada.png" alt="Processed Signal - Basal - Primera Derivada" width="600"/>
</div>

#### Respiración

<div align="center">
  <img src="https://link_to_your_image_ecg_plot_respiracion_primera_derivada.png" alt="ECG Plot - Respiración - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_raw_respiracion_primera_derivada.png" alt="Raw Signal - Respiración - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_clean_respiracion_primera_derivada.png" alt="Clean Signal - Respiración - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_process_respiracion_primera_derivada.png" alt="Processed Signal - Respiración - Primera Derivada" width="600"/>
</div>

#### Reposo

<div align="center">
  <img src="https://link_to_your_image_ecg_plot_reposo_primera_derivada.png" alt="ECG Plot - Reposo - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_raw_reposo_primera_derivada.png" alt="Raw Signal - Reposo - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_clean_reposo_primera_derivada.png" alt="Clean Signal - Reposo - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_process_reposo_primera_derivada.png" alt="Processed Signal - Reposo - Primera Derivada" width="600"/>
</div>

#### Ejercicio

<div align="center">
  <img src="https://link_to_your_image_ecg_plot_ejercicio_primera_derivada.png" alt="ECG Plot - Ejercicio - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_raw_ejercicio_primera_derivada.png" alt="Raw Signal - Ejercicio - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_clean_ejercicio_primera_derivada.png" alt="Clean Signal - Ejercicio - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_process_ejercicio_primera_derivada.png" alt="Processed Signal - Ejercicio - Primera Derivada" width="600"/>
</div>

### Segunda Derivada

#### Basal

<div align="center">
  <img src="https://link_to_your_image_ecg_plot_basal_segunda_derivada.png" alt="ECG Plot - Basal - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_raw_basal_segunda_derivada.png" alt="Raw Signal - Basal - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_clean_basal_segunda_derivada.png" alt="Clean Signal - Basal - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_process_basal_segunda_derivada.png" alt="Processed Signal - Basal - Segunda Derivada" width="600"/>
</div>

#### Respiración

<div align="center">
  <img src="https://link_to_your_image_ecg_plot_respiracion_segunda_derivada.png" alt="ECG Plot - Respiración - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_raw_respiracion_segunda_derivada.png" alt="Raw Signal - Respiración - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_clean_respiracion_segunda_derivada.png" alt="Clean Signal - Respiración - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_process_respiracion_segunda_derivada.png" alt="Processed Signal - Respiración - Segunda Derivada" width="600"/>
</div>

#### Reposo

<div align="center">
  <img src="https://link_to_your_image_ecg_plot_reposo_segunda_derivada.png" alt="ECG Plot - Reposo - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_raw_reposo_segunda_derivada.png" alt="Raw Signal - Reposo - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_clean_reposo_segunda_derivada.png" alt="Clean Signal - Reposo - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_process_reposo_segunda_derivada.png" alt="Processed Signal - Reposo - Segunda Derivada" width="600"/>
</div>

#### Ejercicio

<div align="center">
  <img src="https://link_to_your_image_ecg_plot_ejercicio_segunda_derivada.png" alt="ECG Plot - Ejercicio - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_raw_ejercicio_segunda_derivada.png" alt="Raw Signal - Ejercicio - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_clean_ejercicio_segunda_derivada.png" alt="Clean Signal - Ejercicio - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_process_ejercicio_segunda_derivada.png" alt="Processed Signal - Ejercicio - Segunda Derivada" width="600"/>
</div>

### Tercera Derivada

#### Basal

<div align="center">
  <img src="https://link_to_your_image_ecg_plot_basal_tercera_derivada.png" alt="ECG Plot - Basal - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_raw_basal_tercera_derivada.png" alt="Raw Signal - Basal - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_clean_basal_tercera_derivada.png" alt="Clean Signal - Basal - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_process_basal_tercera_derivada.png" alt="Processed Signal - Basal - Tercera Derivada" width="600"/>
</div>

#### Respiración

<div align="center">
  <img src="https://link_to_your_image_ecg_plot_respiracion_tercera_derivada.png" alt="ECG Plot - Respiración - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_raw_respiracion_tercera_derivada.png" alt="Raw Signal - Respiración - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_clean_respiracion_tercera_derivada.png" alt="Clean Signal - Respiración - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_process_respiracion_tercera_derivada.png" alt="Processed Signal - Respiración - Tercera Derivada" width="600"/>
</div>

#### Reposo

<div align="center">
  <img src="https://link_to_your_image_ecg_plot_reposo_tercera_derivada.png" alt="ECG Plot - Reposo - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_raw_reposo_tercera_derivada.png" alt="Raw Signal - Reposo - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_clean_reposo_tercera_derivada.png" alt="Clean Signal - Reposo - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_process_reposo_tercera_derivada.png" alt="Processed Signal - Reposo - Tercera Derivada" width="600"/>
</div>

#### Ejercicio

<div align="center">
  <img src="https://link_to_your_image_ecg_plot_ejercicio_tercera_derivada.png" alt="ECG Plot - Ejercicio - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_raw_ejercicio_tercera_derivada.png" alt="Raw Signal - Ejercicio - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_clean_ejercicio_tercera_derivada.png" alt="Clean Signal - Ejercicio - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://link_to_your_image_process_ejercicio_tercera_derivada.png" alt="Processed Signal - Ejercicio - Tercera Derivada" width="600"/>
</div>



## Discusión <a name="id5"></a>

## Conclusión <a name="id6"></a>



## Bibliografía<a name="id7"></a>



## Referencias
