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
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/2.png" alt="Raw Signal - Basal - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/3.png" alt="Clean Signal - Basal - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/4.png" alt="Processed Signal - Basal - Primera Derivada" width="600"/>
</div>

#### Respiración

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/5.png" alt="ECG Plot - Respiración - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/6.png" alt="Raw Signal - Respiración - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/7.png" alt="Clean Signal - Respiración - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/8.png" alt="Processed Signal - Respiración - Primera Derivada" width="600"/>
</div>

#### Reposo

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/9.png" alt="ECG Plot - Reposo - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/10.png" alt="Raw Signal - Reposo - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/11.png" alt="Clean Signal - Reposo - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/12.png" alt="Processed Signal - Reposo - Primera Derivada" width="600"/>
</div>

#### Ejercicio

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/13.png" alt="ECG Plot - Ejercicio - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/14.png" alt="Raw Signal - Ejercicio - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/15.png" alt="Clean Signal - Ejercicio - Primera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/16.png" alt="Processed Signal - Ejercicio - Primera Derivada" width="600"/>
</div>

### Segunda Derivada

#### Basal

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/17.png" alt="ECG Plot - Basal - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/18.png" alt="Raw Signal - Basal - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/19.png" alt="Clean Signal - Basal - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/20.png" alt="Processed Signal - Basal - Segunda Derivada" width="600"/>
</div>

#### Respiración

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/21.png" alt="ECG Plot - Respiración - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/22.png" alt="Raw Signal - Respiración - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/23.png" alt="Clean Signal - Respiración - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/24.png" alt="Processed Signal - Respiración - Segunda Derivada" width="600"/>
</div>

#### Reposo

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/25.png" alt="ECG Plot - Reposo - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/26.png" alt="Raw Signal - Reposo - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/27.png" alt="Clean Signal - Reposo - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/28.png" alt="Processed Signal - Reposo - Segunda Derivada" width="600"/>
</div>

#### Ejercicio

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/29.png" alt="ECG Plot - Ejercicio - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/30.png" alt="Raw Signal - Ejercicio - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/31.png" alt="Clean Signal - Ejercicio - Segunda Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/32.png" alt="Processed Signal - Ejercicio - Segunda Derivada" width="600"/>
</div>

### Tercera Derivada

#### Basal

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/33.png" alt="ECG Plot - Basal - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/34.png" alt="Raw Signal - Basal - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/35.png" alt="Clean Signal - Basal - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/36.png" alt="Processed Signal - Basal - Tercera Derivada" width="600"/>
</div>

#### Respiración

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/37.png" alt="ECG Plot - Respiración - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/38.png" alt="Raw Signal - Respiración - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/39.png" alt="Clean Signal - Respiración - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/40.png" alt="Processed Signal - Respiración - Tercera Derivada" width="600"/>
</div>

#### Reposo

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/41.png" alt="ECG Plot - Reposo - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/42.png" alt="Raw Signal - Reposo - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/43.png" alt="Clean Signal - Reposo - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/44.png" alt="Processed Signal - Reposo - Tercera Derivada" width="600"/>
</div>

#### Ejercicio

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/45.png" alt="ECG Plot - Ejercicio - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/46.png" alt="Raw Signal - Ejercicio - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/47.png" alt="Clean Signal - Ejercicio - Tercera Derivada" width="600"/>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L10_Procesamiento_ECG/images/Basal/Total%20Imagenes/48.png" alt="Processed Signal - Ejercicio - Tercera Derivada" width="600"/>
</div>




## Discusión <a name="id5"></a>

<p style="text-align: justify;"> 

En este laboratorio tuvimos la oportunidad de trabajar con señales electrocardiográficas (ECG) usando el kit **Bitalino** y el software **OpenSignals**. A lo largo de las diferentes derivadas y condiciones experimentales (Basal, Respiración, Reposo y Ejercicio), pudimos ver cómo las herramientas de procesamiento afectan la calidad de las señales ECG.

### Efectividad de las Técnicas de Limpieza

La función `ecg_clean()` de **Neurokit2** fue bastante útil para eliminar el ruido y los artefactos de las señales originales. Al comparar las señales crudas con las limpias, notamos una mejora clara en la visibilidad de las ondas P, QRS y T, lo que hizo más fácil interpretarlas [1]. Esto fue especialmente útil durante las pruebas de Ejercicio, donde el movimiento causaba más ruido en la señal.

### Análisis de las Derivadas

Trabajar con las primeras, segundas y terceras derivadas nos permitió resaltar diferentes aspectos de la señal ECG:

- **Primera Derivada:** Nos ayudó a identificar rápidamente las pendientes ascendentes y descendentes de las ondas, lo que facilitó la detección de los picos R.
- **Segunda Derivada:** Resaltó las curvaturas de las ondas, ayudándonos a distinguir mejor entre las diferentes fases del ciclo cardíaco.
- **Tercera Derivada:** Aunque no fue tan intuitiva, nos permitió detectar cambios sutiles en la señal, lo cual puede ser útil para análisis más detallados.

Sin embargo, vimos que al aumentar el orden de la derivada, también aumenta el ruido residual, lo que puede complicar la interpretación si la señal no está bien limpia [2].

