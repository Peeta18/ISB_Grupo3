# Laboratorio 12: Generación de Edge Impulse 

## Tabla de Contenidos

1. [Corrección del último laboratorio](#1-Corrección-del-último-laboratorio)
2. [Create impulse](#2-Create-impulse)
3. [Parámetros](#3-Parámetros)
4. [Clasificación](#4-Clasificación)
5. [Training output](#5-Training-output)


## 1. Corrección del último laboratorio

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

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/2.jpg?raw=true" alt="Definición de parámetros"><p>
  </p>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/3.jpg?raw=true" alt="Parámetros intermedios"><p>
  </p>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/4.jpg?raw=true" alt="Validación de parámetros"><p>
  </p>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/5.jpg?raw=true" alt="Confirmación final"><p>
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
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/7.jpg?raw=true" alt="Eliminación de datos no válidos"><p>
  Eliminación de datos con duración insuficiente.
  </p>
</div>

---

## 2. Create impulse

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/diseñodeimpulso.png?raw=true" alt="Create impulse"><p>
  Diseño del modelo en Edge Impulse.
  </p>
</div>

---

## 3. Parámetros

Parámetros de **Spectral features** utilizados en el diseño:

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/Spectral%20features.png?raw=true" alt="Parámetros de Spectral features"><p>
  Configuración de Spectral features.
  </p>
</div>

---

## 4. Clasificación

Configuración utilizada para la clasificación de los datos:

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/Classifier.png?raw=true" alt="Clasificación"><p>
  Parámetros del clasificador en Edge Impulse.
  </p>
</div>

---

## 5. Training output

Resultados del entrenamiento obtenidos:

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/traininoutput.png?raw=true" alt="Training output"><p>
  Resultados iniciales del entrenamiento.
  </p>
</div>

<div align="center">
  <img src="https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/Lab12_Generacion_Impulso_Edge_Impulse%20/Italo/Imagenes/traininoutput2.png?raw=true" alt="Training output adicional"><p>
  Resultados adicionales del entrenamiento.
  </p>
</div>
