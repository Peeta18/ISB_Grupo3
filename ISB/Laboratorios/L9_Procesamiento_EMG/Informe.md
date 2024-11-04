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

### Señal EMG Cruda

```python
def plot_signal(x, samplerate, chname):
    """
    Grafica la señal EMG cruda.

    :param x: Señal de entrada.
    :param samplerate: Frecuencia de muestreo.
    :param chname: Nombre del canal.
    """
    t = np.arange(0, len(x) / samplerate, 1 / samplerate)
    plt.figure(figsize=(12, 4))
    plt.plot(t, x)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud (mV)')
    plt.title(f'Señal EMG Cruda - {chname}')
    plt.tight_layout()
    plt.show()
```
<div align="center"> <img src="(inserta_link_imagen_emg_cruda_aqui)" alt="Señal EMG Cruda"> <p><em>Figura 1: Señal EMG Cruda</em></p> </div>

```python
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
```
<div align="center"> <img src="(inserta_link_imagen_notch_filter_aqui)" alt="Filtro Notch (59-61 Hz)"> <p><em>Figura 2: Señal después del Filtro Notch (59-61 Hz)</em></p> </div> ```
### Filtro Pasa Banda (10-490 Hz)

```python
def bp_filter(x, low_f, high_f, samplerate, plot=False):
    """
    Aplica un filtro Pasa Banda para mantener frecuencias entre low_f y high_f.
    
    :param x: Señal de entrada.
    :param low_f: Frecuencia de corte baja.
    :param high_f: Frecuencia de corte alta.
    :param samplerate: Frecuencia de muestreo.
    :param plot: Si es True, grafica la señal original y filtrada.
    :return: Señal filtrada.
    """
    nyquist = samplerate / 2
    if high_f >= nyquist:
        print(f"Ajustando high_f de {high_f} Hz a {nyquist - 1} Hz para evitar errores.")
        high_f = nyquist - 1

    low_cutoff_bp = low_f / nyquist
    high_cutoff_bp = high_f / nyquist
    b, a = signal.butter(5, [low_cutoff_bp, high_cutoff_bp], btype='bandpass')
    x_filt = signal.filtfilt(b, a, x)
    if plot:
        t = np.arange(0, len(x) / samplerate, 1 / samplerate)
        plt.figure(figsize=(12, 4))
        plt.plot(t, x, label='Señal Original')
        plt.plot(t, x_filt, 'k', label='Señal Filtrada')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Amplitud (mV)')
        plt.title(f'Filtro Pasa Banda ({low_f}-{high_f} Hz)')
        plt.legend()
        plt.tight_layout()
        plt.show()
    return x_filt

```
<div align="center"> <img src="(inserta_link_imagen_bp_filter_aqui)" alt="Filtro Pasa Banda (10-490 Hz)"> <p><em>Figura 3: Señal después del Filtro Pasa Banda (10-490 Hz)</em></p> </div>
#Señal EMG filtrada

```python
def plot_signal(x, samplerate, chname):
    """
    Grafica la señal EMG filtrada.
    :param x: Señal de entrada.
    :param samplerate: Frecuencia de muestreo.
    :param chname: Nombre del canal.
    """
    t = np.arange(0, len(x) / samplerate, 1 / samplerate)
    plt.figure(figsize=(12, 4))
    plt.plot(t, x)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud (mV)')
    plt.title(f'Señal EMG Filtrada - {chname}')
    plt.tight_layout()
    plt.show()
```
<div align="center"> <img src="(inserta_link_imagen_emg_filtrada_aqui)" alt="Señal EMG Filtrada"> <p><em>Figura 4: Señal EMG Filtrada</em></p> </div>
```

