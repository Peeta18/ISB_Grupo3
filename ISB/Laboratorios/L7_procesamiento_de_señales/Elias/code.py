import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Leer el archivo de texto
file_path = 'EMG_reposo.txt'  # Asegúrate de que la ruta esté bien definida
data = []

with open(file_path, 'r') as file:
    for line in file:
        if not line.startswith('#'):  # Saltar las líneas de comentarios
            values = line.split()
            if len(values) >= 6:  # Asegúrate de que haya suficientes columnas
                data.append(float(values[5]))  # Columna A1, que parece ser la señal EMG

# Convertir a array de numpy para análisis
data = np.array(data)

# Parámetros
fs = 1000  # Frecuencia de muestreo en Hz (según el archivo de texto)
t = np.arange(len(data)) / fs  # Tiempo en segundos

# Graficar en el dominio del tiempo
plt.figure(figsize=(10, 4))
plt.plot(t, data)
plt.title('Señal EMG - Dominio del Tiempo')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid()
plt.show()

# FFT para dominio de frecuencia
n = len(data)
f = np.linspace(0, fs/2, int(n/2))
fft_values = fft(data)
fft_magnitude = np.abs(fft_values)[:n//2]  # Tomar la mitad positiva

# Graficar en el dominio de frecuencia
plt.figure(figsize=(10, 4))
plt.plot(f, fft_magnitude)
plt.title('Señal EMG - Dominio de Frecuencia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.grid()
plt.show()

