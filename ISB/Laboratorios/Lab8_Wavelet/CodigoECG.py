import numpy as np 
import pywt
import matplotlib.pyplot as plt
from numpy import array, linspace

# Lectura de documento txt con tabulación (\t) como delimitador
datos = np.genfromtxt(r"C:\Users\tefic\Downloads\LAB8_ECG\EJERCICIO.txt", delimiter="\t")

# Nos quedamos con los datos del sensor (asumiendo que están en unidades arbitrarias)
ecg_datos = datos[:, -2]

# Convertir los datos de señal a milivoltios (mV)
ecg_datos_mV = (((array(ecg_datos) / 1024) - 0.5) * 3000) / 1000

# Definir el tramo de la señal que deseas analizar
start = 0  # Índice de inicio del tramo
end = 10000    # Índice de fin del tramo
ecg_tramo_mV = ecg_datos_mV[start:end]

# Aplicar la transformada wavelet
wavelet = 'db6'  # Cambiado a db6 según lo sugerido en el trabajo de grado
level = 5
coeffs = pywt.wavedec(ecg_tramo_mV, wavelet, level=level)

# Calcular el nivel de ruido y el nivel de la señal sobre la magnitud absoluta de la señal
noise_level = np.std(ecg_datos_mV)  # Estimación del nivel de ruido
n_samples = len(ecg_tramo_mV)  # Estimación del nivel de la señal

# Manejo de excepciones para evitar RuntimeWarning si la señal no tiene variabilidad
threshold = noise_level * np.sqrt(2 * np.log(n_samples))

# Filtrar los coeficientes con el umbral calculado
filtered_coeffs = [pywt.threshold(coeff, threshold, mode='soft') for coeff in coeffs]

# Reconstruir la señal filtrada
filtered_signal_mV = pywt.waverec(filtered_coeffs, wavelet)

# Graficar el tramo original y el tramo filtrado
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(ecg_tramo_mV)
plt.title('Tramo de la Señal de ECG en ejercicio')
plt.xlabel("Muestra")
plt.ylabel("Amplitud (mV)")

plt.subplot(2, 1, 2)
plt.plot(filtered_signal_mV)
plt.title('Tramo de la Señal de ECG en ejercicio Filtrada')
plt.xlabel("Muestra")
plt.ylabel("Amplitud (mV)")
plt.tight_layout()
plt.show()
plt.close()

# Sección para respiraciones rápidas, se repite el proceso de wavelet
# Aplicar la transformada wavelet 'db6' también para las respiraciones rápidas y la señal en actividad