#Extracción de Características
```python
def features_estimation(signal, channel_name, fs, frame, step, plot=False):
    """
    Calcula características en el dominio del tiempo, frecuencia y tiempo-frecuencia de la señal.
    :param signal: Señal EMG filtrada.
    :param channel_name: Nombre del canal.
    :param fs: Frecuencia de muestreo.
    :param frame: Tamaño de la ventana (en muestras).
    :param step: Paso de la ventana (en muestras).
    :param plot: Si es True, grafica las características.
    :return: DataFrame con características y lista de nombres de características.
    """
    features_names = ['VAR', 'RMS', 'IEMG', 'MAV', 'LOG', 'WL', 'ACC', 'DASDV', 'ZC', 'WAMP', 'MYOP', 
                      "FR", "MNP", "TP", "MNF", "MDF", "PKF", "WENT"]
    time_matrix = time_features_estimation(signal, frame, step)
    frequency_matrix = frequency_features_estimation(signal, fs, frame, step)
    time_frequency_matrix = time_frequency_features_estimation(signal, frame, step)
    total_feature_matrix = pd.DataFrame(np.column_stack((time_matrix, frequency_matrix, time_frequency_matrix)), 
                                        columns=features_names)
    print(f'Las características EMG del canal "{channel_name}" fueron extraídas exitosamente.')
    if plot:
        plot_features(signal, channel_name, fs, total_feature_matrix, step)
    return total_feature_matrix, features_names

def time_features_estimation(signal, frame, step):
    """
    Calcula características en el dominio del tiempo utilizando ventana deslizante.
    :param signal: Señal EMG filtrada.
    :param frame: Tamaño de la ventana (en muestras).
    :param step: Paso de la ventana (en muestras).
    :return: Matriz de características de tiempo.
    """
    variance = []
    rms = []
    iemg = []
    mav = []
    log_detector = []
    wl = []
    aac = []
    dasdv = []
    zc = []
    wamp = []
    myop = []
    th = np.mean(signal) + 3 * np.std(signal)
    for i in range(frame, len(signal), step):
        x = signal[i - frame:i]
        variance.append(np.var(x))
        rms.append(np.sqrt(np.mean(x ** 2)))
        iemg.append(np.sum(np.abs(x)))
        mav.append(np.mean(np.abs(x)))
        # Añadir una pequeña constante para evitar log(0)
        log_detector.append(np.exp(np.sum(np.log(np.abs(x) + 1e-10)) / frame))
        wl.append(np.sum(np.abs(np.diff(x))))
        aac.append(np.sum(np.abs(np.diff(x))) / frame)
        dasdv.append(np.sqrt(np.sum(np.diff(x) ** 2) / (frame - 1)))
        zc.append(zcruce(x, th))
        wamp.append(wilson_amplitude(x, th))
        myop.append(myopulse(x, th))
    time_features_matrix = np.column_stack((variance, rms, iemg, mav, log_detector, wl, aac, dasdv, zc, wamp, myop))
    return time_features_matrix

def frequency_features_estimation(signal, fs, frame, step):
    """
    Calcula características en el dominio de la frecuencia utilizando ventana deslizante.
    :param signal: Señal EMG filtrada.
    :param fs: Frecuencia de muestreo.
    :param frame: Tamaño de la ventana (en muestras).
    :param step: Paso de la ventana (en muestras).
    :return: Matriz de características de frecuencia.
    """
    fr = []
    mnp = []
    tot = []
    mnf = []
    mdf = []
    pkf = []
    for i in range(frame, len(signal), step):
        x = signal[i - frame:i]
        frequency, power = spectrum(x, fs)
        fr.append(frequency_ratio(frequency, power))
        mnp.append(np.mean(power))
        tot.append(np.sum(power))
        mnf.append(mean_freq(frequency, power))
        mdf.append(median_freq(frequency, power))
        pkf.append(frequency[np.argmax(power)])
    frequency_features_matrix = np.column_stack((fr, mnp, tot, mnf, mdf, pkf))
    return frequency_features_matrix

def time_frequency_features_estimation(signal, frame, step):
    """
    Calcula características en el dominio tiempo-frecuencia utilizando ventana deslizante.
    :param signal: Señal EMG filtrada.
    :param frame: Tamaño de la ventana (en muestras).
    :param step: Paso de la ventana (en muestras).
    :return: Lista de características de tiempo-frecuencia.
    """
    h_wavelet = []
    for i in range(frame, len(signal), step):
        x = signal[i - frame:i]
        E_a, E = wavelet_energy(x, 'db2', 4)
        E.insert(0, E_a)
        E = np.asarray(E) / 100
        # Evitar log(0) sumando una pequeña constante
        E = np.where(E > 0, E, 1e-10)
        h_wavelet.append(-np.sum(E * np.log2(E)))
    return h_wavelet

def wilson_amplitude(signal, th):
    """
    Calcula la amplitud de Wilson.
    :param signal: Señal EMG filtrada.
    :param th: Umbral para la amplitud.
    :return: Valor de la amplitud de Wilson.
    """
    x = np.abs(np.diff(signal))
    umbral = x >= th
    return np.sum(umbral)

def myopulse(signal, th):
    """
    Calcula la tasa de pulsos mioeléctricos.
    :param signal: Señal EMG filtrada.
    :param th: Umbral para los pulsos.
    :return: Tasa de pulsos mioeléctricos.
    """
    umbral = np.abs(signal) >= th
    return np.sum(umbral) / len(signal)

def spectrum(signal, fs):
    """
    Calcula el espectro de potencia de la señal.
    :param signal: Señal EMG filtrada.
    :param fs: Frecuencia de muestreo.
    :return: Frecuencias y potencia.
    """
    m = len(signal)
    n = next_power_of_2(m)
    y = np.fft.fft(signal, n)
    yh = y[:n // 2]
    fh = (fs / n) * np.arange(0, n // 2)
    power = np.real(yh * np.conj(yh)) / n
    return fh, power

def frequency_ratio(frequency, power):
    """
    Calcula la relación de frecuencia.
    :param frequency: Array de frecuencias.
    :param power: Array de potencia.
    :return: Relación de frecuencia (ULC / UHC).
    """
    power_low = power[(frequency >= 30) & (frequency <= 250)]
    power_high = power[(frequency > 250) & (frequency <= 500)]
    ULC = np.sum(power_low)
    UHC = np.sum(power_high)
    if UHC == 0:
        return 0
    return ULC / UHC

def zcruce(X, th):
    """
    Calcula el número de cruces por cero.
    :param X: Señal EMG filtrada.
    :param th: Umbral para evitar cruces insignificantes.
    :return: Número de cruces por cero.
    """
    crossings = np.where(np.diff(np.signbit(X - th)))[0]
    return len(crossings)

def mean_freq(frequency, power):
    """
    Calcula la frecuencia media.
    :param frequency: Array de frecuencias.
    :param power: Array de potencia.
    :return: Frecuencia media.
    """
    return np.sum(frequency * power) / np.sum(power)

def median_freq(frequency, power):
    """
    Calcula la frecuencia mediana.
    :param frequency: Array de frecuencias.
    :param power: Array de potencia.
    :return: Frecuencia mediana.
    """
    cumulative_power = np.cumsum(power)
    cutoff = cumulative_power[-1] / 2.0
    idx = np.where(cumulative_power >= cutoff)[0]
    if len(idx) == 0:
        return frequency[-1]
    return frequency[idx[0]]

def wavelet_energy(x, mother, nivel):
    """
    Calcula la energía de la señal en diferentes niveles de la transformada wavelet.
    :param x: Señal EMG filtrada.
    :param mother: Tipo de wavelet.
    :param nivel: Número de niveles.
    :return: Energía de aproximación y detalles.
    """
    coeffs = pywt.wavedec(x, wavelet=mother, level=nivel)
    Et = sum(np.sum(c ** 2) for c in coeffs)
    Ea = 100 * np.sum(coeffs[0] ** 2) / Et
    Ed = [100 * np.sum(c ** 2) / Et for c in coeffs[1:]]
    return Ea, Ed

def next_power_of_2(x):
    """
    Calcula el siguiente número que es potencia de 2.
    :param x: Número entero.
    :return: Siguiente potencia de 2.
    """
    return 1 if x == 0 else 2 ** (x - 1).bit_length()

def plot_features(signal, channel_name, fs, feature_matrix, step):
    """
    Grafica las características extraídas superpuestas con la señal EMG.
    :param signal: Señal EMG filtrada.
    :param channel_name: Nombre del canal.
    :param fs: Frecuencia de muestreo.
    :param feature_matrix: DataFrame con características.
    :param step: Paso de la ventana (en muestras).
    """
    ts = np.arange(0, len(signal) / fs, 1 / fs)
    tf = np.arange(0, len(feature_matrix) * step / fs, step / fs)
    for feature in feature_matrix.columns:
        plt.figure(figsize=(12, 6))
        plt.plot(ts, signal, label='Señal EMG', alpha=0.5)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Amplitud (mV)')
        plt.title(f'{channel_name}: {feature}')
        ax2 = plt.twinx()
        plt.plot(tf, feature_matrix[feature], 'r', label=feature)
        plt.ylabel('Valor de la característica')
        plt.legend(loc='upper right')
        plt.tight_layout()
        plt.show()
```

