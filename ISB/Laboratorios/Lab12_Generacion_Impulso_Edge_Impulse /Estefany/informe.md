
# Laboratorio 12 - Edge impulse
## Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [Marco teórico](#2-marco-teórico)
3. [Objetivos](#3-objetivos)
4. [Corrección del último laboratorio](#1-Corrección-del-último-laboratorio)
5. [Create impulse](#2-Create-impulse)
6. [Parámetros](#3-Parámetros)
7. [Clasificación](#4-Clasificación)
8. [Training output](#5-Training-output)
9. [Referencias](#5-referencias)



## 1. Introducción

El estudio de señales biomédicas, especialmente las obtenidas a través de la electrocardiografía (ECG), es esencial en el campo de la salud, ya que permite la detección temprana de enfermedades cardiovasculares y el seguimiento continuo de los estados fisiológicos. Este proyecto se centra en el análisis y procesamiento avanzado de señales ECG, aprovechando herramientas innovadoras de aprendizaje automático como Edge Impulse, para desarrollar soluciones precisas y eficientes en el ámbito médico.[1]


## 2. Marco teórico

- Señales de ECG
El electrocardiograma (ECG) es una representación gráfica de la actividad eléctrica del corazón, producida por los procesos de despolarización y repolarización de las células cardíacas. Esta señal contiene información esencial para diagnosticar diversas anomalías cardíacas, como arritmias, bloqueos de conducción o alteraciones en los ritmos cardíacos. Su análisis permite realizar una evaluación precisa de la función cardíaca y es fundamental para la toma de decisiones clínicas en cardiología.

- Edge Impulse
Edge Impulse es una plataforma innovadora diseñada para facilitar el desarrollo y entrenamiento de modelos de aprendizaje automático optimizados para dispositivos embebidos. Proporciona un conjunto completo de herramientas que abarca desde la adquisición y preprocesamiento de datos hasta el diseño e implementación de modelos personalizados para aplicaciones específicas. Gracias a su capacidad de integración con microcontroladores, sensores y otros dispositivos IoT, Edge Impulse se posiciona como una solución ideal para aplicaciones en tiempo real, como la monitorización médica. En este proyecto, la plataforma se utilizó para gestionar el flujo completo de trabajo: desde la carga y procesamiento de señales de ECG hasta el entrenamiento de un modelo optimizado para la detección de patrones cardíacos.

## 3. Objetivos
1. **Procesamiento y análisis de señales biomédicas:**  Adquirir y organizar señales biomédicas de ECG en diferentes estados fisiológicos, aplicando técnicas adecuadas para su análisis.  

2. **Uso de herramientas de aprendizaje automático:**  Subir los datos a Edge Impulse para explorar su aplicación en el desarrollo de modelos de aprendizaje automático.

## 4. Corrección del último laboratorio

Se realizaron las correcciones necesarias para garantizar que los datos sean compatibles con Edge Impulse. A continuación, se describen los pasos realizados:

### Paso 1: Seleccionar el archivo para configurar el CSV Wizard

En este paso, se seleccionó el archivo correspondiente y se configuró el **CSV Wizard** para dar formato a los datos de entrada, asegurando que sean compatibles con Edge Impulse.

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/1.jpg?raw=true" alt="Configuración del CSV Wizard"><p>
  Configuración inicial en el CSV Wizard.
  </p>
</div>

---

### Paso 2: Definir los parámetros de configuración

Se realizaron las configuraciones principales utilizando las herramientas de Edge Impulse para ajustar el formato y las especificaciones de los datos.

#### a. Configurar los parámetros iniciales
<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Estefany/A.%20Configurr%20parametros%20inciales.png"><p>
  Selección de parámetros iniciales.
  </p>
</div>

#### b. Ajuste fino de los parámetros intermedios
<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/3.jpg?raw=true" alt="Parámetros intermedios"><p>
  Ajuste de parámetros intermedios para garantizar la correcta lectura de los datos.
  </p>
</div>

#### c. Validación de parámetros
<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Estefany/C.validaci%C3%B3n%20.png"><p>
  Confirmación y validación de los parámetros configurados.
  </p>
</div>

#### d. Confirmación final
<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Estefany/D.%20confirmacion%20final.png" alt="Confirmación final"><p>
  Vista previa y confirmación final de los datos configurados.
  </p>
</div>

---

### Paso 3: Subir la data y dividirla entre Training y Testing

Se cargaron los datos procesados en Edge Impulse y se dividieron en **Training** y **Testing**, asignando el 80% para entrenamiento y el 20% para pruebas.

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/6.jpg?raw=true" alt="Subir y dividir la data"><p>
  Carga de los datos y división entre Training y Testing.
  </p>
</div>

---

### Paso 4: Eliminar datos que no cumplen con los requisitos

Finalmente, se eliminaron los datos que no cumplían con los requisitos, como tener una duración mínima de 5 segundos. Este paso es crucial para asegurar que los datos sean aptos para el entrenamiento del modelo.

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Estefany/paso%204.png"><p>
  Eliminación de datos con duración insuficiente.
  </p>
</div>

---

## 5. Create impulse

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Estefany/2.%20Create%20impulse.png"><p>
  Diseño del modelo en Edge Impulse.
  </p>
</div>

---

## 6. Parámetros

Parámetros de **Spectral features** utilizados en el diseño:

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Estefany/3.%20spectral%20features.png"><p>
  Configuración de Spectral features.
  </p>
</div>

---

## 7. Clasificación

Configuración utilizada para la clasificación de los datos:

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Estefany/parametors.png"><p>
  Parámetros del clasificador en Edge Impulse.
  </p>
</div>

---

## 8. Training output

Resultados del entrenamiento obtenidos:

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Estefany/resultados.png"><p>
  Resultados iniciales del entrenamiento.
  </p>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/traininoutput2.png?raw=true" alt="Training output adicional"><p>
  Resultados adicionales del entrenamiento.
  </p>
</div>








  ## 9. Referencias
1. Smith, J., & Brown, P. (2022). Machine Learning Applications in Biomedical Signal Processing. Academic Press.
