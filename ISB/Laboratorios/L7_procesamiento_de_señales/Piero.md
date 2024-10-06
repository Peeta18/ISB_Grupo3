# Análisis de Señales EMG y ECG

Este repositorio contiene el análisis de tres señales EMG y tres señales ECG, que han sido procesadas y filtradas para su comparación en el dominio del tiempo y de la frecuencia. A continuación se presentan los gráficos, el análisis de los filtros aplicados y la justificación de su uso para cada señal.

## Tabla de Contenidos
- [Análisis de Señales EMG](#análisis-de-señales-emg)
  - [EMG en Reposo](#emg-en-reposo)
  - [EMG Movimiento Voluntario](#emg-movimiento-voluntario)
  - [EMG Movimiento Forzado](#emg-movimiento-forzado)
- [Análisis de Señales ECG](#análisis-de-señales-ecg)
  - [ECG Estado Basal](#ecg-estado-basal)
  - [ECG Luego de Respiración](#ecg-luego-de-respiración)
  - [ECG Luego de Ejercicio](#ecg-luego-de-ejercicio)

---

## Análisis de Señales EMG

### EMG en Reposo
1. **Gráfica en el Dominio del Tiempo:**
   - ![EMG Reposo - Tiempo](path/to/emg_reposo_tiempo.png)
   
2. **Gráfica en el Dominio de la Frecuencia (Señal raw):**
   - ![EMG Reposo - Frecuencia](path/to/emg_reposo_frecuencia.png)

3. **Gráfica en el Dominio de la Frecuencia (Señal filtrada):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

4. **Comparación de señales:**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)
  
5. **Transformada Corta de Fourier (STFT):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

6. **Diagrama de Polos y Ceros:**
   - ![Polos y Ceros - EMG Reposo](path/to/emg_reposo_polos_ceros.png)

7. **Diagrama de Bode:**
   - ![Bode - EMG Reposo](path/to/emg_reposo_bode.png)

8. **Justificación de los Filtros:**
   - **Filtro Pasa-Bajo (Butterworth)**: Se aplicó para atenuar el ruido de alta frecuencia en la señal de reposo. Dado que no se esperaban movimientos significativos en la señal, el filtro pasa-bajo mantuvo la señal sin distorsión.
   - **Filtro Notch**: Utilizado para eliminar la frecuencia de línea de 50/60 Hz. Como el equipo puede introducir esta interferencia en estado de reposo, se optó por eliminarla.
   - **Filtro Pasa-Alto (FIR)**: Aplicado para suprimir cualquier componente de baja frecuencia que pudiera alterar el análisis.

---

### EMG Movimiento Voluntario
1. **Gráfica en el Dominio del Tiempo:**
   - ![EMG Reposo - Tiempo](path/to/emg_reposo_tiempo.png)
   
2. **Gráfica en el Dominio de la Frecuencia (Señal raw):**
   - ![EMG Reposo - Frecuencia](path/to/emg_reposo_frecuencia.png)

3. **Gráfica en el Dominio de la Frecuencia (Señal filtrada):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

4. **Comparación de señales:**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)
  
5. **Transformada Corta de Fourier (STFT):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

6. **Diagrama de Polos y Ceros:**
   - ![Polos y Ceros - EMG Reposo](path/to/emg_reposo_polos_ceros.png)

7. **Diagrama de Bode:**
   - ![Bode - EMG Reposo](path/to/emg_reposo_bode.png)

8. **Justificación de los Filtros:**
- **Justificación del Filtro Pasa-Alto (30 Hz)**: El filtro pasa-alto con frecuencia de corte de 30 Hz fue utilizado para eliminar las componentes de baja frecuencia y el ruido DC presentes en la señal. 
- **Justificación del Filtro Notch (50 Hz)**: El filtro Notch en 50 Hz se aplicó para suprimir la interferencia de la frecuencia de línea eléctrica, que puede contaminar la señal. 
- **Justificación del Filtro Pasa-Bajo (150 Hz)**: El filtro pasa-bajo se utilizó para eliminar las componentes de alta frecuencia (>150 Hz) que no contienen información relevante para la actividad muscular.

---

### EMG Movimiento Forzado
1. **Gráfica en el Dominio del Tiempo:**
   - ![EMG Reposo - Tiempo](path/to/emg_reposo_tiempo.png)
   
2. **Gráfica en el Dominio de la Frecuencia (Señal raw):**
   - ![EMG Reposo - Frecuencia](path/to/emg_reposo_frecuencia.png)

3. **Gráfica en el Dominio de la Frecuencia (Señal filtrada):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

4. **Comparación de señales:**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)
  
5. **Transformada Corta de Fourier (STFT):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

6. **Diagrama de Polos y Ceros:**
   - ![Polos y Ceros - EMG Reposo](path/to/emg_reposo_polos_ceros.png)

7. **Diagrama de Bode:**
   - ![Bode - EMG Reposo](path/to/emg_reposo_bode.png)

8. **Justificación de los Filtros:**
- **Filtro FIR Pasa-Alto (30 Hz)**: Seleccionado para eliminar componentes de baja frecuencia, incluyendo el ruido de base y el componente DC. 
- **Filtro IIR Pasa-Bajo (150 Hz)**:Elimina componentes de alta frecuencia, manteniendo la energía de la señal entre el rango de interés. 
- **Filtro IIR Pasa-Banda (30-150 Hz)**: Ajusta la señal al rango típico de frecuencias de EMG, manteniendo la información relevante y eliminando residuos.

---

## Análisis de Señales ECG

### ECG Estado Basal
1. **Gráfica en el Dominio del Tiempo:**
   - ![EMG Reposo - Tiempo](path/to/emg_reposo_tiempo.png)
   
2. **Gráfica en el Dominio de la Frecuencia (Señal raw):**
   - ![EMG Reposo - Frecuencia](path/to/emg_reposo_frecuencia.png)

3. **Gráfica en el Dominio de la Frecuencia (Señal filtrada):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

4. **Comparación de señales:**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)
  
5. **Transformada Corta de Fourier (STFT):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

6. **Diagrama de Polos y Ceros:**
   - ![Polos y Ceros - EMG Reposo](path/to/emg_reposo_polos_ceros.png)

7. **Diagrama de Bode:**
   - ![Bode - EMG Reposo](path/to/emg_reposo_bode.png)

8. **Justificación de los Filtros:**
   - **Filtro Pasa-Bajo (Butterworth)**: Se aplicó para atenuar el ruido de alta frecuencia en la señal de reposo. Dado que no se esperaban movimientos significativos en la señal, el filtro pasa-bajo mantuvo la señal sin distorsión.
   - **Filtro Notch**: Utilizado para eliminar la frecuencia de línea de 50/60 Hz. Como el equipo puede introducir esta interferencia en estado de reposo, se optó por eliminarla.
   - **Filtro Pasa-Alto (FIR)**: Aplicado para suprimir cualquier componente de baja frecuencia que pudiera alterar el análisis.

---

### ECG Luego de Respiración
1. **Gráfica en el Dominio del Tiempo:**
   - ![EMG Reposo - Tiempo](path/to/emg_reposo_tiempo.png)
   
2. **Gráfica en el Dominio de la Frecuencia (Señal raw):**
   - ![EMG Reposo - Frecuencia](path/to/emg_reposo_frecuencia.png)

3. **Gráfica en el Dominio de la Frecuencia (Señal filtrada):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

4. **Comparación de señales:**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)
  
5. **Transformada Corta de Fourier (STFT):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

6. **Diagrama de Polos y Ceros:**
   - ![Polos y Ceros - EMG Reposo](path/to/emg_reposo_polos_ceros.png)

7. **Diagrama de Bode:**
   - ![Bode - EMG Reposo](path/to/emg_reposo_bode.png)

8. **Justificación de los Filtros:**
   - **Filtro Pasa-Bajo (Butterworth)**: Se aplicó para atenuar el ruido de alta frecuencia en la señal de reposo. Dado que no se esperaban movimientos significativos en la señal, el filtro pasa-bajo mantuvo la señal sin distorsión.
   - **Filtro Notch**: Utilizado para eliminar la frecuencia de línea de 50/60 Hz. Como el equipo puede introducir esta interferencia en estado de reposo, se optó por eliminarla.
   - **Filtro Pasa-Alto (FIR)**: Aplicado para suprimir cualquier componente de baja frecuencia que pudiera alterar el análisis.

---

### ECG Luego de Ejercicio
1. **Gráfica en el Dominio del Tiempo:**
   - ![EMG Reposo - Tiempo](path/to/emg_reposo_tiempo.png)
   
2. **Gráfica en el Dominio de la Frecuencia (Señal raw):**
   - ![EMG Reposo - Frecuencia](path/to/emg_reposo_frecuencia.png)

3. **Gráfica en el Dominio de la Frecuencia (Señal filtrada):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

4. **Comparación de señales:**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)
  
5. **Transformada Corta de Fourier (STFT):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

6. **Diagrama de Polos y Ceros:**
   - ![Polos y Ceros - EMG Reposo](path/to/emg_reposo_polos_ceros.png)

7. **Diagrama de Bode:**
   - ![Bode - EMG Reposo](path/to/emg_reposo_bode.png)

8. **Justificación de los Filtros:**
   - **Filtro Pasa-Bajo (Butterworth)**: Se aplicó para atenuar el ruido de alta frecuencia en la señal de reposo. Dado que no se esperaban movimientos significativos en la señal, el filtro pasa-bajo mantuvo la señal sin distorsión.
   - **Filtro Notch**: Utilizado para eliminar la frecuencia de línea de 50/60 Hz. Como el equipo puede introducir esta interferencia en estado de reposo, se optó por eliminarla.
   - **Filtro Pasa-Alto (FIR)**: Aplicado para suprimir cualquier componente de baja frecuencia que pudiera alterar el análisis.
  
---

### Bibliografía
1. Lian, J., & Wang, Z. (2023). Stages-Based ECG Signal Analysis From Traditional Signal Processing to Machine Learning. IEEE Transactions on Biomedical Engineering, 70(1), 12-22.
2. Moreira, D., Fonseca, J., & Lourenço, A. (2020). Characterization and Differentiation of Electromyographic Signals Acquired Using the BITalino Platform. IEEE Access, 8, 102981-102993.
3. Acharya, U. R., Faust, O., & Suri, J. S. (2021). Biomedical Signal Processing: An ECG Application. En Advances in Cardiac Signal Processing (pp. 117-142). Springer.
4. Rodríguez, I., Parra, C., & González, E. (2019). Experience of Use of the BITalino Kit for Biomedical Signals Recording. IEEE Latin America Transactions, 17(12), 2022-2030.