<div align="center"> <img src="(inserta_link_imagen_features_VAR_aqui)" alt="VAR"> <p><em>Figura 5: Característica VAR</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_RMS_aqui)" alt="RMS"> <p><em>Figura 6: Característica RMS</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_IEMG_aqui)" alt="IEMG"> <p><em>Figura 7: Característica IEMG</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_MAV_aqui)" alt="MAV"> <p><em>Figura 8: Característica MAV</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_LOG_aqui)" alt="LOG"> <p><em>Figura 9: Característica LOG</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_WL_aqui)" alt="WL"> <p><em>Figura 10: Característica WL</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_ACC_aqui)" alt="ACC"> <p><em>Figura 11: Característica ACC</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_DASDV_aqui)" alt="DASDV"> <p><em>Figura 12: Característica DASDV</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_ZC_aqui)" alt="ZC"> <p><em>Figura 13: Característica ZC</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_WAMP_aqui)" alt="WAMP"> <p><em>Figura 14: Característica WAMP</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_MYOP_aqui)" alt="MYOP"> <p><em>Figura 15: Característica MYOP</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_FR_aqui)" alt="FR"> <p><em>Figura 16: Característica FR</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_MNP_aqui)" alt="MNP"> <p><em>Figura 17: Característica MNP</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_TP_aqui)" alt="TP"> <p><em>Figura 18: Característica TP</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_MNF_aqui)" alt="MNF"> <p><em>Figura 19: Característica MNF</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_MDF_aqui)" alt="MDF"> <p><em>Figura 20: Característica MDF</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_PKF_aqui)" alt="PKF"> <p><em>Figura 21: Característica PKF</em></p> </div> 

<div align="center"> <img src="(inserta_link_imagen_features_WENT_aqui)" alt="WENT"> <p><em>Figura 22: Característica WENT</em></p> </div> ```