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
   
2. **Gráfica en el Dominio de la Frecuencia:**
   - ![EMG Reposo - Frecuencia](path/to/emg_reposo_frecuencia.png)

3. **Transformada Corta de Fourier (STFT):**
   - ![EMG Reposo - STFT](path/to/emg_reposo_stft.png)

4. **Diagrama de Polos y Ceros:**
   - ![Polos y Ceros - EMG Reposo](path/to/emg_reposo_polos_ceros.png)

5. **Diagrama de Bode:**
   - ![Bode - EMG Reposo](path/to/emg_reposo_bode.png)

6. **Justificación de los Filtros:**
   - **Filtro Pasa-Bajo (Butterworth)**: Se aplicó para atenuar el ruido de alta frecuencia en la señal de reposo. Dado que no se esperaban movimientos significativos en la señal, el filtro pasa-bajo mantuvo la señal sin distorsión.
   - **Filtro Notch**: Utilizado para eliminar la frecuencia de línea de 50/60 Hz. Como el equipo puede introducir esta interferencia en estado de reposo, se optó por eliminarla.
   - **Filtro Pasa-Alto (FIR)**: Aplicado para suprimir cualquier componente de baja frecuencia que pudiera alterar el análisis.

---

### EMG Movimiento Voluntario
1. **Gráfica en el Dominio del Tiempo:**
   - ![EMG Movimiento Voluntario - Tiempo](path/to/emg_voluntario_tiempo.png)

2. **Gráfica en el Dominio de la Frecuencia:**
   - ![EMG Movimiento Voluntario - Frecuencia](path/to/emg_voluntario_frecuencia.png)

3. **Transformada Corta de Fourier (STFT):**
   - ![EMG Movimiento Voluntario - STFT](path/to/emg_voluntario_stft.png)

4. **Diagrama de Polos y Ceros:**
   - ![Polos y Ceros - EMG Movimiento Voluntario](path/to/emg_voluntario_polos_ceros.png)

5. **Diagrama de Bode:**
   - ![Bode - EMG Movimiento Voluntario](path/to/emg_voluntario_bode.png)

6. **Justificación de los Filtros:**
   - **Filtro Pasa-Bajo (Butterworth)**: Se usó para suavizar la señal y eliminar componentes de alta frecuencia debido a movimientos bruscos.
   - **Filtro Notch**: Aplicado para eliminar interferencias en la frecuencia de línea.
   - **Filtro Pasa-Alto (FIR)**: Eliminó ruido de baja frecuencia que podría haber sido causado por la contracción muscular lenta.

---

### EMG Movimiento Forzado
1. **Gráfica en el Dominio del Tiempo:**
   - ![EMG Movimiento Forzado - Tiempo](path/to/emg_forzado_tiempo.png)

2. **Gráfica en el Dominio de la Frecuencia:**
   - ![EMG Movimiento Forzado - Frecuencia](path/to/emg_forzado_frecuencia.png)

3. **Transformada Corta de Fourier (STFT):**
   - ![EMG Movimiento Forzado - STFT](path/to/emg_forzado_stft.png)

4. **Diagrama de Polos y Ceros:**
   - ![Polos y Ceros - EMG Movimiento Forzado](path/to/emg_forzado_polos_ceros.png)

5. **Diagrama de Bode:**
   - ![Bode - EMG Movimiento Forzado](path/to/emg_forzado_bode.png)

6. **Justificación de los Filtros:**
   - **Filtro Pasa-Bajo (Butterworth)**: El filtro pasa-bajo se usó para eliminar picos de alta frecuencia debidos al esfuerzo.
   - **Filtro Notch**: Se mantuvo para asegurar la eliminación de la interferencia de línea.
   - **Filtro Pasa-Alto (FIR)**: Eliminó componentes de baja frecuencia que podrían haber surgido del esfuerzo muscular.

---

## Análisis de Señales ECG

### ECG Estado Basal
1. **Gráfica en el Dominio del Tiempo:**
   - ![ECG Basal - Tiempo](path/to/ecg_basal_tiempo.png)
   
2. **Gráfica en el Dominio de la Frecuencia:**
   - ![ECG Basal - Frecuencia](path/to/ecg_basal_frecuencia.png)

