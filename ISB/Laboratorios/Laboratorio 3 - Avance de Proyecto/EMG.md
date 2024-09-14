# LABORATORIO 3: USO DE BITalino PARA EMG Y ECG

## Tabla de contenidos

1. [Objetivos](#objetivos)
2. [Materiales y equipos](#materiales-y-equipos)
3. [Resultados](#resultados)
   - [Conexión usada](#conexión-usada)
   - [Video de la señal y ploteo en Opensignal](#video-de-la-señal-y-ploteo-en-opensignal)
   - [Ploteo de la señal en Python](#ploteo-de-la-señal-en-python)
4. [Archivos](#archivos)

## Objetivos

- Adquirir señales biomédicas de EMG y ECG.
- Hacer una correcta configuración de BITalino.
- Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolution.

## Materiales y equipos

          | Modelo         | Descripción    | Cantidad |
          | -------------- | -------------- | -------- |
          | (R)EVOLUTION   | Kit BITalino   | 1        |
          | -              | Laptop         | 1        |

## Resultados

### Conexión usada

Se utilizó la conexión EMG en la placa BITalino utilizando el sensor EMG de 3 electrodos como se muestra a continuación.

![Conexión EMG](link-to-image)

### Video de la señal y ploteo en Opensignal

#### PRUEBA 1

En la prueba 1 se tomó señales del reposo y contracción del dedo pulgar, teniendo la conexión de tierra en el dorso de la mano.

![Video 1](link-to-video)

#### PRUEBA 2

En la prueba 2 se tomó señales de reposo y contracción del bíceps, teniendo la conexión de tierra a la altura de la muñeca.

![Video 2](link-to-video)

#### PRUEBA 3

En la prueba 3 se tomó señales de reposo y contracción del músculo gastrocnemio, teniendo la conexión de tierra en la parte anterior de la tibia.

![Video 3](link-to-video)

### Ploteo de la señal en Python

#### Señal del dedo en reposo

![Señal de dedo en reposo](link-to-image)

#### Señal de bíceps en contracción

![Señal de bíceps en contracción](link-to-image)

#### Señal de gastrocnemio en contracción

![Señal de gastrocnemio en contracción](link-to-image)

## Archivos

- [Documentos (.txt)](link-to-files)
- [Programa de ploteo (Jupyter Notebook)](link-to-jupyter-notebook)


