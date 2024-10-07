# Laboratorio 7 - Introducción a Señales Biomédicas
Martin Elias Pino Aguilar

Se utilizaron los siguientes filtros para el procesamiento de las señales EMG y ECG:

## Filtro FIR Pasa Alta fc = 20 Hz
Se utilizó este filtro para atenuar las frecuencias menores a 20 Hz, esto ayuda a eliminar el ruido de baja frecuencia y artefactos que pueden contaminar la señal EMG. Esto incluye ruido causado por el movimiento, que a menudo está presentes en las mediciones.[1] 

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Magnitud**                  |![Magnitud](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/Highpass_Filter_20_Hz_Magnitude.png)|
| **Fase**                  |![Fase](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/HighpassFilter20Hz-Phase.png)|
| **Polos y ceros**                  |![zplane](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/HighpassFilter20Hz-zplane.png)|

## EMG: Filtro IIR Pasa Baja fc = 450 Hz
Se utilizaron los filtros pasa baja para atenuar las frecuencias mayores a 450 Hz, esto ayuda a atenuar el ruido o artefactos interferieren con la señal EMG. Estos pueden ser el ruido eléctrico del entorno y otras fuentes que puedan estar presentes en la adquisición de datos. [1]

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Magnitud**                  |![Magnitud](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/LowpassFilter450Hz-Magnitude.png)|
| **Fase**                  |![Fase](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/LowpassFilter450Hz-Phase.png)|
| **Polos y ceros**                  |![zplane](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/LowpassFilter450Hz-zplane.png)|

## ECG: Filtro IIR Pasa Baja fc = 150 Hz

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Magnitud**                  |![Magnitud](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/LowpassFilter150Hz-Magnitude.png)|
| **Fase**                  |![Fase](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/LowpassFilter150Hz-Phase.png)|
| **Polos y ceros**                  |![zplane](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/LowpassFilter150Hz-zplane.png)|

## Filtro Notch Rechaza Banda fc = 50-60 Hz
Se utilizó este filtro para atenuar las frecuencias entre a 50 y 60 Hz, esto debido a la interferencia de la línea eléctrica que podría existir en las mediciones de ECG en interiores. [2]
| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Magnitud**                  |![Magnitud](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/NotchFilter50-60Hz-Magnitude.png)|
| **Fase**                  |![Fase](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/NotchFilter50-60Hz-Phase.png)|
| **Polos y ceros**                  |![zplane](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/NotchFilter50-60Hz-zplane.png)|


## Señales EMG

### EMG en reposo con filtro pasa alta.
Se observa la atenuación de frecuencias menores a 20 Hz.

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Señal en dominio del tiempo**                  |![Señal](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/EMG_reposo/HighP_EMG_reposo.png)|
| **Señal en dominio de la frecuencia**                  |![Freq](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/EMG_reposo/HighP_EMG_reposo_F.png)|
| **STFT**                  |![stft](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/EMG_reposo/HighP_EMG_reposo_STFT.png)|


### EMG en movimiento voluntario con filtro pasa baja
Se observa la atenuación de frecuencias mayores a 450 Hz.

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Señal en dominio del tiempo**                  |![Señal](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/EMG_voluntario/LowP_EMG_voluntario.png)|
| **Señal en dominio de la frecuencia**                  |![Freq](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/EMG_voluntario/LowP_EMG_voluntario_F.png)|
| **STFT**                  |![stft](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/EMG_voluntario/LowP_EMG_voluntario_STFT.png)|


### EMG en movimiento máximo con filtro notch
| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Señal en dominio del tiempo**                  |![Señal](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/EMG_max/Notch_EMG_max.png)|
| **Señal en dominio de la frecuencia**                  |![Freq](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/EMG_max/Notch_EMG_max_F.png)|
| **STFT**                  |![stft](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/EMG_max/Notch_EMG_max_STFT.png)|

## Señales ECG

### ECG en estado basal con filtro pasa alta
Se observa la atenuación de frecuencias menores a 20 Hz.

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Señal en dominio del tiempo**                  |![Señal](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/ECG_basal/HighP_ECG_basal.png)|
| **Señal en dominio de la frecuencia**                  |![Freq](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/ECG_basal/HighP_ECG_basal_F.png)|
| **STFT**                  |![stft](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/ECG_basal/HighP_ECG_basal_STFT.png)|

### ECG en respiración pausada con filtro pasa baja
Se observa la atenuación de frecuencias mayores a 150 Hz.

| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Señal en dominio del tiempo**                  |![Señal](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/ECG_respiracion/LowP_ECG_respiracion.png)|
| **Señal en dominio de la frecuencia**                  |![Freq](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/ECG_respiracion/LowP_ECG_respiracion_F.png)|
| **STFT**                  |![stft](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/ECG_respiracion/LowP_ECG_respiracion_STFT.png)|

### ECG después del ejercicio con filtro notch
| Análisis                                              | Imagen                                                                                                        |
|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Señal en dominio del tiempo**                  |![Señal](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/ECG_ejercicio/Notch_ECG_ejercicio.png)|
| **Señal en dominio de la frecuencia**                  |![Freq](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/ECG_ejercicio/Notch_ECG_ejercicio_F.png)|
| **STFT**                  |![stft](https://github.com/Peeta18/ISB_Grupo3/blob/main/ISB/Laboratorios/L7_procesamiento_de_señales/Imagenes_Codigo_Elias/Imagenes/ECG_ejercicio/Notch_ECG_ejercicio_STFT.png)|

### Bibliografía
1. De Luca, C. J., Gilmore, L. D., Kuznetsov, M., & Roy, S. H. (2010). Filtering the surface EMG signal: Movement artifact and baseline noise contamination. Journal of biomechanics, 43(8), 1573-1579.
2. Vale-Cardoso, A. S., & Guimarães, H. N. (2009). The effect of 50/60 Hz notch filter application on human and rat ECG recordings. Physiological measurement, 31(1), 45.
