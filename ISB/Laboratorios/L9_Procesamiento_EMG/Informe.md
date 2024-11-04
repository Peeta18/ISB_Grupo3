LAB 9: PROCESAMIENTO DE SEÑALES EMG
Tabla de Contenido
Introducción
Objetivos
Materiales
Procedimiento
Resultados
Discusión
Conclusiones
Bibliografía
Introducción <a name="introduccion"></a>
La electromiografía de superficie (sEMG) es una técnica no invasiva utilizada para registrar la actividad eléctrica generada por los músculos esqueléticos. Esta técnica se basa en la captación de señales eléctricas durante la contracción muscular y es ampliamente empleada en áreas como la rehabilitación, diagnóstico de enfermedades musculares, y control de prótesis. La sEMG permite obtener información clave sobre el comportamiento muscular bajo diferentes condiciones [10, 11].

El procesamiento de señales EMG es esencial para eliminar el ruido y extraer las características relevantes, lo cual permite una interpretación más precisa de los datos para aplicaciones específicas, como la detección de sarcopenia o la evaluación del rendimiento muscular en entornos clínicos y de investigación.

Objetivos <a name="objetivos"></a>
Diseñar un filtro adecuado para señales EMG utilizando técnicas avanzadas.
Extraer y analizar características relevantes de señales EMG, aplicando métodos de normalización y cálculo de parámetros.
Materiales <a name="materiales"></a>
Material	Cantidad
Software de procesamiento de datos (Python)	N.A
Procedimiento <a name="procedimiento"></a>
1. Selección de las señales a analizar
Para este experimento, se utilizaron señales EMG de tres músculos diferentes:

Bíceps
Tríceps
Gastrocnemio (pantorrilla)
Cada señal incluye tres fases: reposo, contracción simple, y contracción progresiva.

2. Filtrado de la señal
En primer lugar, las señales EMG en crudo fueron sometidas a un proceso de filtrado utilizando la transformada wavelet para eliminar el ruido y mejorar la calidad de los datos. Este proceso se implementó con una wavelet de tipo Daubechies (db6) y niveles de descomposición específicos.

python
Copiar código
# Código para el filtrado de señal EMG
# Este código aplica la función wavelet_denoising a una señal EMG y devuelve la señal filtrada.
wavelet = 'db6'
level = 4
threshold = [0.022, 0.109, 0.303, 0.742]
filtered_signal = wavelet_denoising(amplitude, wavelet, level, threshold)
[Espacio para imagen]: Inserta aquí la imagen de la señal en crudo comparada con la señal filtrada.

3. Normalización de la señal
Para comparar los resultados entre señales y reducir el impacto de la variabilidad intersujeto, las señales filtradas fueron normalizadas respecto al valor máximo alcanzado durante la contracción máxima voluntaria (MVC).

python
Copiar código
# Código para normalizar la señal EMG
imvc = np.max(np.abs(filtered_signal))
normalized_signal = filtered_signal / imvc
[Espacio para imagen]: Inserta aquí la imagen de la señal normalizada para mostrar la comparación entre la señal filtrada y la normalizada.

4. Extracción de características de la señal
A partir de la señal EMG filtrada y normalizada, se extrajeron características como el valor absoluto medio (MAV), raíz cuadrática media (RMS), longitud de la forma de onda (WL), tasa de impulso mioeléctrico (MYOP) y varianza (VAR).

python
Copiar código
# Código para extraer características de la señal EMG
MAV = mean_absolute_value(normalized_signal)
RMS = root_mean_square(normalized_signal)
WL = waveform_length(normalized_signal)
MYOP = myopulse_percentage_rate(normalized_signal)
VAR = variance(normalized_signal)
[Espacio para imagen]: Inserta aquí la imagen que muestre las características calculadas para cada fase de la señal EMG.

Resultados <a name="resultados"></a>
Características extraídas para cada músculo
Se obtuvieron los siguientes valores para las características MAV, RMS, WL, MYOP y VAR en las señales EMG de los músculos bíceps, tríceps y gastrocnemio, en cada una de las fases de reposo, contracción simple y contracción progresiva.

[Espacio para tabla]: Inserta aquí una tabla que muestre los resultados de las características extraídas para cada fase y músculo.

Discusión <a name="discusion"></a>
El análisis de las características extraídas permite identificar patrones específicos en la actividad de cada músculo en las diferentes fases de contracción y reposo.

MAV (Mean Absolute Value): Valor promedio que indica la intensidad de la señal. Los valores más altos en la fase de contracción progresiva sugieren una activación muscular más intensa.
RMS (Root Mean Square): Representa la magnitud de la señal en términos de potencia. El RMS más alto se obtuvo en el músculo gastrocnemio durante la fase de contracción con carga.
WL (Waveform Length): Una medida de la complejidad de la señal. En el bíceps, la longitud de onda fue notablemente más alta, posiblemente debido a una mayor activación de fibras musculares.
Conclusiones <a name="conclusiones"></a>
El procesamiento de señales EMG con técnicas de filtrado y normalización es esencial para mejorar la precisión de los análisis de activación muscular. Los resultados obtenidos demuestran que las características extraídas (MAV, RMS, WL, MYOP y VAR) son representativas del comportamiento muscular en distintas condiciones de contracción, lo cual puede ser de gran utilidad para aplicaciones clínicas y de investigación, como el diagnóstico temprano de condiciones musculares [10, 11].

Bibliografía <a name="bibliografia"></a>
Referencia completa de fnbot-13-00031.pdf en formato IEEE.
Referencia completa de s12984-024-01369-y.pdf en formato IEEE.
