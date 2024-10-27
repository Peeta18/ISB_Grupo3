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
    # Asegurarse de que high_f sea menor que Nyquist
    if high_f >= nyquist:
        print(f"Ajustando high_f de {high_f} Hz a {nyquist - 1} Hz para evitar errores.")
        high_f = nyquist - 1  # Ajuste a 1 Hz menos que Nyquist

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

# Funciones para extracción de características

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

# Código principal

def main():
    # Parámetros iniciales
    signal_path = 'Reposo.txt'  # <-- Cambia este nombre para analizar otros archivos
    channel_name = 'A1'  # Nombre del canal según el archivo
    sampling_frequency = 1000  # Frecuencia de muestreo en Hz (según el archivo)
    frame = int(0.5 * sampling_frequency)  # Ventana de 0.5 segundos
    step = int(0.25 * sampling_frequency)  # Paso de 0.25 segundos

    # Verificar si el archivo existe
    if not os.path.isfile(signal_path):
        print(f"Error: El archivo '{signal_path}' no fue encontrado en el directorio actual.")
        return

    # Leer el archivo de texto
    try:
        # Leer solo las primeras 6 columnas (0 a 5) para evitar columnas vacías
        emg_data = pd.read_csv(signal_path, sep='\t', comment='#', header=None, usecols=range(6))
        print(f"Archivo '{signal_path}' leído exitosamente.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return

    # Mostrar información básica de los datos
    print(f"Forma de los datos: {emg_data.shape}")
    print("Primeras filas de los datos:")
    print(emg_data.head())

    # Seleccionar la columna de interés (A1, índice 5)
    try:
        emg_signal = emg_data.iloc[:, 5].values
        print(f"Longitud de la señal EMG: {len(emg_signal)}")
        print(f"Primeros 10 valores de la señal EMG: {emg_signal[:10]}")
    except Exception as e:
        print(f"Error al seleccionar la columna de la señal EMG: {e}")
        return

    # Verificar si la señal está vacía o contiene NaN
    if emg_signal.size == 0:
        print("Error: La señal EMG está vacía.")
        return
    if np.isnan(emg_signal).all():
        print("Error: La señal EMG contiene únicamente valores NaN.")
        return

    # Reemplazar NaN con interpolación o eliminación si es necesario
    if np.isnan(emg_signal).any():
        print("Advertencia: La señal EMG contiene valores NaN. Aplicando interpolación.")
        emg_signal = pd.Series(emg_signal).interpolate().fillna(method='bfill').fillna(method='ffill').values

    # Graficar señal EMG cruda
    plot_signal(emg_signal, sampling_frequency, f'Señal EMG Cruda - {channel_name}')

    # Procesamiento de señal
    try:
        filtered_signal = notch_filter(emg_signal, sampling_frequency, plot=True)
        filtered_signal = bp_filter(filtered_signal, 10, 490, sampling_frequency, plot=True)  # Ajuste a 490 Hz
    except ValueError as ve:
        print(f"Error en el filtrado de la señal: {ve}")
        return
    except Exception as e:
        print(f"Error inesperado durante el filtrado: {e}")
        return

    # Verificar la señal filtrada
    print(f"Primeros 10 valores de la señal filtrada: {filtered_signal[:10]}")

    # Graficar señal EMG filtrada
    plot_signal(filtered_signal, sampling_frequency, f'Señal EMG Filtrada - {channel_name}')

    # Extracción de características
    try:
        emg_features, features_names = features_estimation(filtered_signal, channel_name,
                                                           sampling_frequency, frame, step, plot=True)
    except Exception as e:
        print(f"Error durante la extracción de características: {e}")
        return

    # Guardar características en un archivo CSV
    try:
        output_csv = 'caracteristicas_emg.csv'
        emg_features.to_csv(output_csv, index=False)
        print(f'Las características se han guardado en "{output_csv}".')
    except Exception as e:
        print(f"Error al guardar las características: {e}")

if __name__ == '__main__':
    main()

#Bibliografía
#S. Cai, Y. Chen, S. Huang, Y. Wu, H. Zheng, X. Li, y L. Xie, "SVM-Based Classification of sEMG Signals for Upper-Limb Self-Rehabilitation Training," Frontiers in Neurorobotics, vol. 13, art. 31, Jun. 2019, doi: 10.3389/fnbot.2019.00031​(fnbot-13-00031).

#N. Li, J. Ou, H. He, J. He, L. Zhang, Z. Peng, J. Zhong, y N. Jiang, "Exploration of a machine learning approach for diagnosing sarcopenia among Chinese community-dwelling older adults using sEMG-based data," Journal of NeuroEngineering and Rehabilitation, vol. 21, art. 69, Apr. 2024, doi: 10.1186/s12984-024-01369-y​(s12984-024-01369-y).

#S. Restrepo, "EMG-pattern-recognition," GitHub, [Online]. Available: https://github.com/SebastianRestrepoA/EMG-pattern-recognition/tree/master