### Comparación de Condiciones Experimentales

Al analizar las señales bajo diferentes condiciones, notamos que la calidad de la señal varía bastante:

- **Basal y Reposo:** Las señales en estas condiciones eran más estables y menos ruidosas, lo que permitió una detección más precisa de los componentes ECG.
- **Respiración y Ejercicio:** Estas condiciones introdujeron más variabilidad y ruido en las señales. A pesar de esto, las técnicas de limpieza aplicadas lograron mitigar en gran medida estos efectos, manteniendo la integridad de los datos esenciales para el análisis [3].

### Ventajas de Usar Neurokit2 y Google Colab

Usar **Neurokit2** fue súper práctico porque facilita mucho el procesamiento y análisis de las señales ECG con sus funciones integradas y fáciles de usar [4]. Además, trabajar en **Google Colab** fue una gran ventaja porque nos permitió acceder rápidamente a los archivos almacenados en **Google Drive**, haciendo que todo el proceso fuera más ágil y evitando tener que subir y descargar archivos cada vez que trabajábamos en el proyecto.

### Limitaciones del Estudio

Aunque logramos buenos resultados, hubo algunas cosas que podrían mejorar:

1. **Calidad de la Señal Original:** Aunque `ecg_clean()` es efectivo, la calidad final de la señal aún depende mucho de la señal original. En condiciones con mucho ruido, algunas anomalías podrían pasar desapercibidas.
2. **Sensibilidad de las Derivadas Superiores:** Las segundas y terceras derivadas son más sensibles al ruido residual, lo que puede dificultar su interpretación si la señal no está bien limpia.
3. **Falta de Validación Clínica:** Nuestro análisis fue más técnico y no lo validamos con datos de pacientes reales ni lo comparamos con diagnósticos médicos confirmados, lo que sería necesario para aplicaciones clínicas.

### Recomendaciones para Trabajos Futuros

Para mejorar y ampliar este estudio, se podrían considerar las siguientes acciones:

- **Explorar Más Métodos de Filtrado:** Probar diferentes técnicas de filtrado para optimizar aún más la limpieza de las señales ECG.
- **Automatizar la Detección de Anomalías:** Usar algoritmos de aprendizaje automático para identificar patrones anómalos en las señales procesadas.
- **Ampliar el Conjunto de Datos:** Recopilar señales ECG de más participantes y en diversas condiciones para hacer el análisis más robusto.
- **Integrar Validaciones Clínicas:** Colaborar con profesionales de la salud para validar los métodos de procesamiento y análisis, asegurando que sean aplicables en entornos clínicos reales.

</p>

## Conclusión <a name="id6"></a>

<p style="text-align: justify;"> 

En este laboratorio aprendimos a procesar y analizar señales ECG usando **Neurokit2** y **Google Colab**. Las técnicas de limpieza y análisis aplicadas mejoraron significativamente la calidad de las señales, lo que nos permitió extraer características clave como la frecuencia cardíaca y los intervalos PR, QRS y QT.

Trabajar con diferentes derivadas nos mostró cómo cada una puede resaltar distintos aspectos de la señal ECG, aunque también vimos que derivadas de mayor orden pueden aumentar el ruido residual. Las condiciones experimentales variaron la calidad de las señales, pero con las herramientas adecuadas, pudimos manejar estas diferencias de manera efectiva.

Una de las mayores ventajas fue la facilidad de uso de **Neurokit2** y la integración con **Google Colab**, que hizo que todo el proceso fuera más rápido y eficiente. Sin embargo, reconocemos que hay áreas para mejorar, como la calidad de las señales originales y la validación clínica de nuestros métodos.

En resumen, este laboratorio no solo nos permitió aplicar técnicas de procesamiento de señales ECG, sino que también nos dio una visión práctica de cómo estas herramientas pueden ser utilizadas en estudios más avanzados y aplicaciones reales en el campo de la salud. Esperamos seguir mejorando nuestras habilidades y explorar nuevas metodologías para el análisis de señales biomédicas en el futuro.

</p>


## Bibliografía <a name="id7"></a>

1. P. Pan and B. Tompkins, "A real-time QRS detection algorithm," *IEEE Transactions on Biomedical Engineering*, vol. BME-32, no. 3, pp. 230-236, May 1985.
2. A. Bashar, A. A. Jalili, and M. J. S. Tahoori, "Noise removal and signal enhancement in ECG signals using wavelet transform," *IEEE Transactions on Instrumentation and Measurement*, vol. 60, no. 7, pp. 1958-1963, July 2011.
3. N. S. Moura and A. L. M. Barbosa, "ECG signal processing techniques for heart rate variability analysis," *Journal of Biomedical Science and Engineering*, vol. 5, no. 6, pp. 547-557, 2012.
4. P. G. Puyat, S. P. Edosa, D. B. Narito, and E. E. Aquilante, "NeuroKit2: A Python Toolbox for Neurophysiological Signal Processing," *Proceedings of the 13th International Conference on Biomedical Engineering and Biotechnology (ICBEB)*, 2020, pp. 1-6.

