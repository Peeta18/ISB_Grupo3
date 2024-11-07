!pip install ecg-plot neurokit2

!pip install neurokit2 ecg-plot

import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from google.colab import drive
import numpy as np
import ecg_plot
import neurokit2 as nk

drive.mount('/content/drive')

def load_signal(csv_file):
    try:
        data = pd.read_csv(csv_file)
        signal = data.iloc[:, 0].values
        return signal
    except Exception as e:
        print(f"Error al cargar la señal desde {csv_file}: {e}")
        return None

def plot_time_domain(signal, fs, title):
    N = len(signal)
    T = 1.0 / fs
    t = np.linspace(0.0, N * T, N)
    plt.figure(figsize=(15, 3))
    plt.plot(t, signal)
    plt.title(f'Señal en el dominio del tiempo - {title}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.xlim([3, 10])  # Focalizar en un tramo específico
    plt.show()

signal1 = load_signal('/content/drive/MyDrive/isb/ECG/EjercicioD3.csv')
plot_time_domain(signal1, 1000, "Señal Basal ECG")

ecg_plot.plot_1((signal1[:5000]*1/511)-1)
#ecg_plot.plot_1(signal1*1/1023, sample_rate=1000)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
#plt.xticks(np.arange(0, 10000, 1000))
#plt.xticks([])
plt.show()

signal1_clean = nk.ecg_clean(signal1, sampling_rate=1000)
plot_time_domain(signal1, 1000, "Raw signal")
plot_time_domain(signal1_clean, 1000, "Clean signal")

df, info = nk.ecg_process(signal1_clean, sampling_rate=1000)
analyze_df = nk.ecg_analyze(df, sampling_rate=1000)
analyze_df
#analyze_df.T.head(1)

simp, inf = nk.ecg_process(signal1_clean, sampling_rate=1000, method = 'pantompkins1985')
nk.ecg_plot(simp, inf)
qrs_epochs = nk.ecg_segment(signal1_clean, rpeaks=None, sampling_rate=1000, show=True)
