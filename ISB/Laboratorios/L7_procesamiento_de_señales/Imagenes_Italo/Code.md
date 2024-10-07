import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, freqz, tf2zpk
from scipy.fft import fft, fftfreq
import json

# Configuración de parámetros
SAMPLING_RATE = 1000  # Hz, según el encabezado del archivo
FILTER_ORDER = 4
LOWCUT = 20.0   # Hz
HIGHCUT = 450.0  # Hz
FILE_NAME = 'EMG_Reposo.txt'  # Cambia esto por el nombre de tu archivo

def read_emg_data(EMG_Reposo):
    """
    Lee el archivo de texto y extrae la señal EMG (A1).
    """
    emg = []
    with open(EMG_Reposo, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue  # Omitir líneas de encabezado
            parts = line.strip().split('\t')
            if len(parts) < 6:
                continue  # Asegurarse de que hay suficientes columnas
            try:
                value = float(parts[5])
                emg.append(value)
            except ValueError:
                continue  # Omitir líneas con datos no numéricos
    return np.array(emg)

def plot_time_domain(emg, fs):
    """
    Grafica la señal en el dominio del tiempo.
    """
    time = np.arange(len(emg)) / fs
    plt.figure(figsize=(12, 4))
    plt.plot(time, emg, label='Señal EMG Cruda')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Dominio del Tiempo')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_frequency_domain(emg, fs, title='Dominio de la Frecuencia'):
    """
    Calcula y grafica la FFT de la señal.
    """
    N = len(emg)
    yf = fft(emg)
    xf = fftfreq(N, 1 / fs)[:N//2]
    magnitude = 2.0/N * np.abs(yf[0:N//2])
    
    plt.figure(figsize=(12, 4))
    plt.plot(xf, magnitude)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def design_bandpass_filter(lowcut, highcut, fs, order=4):
    """
    Diseña un filtro Butterworth bandpass.
    """
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def apply_filter(emg, b, a):
    """
    Aplica el filtro a la señal utilizando filtrado hacia adelante y hacia atrás.
    """
    y = filtfilt(b, a, emg)
    return y

def plot_comparison(raw, filtered, fs):
    """
    Compara la señal cruda y la filtrada en el dominio del tiempo.
    """
    time = np.arange(len(raw)) / fs
    plt.figure(figsize=(12, 6))
    plt.plot(time, raw, label='Señal Cruda', alpha=0.7)
    plt.plot(time, filtered, label='Señal Filtrada', alpha=0.7)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.title('Comparación de Señales')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_bode(b, a):
    """
    Grafica el diagrama de Bode (amplitud y fase) del filtro.
    """
    w, h = freqz(b, a, worN=8000)
    plt.figure(figsize=(12, 6))

    # Amplitud
    plt.subplot(2, 1, 1)
    plt.plot(0.5*SAMPLING_RATE*w/np.pi, 20 * np.log10(abs(h)), 'b')
    plt.title('Diagrama de Bode del Filtro Butterworth Bandpass')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud (dB)')
    plt.grid(True)

    # Fase
    angles = np.unwrap(np.angle(h))
    plt.subplot(2, 1, 2)
    plt.plot(0.5*SAMPLING_RATE*w/np.pi, angles * 180 / np.pi, 'g')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Fase (grados)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_pole_zero(b, a):
    """
    Grafica el diagrama de polos y ceros del filtro.
    """
    z, p, k = tf2zpk(b, a)
    plt.figure(figsize=(6,6))
    plt.scatter(np.real(z), np.imag(z), marker='o', label='Ceros')
    plt.scatter(np.real(p), np.imag(p), marker='x', label='Polos')
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.title('Diagrama de Polos y Ceros')
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def main():
    # Leer datos
    emg_raw = read_emg_data(FILE_NAME)
    print(f"Señal EMG leída: {len(emg_raw)} muestras.")

    # Graficar dominio del tiempo
    plot_time_domain(emg_raw, SAMPLING_RATE)

    # Graficar FFT de la señal cruda
    plot_frequency_domain(emg_raw, SAMPLING_RATE, title='Dominio de la Frecuencia - Señal Cruda')

    # Diseñar filtro
    b, a = design_bandpass_filter(LOWCUT, HIGHCUT, SAMPLING_RATE, order=FILTER_ORDER)
    print(f"Filtro Butterworth bandpass diseñado: Orden={FILTER_ORDER}, {LOWCUT}Hz-{HIGHCUT}Hz.")

    # Aplicar filtro
    emg_filtered = apply_filter(emg_raw, b, a)

    # Graficar FFT de la señal filtrada
    plot_frequency_domain(emg_filtered, SAMPLING_RATE, title='Dominio de la Frecuencia - Señal Filtrada')

    # Comparar señales cruda y filtrada
    plot_comparison(emg_raw, emg_filtered, SAMPLING_RATE)

    # Graficar diagrama de Bode
    plot_bode(b, a)

    # Graficar diagrama de polos y ceros
    plot_pole_zero(b, a)

if __name__ == "__main__":
    main()