3. **Transformada Corta de Fourier (STFT):**
   - ![ECG Basal - STFT](path/to/ecg_basal_stft.png)

4. **Diagrama de Polos y Ceros:**
   - ![Polos y Ceros - ECG Basal](path/to/ecg_basal_polos_ceros.png)

5. **Diagrama de Bode:**
   - ![Bode - ECG Basal](path/to/ecg_basal_bode.png)

6. **Justificación de los Filtros:**
   - **Filtro Pasa-Bajo (Butterworth)**: Se aplicó para eliminar ruido de alta frecuencia sin afectar la morfología de la señal de ECG en reposo.
   - **Filtro Notch**: Utilizado para eliminar la frecuencia de línea que podría aparecer por interferencias en el estado basal.
   - **Filtro Pasa-Alto (FIR)**: Eliminó componentes de baja frecuencia que podrían distorsionar la morfología del ECG basal.

---

### ECG Luego de Respiración
1. **Gráfica en el Dominio del Tiempo:**
   - ![ECG Respiración - Tiempo](path/to/ecg_respiracion_tiempo.png)

2. **Gráfica en el Dominio de la Frecuencia:**
   - ![ECG Respiración - Frecuencia](path/to/ecg_respiracion_frecuencia.png)

3. **Transformada Corta de Fourier (STFT):**
   - ![ECG Respiración - STFT](path/to/ecg_respiracion_stft.png)

4. **Diagrama de Polos y Ceros:**
   - ![Polos y Ceros - ECG Respiración](path/to/ecg_respiracion_polos_ceros.png)

5. **Diagrama de Bode:**
   - ![Bode - ECG Respiración](path/to/ecg_respiracion_bode.png)

6. **Justificación de los Filtros:**
   - **Filtro Pasa-Bajo (Butterworth)**: Se aplicó para eliminar componentes de alta frecuencia debidas a la respiración rápida.
   - **Filtro Notch**: Atenuó las interferencias de línea y otros ruidos de entorno.
   - **Filtro Pasa-Alto (FIR)**: Removió las componentes de baja frecuencia causadas por movimientos torácicos lentos.

---

### ECG Luego de Ejercicio
1. **Gráfica en el Dominio del Tiempo:**
   - ![ECG Ejercicio - Tiempo](path/to/ecg_ejercicio_tiempo.png)

2. **Gráfica en el Dominio de la Frecuencia:**
   - ![ECG Ejercicio - Frecuencia](path/to/ecg_ejercicio_frecuencia.png)

3. **Transformada Corta de Fourier (STFT):**
   - ![ECG Ejercicio - STFT](path/to/ecg_ejercicio_stft.png)

4. **Diagrama de Polos y Ceros:**
   - ![Polos y Ceros - ECG Ejercicio](path/to/ecg_ejercicio_polos_ceros.png)

5. **Diagrama de Bode:**
   - ![Bode - ECG Ejercicio](path/to/ecg_ejercicio_bode.png)

6. **Justificación de los Filtros:**
   - **Filtro Pasa-Bajo (Butterworth)**: Eliminó ruido de alta frecuencia causado por el aumento de la frecuencia cardiaca.
   - **Filtro Notch**: Suprimió cualquier interferencia persistente de la frecuencia de línea.
   - **Filtro Pasa-Alto (FIR)**: Redujo componentes de baja frecuencia que podrían haber surgido por movimientos del cuerpo.
  
---

### Bibliografía

Lian, J., & Wang, Z. (2023). Stages-Based ECG Signal Analysis From Traditional Signal Processing to Machine Learning. IEEE Transactions on Biomedical Engineering, 70(1), 12-22.
Moreira, D., Fonseca, J., & Lourenço, A. (2020). Characterization and Differentiation of Electromyographic Signals Acquired Using the BITalino Platform. IEEE Access, 8, 102981-102993.
Acharya, U. R., Faust, O., & Suri, J. S. (2021). Biomedical Signal Processing: An ECG Application. En Advances in Cardiac Signal Processing (pp. 117-142). Springer.
Rodríguez, I., Parra, C., & González, E. (2019). Experience of Use of the BITalino Kit for Biomedical Signals Recording. IEEE Latin America Transactions, 17(12), 2022-2030.
