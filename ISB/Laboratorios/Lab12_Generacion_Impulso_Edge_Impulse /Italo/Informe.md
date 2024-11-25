# Laboratorio 12: Generación de Edge Impulse 

## Tabla de Contenidos

1. [Corrección del último laboratorio](#1-Corrección-del-último-laboratorio)
2. [Definir parámetros de configuración](#2-Definir-parámetros-de-configuración)
3. [Subir y dividir la data](#3-Subir-y-dividir-la-data)
4. [Eliminación de datos no válidos](#4-Eliminación-de-datos-no-válidos)


## 1. Corrección del último laboratorio

Se realizaron los pasos iniciales para corregir los formatos necesarios y asegurar que los datos puedan ser procesados por Edge Impulse. 

### Paso 1: Seleccionar el archivo para configurar el CSV Wizard

En este paso, se seleccionó el archivo correspondiente y se configuró el **CSV Wizard** para dar formato a los datos de entrada, asegurando que sean compatibles con Edge Impulse.

<div align="center">
  <img src="./Imagen/1.jpg" alt="Configuración del CSV Wizard"><p>
  Configuración inicial en el CSV Wizard.
  </p>
</div>

---

## 2. Definir parámetros de configuración

En esta sección, se definieron los parámetros necesarios para preparar los datos y configurar Edge Impulse correctamente. Esto se realizó utilizando las imágenes del diseño y los valores adecuados para cada configuración.

### Paso 2: Configuración de parámetros
Se realizaron las configuraciones principales utilizando las herramientas de Edge Impulse para ajustar el formato y las especificaciones de los datos.

#### a. Configurar los parámetros iniciales
<div align="center">
  <img src="./Imagen/2.jpg" alt="Definición de parámetros"><p>
  Selección de parámetros iniciales.
  </p>
</div>

#### b. Ajuste fino de los parámetros intermedios
<div align="center">
  <img src="./Imagen/3.jpg" alt="Parámetros intermedios"><p>
  Ajuste de parámetros intermedios para garantizar la correcta lectura de los datos.
  </p>
</div>

#### c. Validación de parámetros
<div align="center">
  <img src="./Imagen/4.jpg" alt="Validación de parámetros"><p>
  Confirmación y validación de los parámetros configurados.
  </p>
</div>

#### d. Confirmación final
<div align="center">
  <img src="./Imagen/5.jpg" alt="Confirmación final"><p>
  Vista previa y confirmación final de los datos configurados.
  </p>
</div>

---

## 3. Subir y dividir la data

Se procedió a cargar los datos procesados en Edge Impulse y dividirlos en **Training** y **Testing**, asignando el 80% para entrenamiento y el 20% para pruebas.

<div align="center">
  <img src="./Imagen/6.jpg" alt="Subir y dividir la data"><p>
  Carga de los datos y división entre Training y Testing.
  </p>
</div>

---

## 4. Eliminación de datos no válidos

Finalmente, se eliminaron los datos que no cumplían con los requisitos, como tener una duración mínima de 5 segundos. Este paso es crucial para asegurar que los datos sean aptos para el entrenamiento del modelo.

<div align="center">
  <img src="./Imagen/7.jpg" alt="Eliminación de datos no válidos"><p>
  Eliminación de datos con duración insuficiente.
  </p>
</div>

---

Con estos pasos, se completaron las correcciones necesarias del laboratorio previo y se configuró todo para el uso en Edge Impulse. Este flujo garantiza datos limpios y formateados correctamente para el modelo de entrenamiento.
