# LAB 9: PROCESAMIENTO DE SEÑALES EMG

#### **Tabla de Contenido**
1. [Introducción](#introduccion)
2. [Objetivos](#objetivos)
3. [Materiales](#materiales)
4. [Procedimiento](#procedimiento)
5. [Resultados](#resultados)
6. [Discusión](#discusion)
7. [Conclusiones](#conclusiones)
8. [Bibliografía](#bibliografia)

## Introducción

La electromiografía de superficie (sEMG) es una técnica de registro que permite analizar la actividad eléctrica de los músculos a través de la piel, proporcionando una herramienta no invasiva para el estudio de los procesos neuromusculares. Su aplicación es especialmente relevante en el ámbito de la rehabilitación y la detección de condiciones musculares, como la sarcopenia. Según estudios recientes, las señales de sEMG pueden revelar cambios en la función neuromuscular asociados al envejecimiento y a la disminución de masa muscular, característicos de esta condición. Esta tecnología también ha mostrado potencial para el desarrollo de algoritmos de aprendizaje automático que ayudan en la clasificación y diagnóstico de estas condiciones en poblaciones mayores, permitiendo enfoques más precisos y personalizados en la atención clínica&#8203;:contentReference[oaicite:0]{index=0}.

La extracción de características de las señales sEMG incluye el uso de transformadas y análisis de la entropía, que ayudan a identificar patrones específicos de actividad muscular, facilitando así la clasificación de movimientos y el control de dispositivos de asistencia robótica en la rehabilitación. Estos métodos, combinados con técnicas de optimización y algoritmos de aprendizaje automático como las máquinas de soporte vectorial (SVM), permiten reconocer movimientos específicos a partir de patrones de sEMG, mejorando la precisión en aplicaciones de rehabilitación asistida&#8203;:contentReference[oaicite:1]{index=1}&#8203;:contentReference[oaicite:2]{index=2}.


## Objetivos <a name="objetivos"></a>
- Diseñar un filtro adecuado para señales EMG utilizando técnicas avanzadas.
- Extraer y analizar características relevantes de señales EMG, aplicando métodos de normalización y cálculo de parámetros.

## Materiales <a name="materiales"></a>
| Material | Cantidad |
|----------|----------|
| Software de procesamiento de datos (*Python*) | N.A |

## Procedimiento <a name="procedimiento"></a>

El procesamiento de señales EMG se llevó a cabo en las siguientes etapas, con el objetivo de eliminar el ruido y extraer características representativas de la actividad muscular.

### 1. Filtrado de la Señal EMG

En primer lugar, se aplicó un filtro Notch para eliminar el ruido de red (frecuencias entre 59 y 61 Hz), comúnmente introducido por la interferencia eléctrica. Esto permitió limpiar la señal de estos componentes de baja frecuencia. Posteriormente, se aplicó un filtro Pasa Banda para conservar únicamente las frecuencias relevantes de la señal EMG, en el rango de 10 a 490 Hz. Este filtro ayudó a eliminar componentes de alta frecuencia no relacionados con la actividad muscular.

### 2. Visualización de la Señal EMG Cruda

Se realizó una visualización de la señal EMG cruda, lo cual permitió observar la señal antes del procesamiento. Esto fue importante para evaluar la presencia inicial de ruido y posibles artefactos en la señal.

### 3. Extracción de Características

Para el análisis de la actividad muscular, se realizó una extracción de características en los dominios de tiempo, frecuencia y tiempo-frecuencia. Estas características incluyeron:
- **Características de tiempo**: como Varianza (VAR), Raíz Cuadrada Media (RMS), Valor Absoluto Medio (MAV), Longitud de Onda (WL), Cruce por Cero (ZC), entre otras.
- **Características de frecuencia**: tales como Mediana de Frecuencia (MDF) y Frecuencia Media (MNF).
- **Características de tiempo-frecuencia**: aplicando técnicas de transformada wavelet para analizar cambios en los diferentes niveles de la señal.

La extracción de estas características proporciona información detallada sobre la intensidad, frecuencia y variabilidad de la señal EMG, lo cual es útil para identificar patrones de actividad muscular.

### 4. Almacenamiento de Características

Finalmente, las características extraídas fueron almacenadas en un archivo CSV. Este paso permite disponer de un registro estructurado de los datos para su posterior análisis y comparación.

## Resultados <a name="resultados"></a>

A continuación se muestra el código implementado para el procesamiento de la señal EMG y la extracción de características. En cada etapa del proceso, se agregan los gráficos correspondientes.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import pywt
import math
import os

# Funciones para procesamiento digital de la señal

def notch_filter(x, samplerate, plot=False):
    """
    Aplica un filtro Notch para eliminar frecuencias específicas (59-61 Hz).

    :param x: Señal de entrada.
    :param samplerate: Frecuencia de muestreo.
    :param plot: Si es True, grafica la señal original y filtrada.
    :return: Señal filtrada.
    """
    x = x - np.mean(x)
    low_cutoff_notch = 59 / (samplerate / 2)
    high_cutoff_notch = 61 / (samplerate / 2)
    b, a = signal.butter(4, [low_cutoff_notch, high_cutoff_notch], btype='bandstop')
    x_filt = signal.filtfilt(b, a, x)
    if plot:
        t = np.arange(0, len(x) / samplerate, 1 / samplerate)
        plt.figure(figsize=(12, 4))
        plt.plot(t, x, label='Señal Original')
        plt.plot(t, x_filt, 'k', label='Señal Filtrada')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Amplitud (mV)')
        plt.title('Filtro Notch (59-61 Hz)')
        plt.legend()
        plt.tight_layout()
        plt.show()
    return x_filt

<div align="center"> <img src="(inserta_link_imagen_emg_cruda_aqui)" alt="Señal EMG Cruda"> <p><em>Figura 1: Señal EMG Cruda</em></p> </div>
