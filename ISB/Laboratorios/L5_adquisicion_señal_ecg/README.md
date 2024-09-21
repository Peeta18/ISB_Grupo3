# **LABORATORIO 5: – Uso de Bitalino para ECG**
Fecha: 18-09-2024


# **Tabla de contenidos**
1. [Introducción](#id0)
2. [Objetivos](#id1)
3. [Materiales y equipos](#id2)
4. [Procedimiento](#id3)
5. [Resultados](#id4)\
     4.1 [Conexión usada](#id5)\
     4.2 [Video de la señal](#id6)\
     4.3 [Archivos](#id8)\
     4.4 [Ploteo de la señal en Python](#id9)
6. [Conclusiones](#id10)
7. [Referencias](#id11)

## **Introducción al laboratorio** <a name="id0"></a>
---
<p align="justify">El electrocardiograma (ECG) es una técnica diagnóstica esencial que permite visualizar la actividad eléctrica del corazón mediante electrodos adheridos a la piel. Este procedimiento es indoloro y nos ayuda en la detección y monitorización de diversas afecciones cardíacas, como arritmias, bloqueos cardíacos y otros problemas relacionados con la función eléctrica del corazón. Al registrar las variaciones en el voltaje eléctrico que ocurren con cada latido cardíaco, el ECG produce trazos que los médicos pueden analizar para evaluar el ritmo y la estructura del corazón. Gracias a herramientas avanzadas como el Bitalino, ahora podemos realizar y estudiar estas mediciones no solo en entornos clínicos, sino también en la investigación y la educación. Esto nos proporciona una forma efectiva y accesible de entender la dinámica cardíaca a los estudiantes de Ingeniería Biomédica.


### Señal de ECG </p>
Podemos identificar 3 fases del ECG:
https://github.com/Peeta18/ISB_Grupo3/issues/1#issue-2540508551
<p align="center"><img src="[![Segmentos](https://github.com/user-attachments/assets/220a2655-cbb3-4b58-967e-8c22a39f4411)](https://github.com/Peeta18/ISB_Grupo3/issues/1#issue-2540508551)" width="600" height="400"></p>
<p align="center">Figura 1. Intervalos y segmentos de ECG. </p>

### Electrocardiograma

<p align="justify">
El electrocardiograma (ECG) es un método diagnóstico que captura la actividad eléctrica del corazón a lo largo del tiempo, traduciendo esta información en líneas que se plasman en un papel o una pantalla. Esta actividad es registrada mediante el uso de electrodos colocados en posiciones específicas sobre el tórax y extremidades del paciente, permitiendo así monitorizar el ritmo cardíaco y detectar posibles anomalías.

El registro de un ECG incluye hasta 12 derivaciones estándar, lo cual brinda una visión comprensiva de la actividad eléctrica cardíaca en el plano frontal y horizontal. Estas derivaciones se dividen en derivaciones estándar de las extremidades (I, II, III) y derivaciones aumentadas (aVR, aVL, aVF), que ofrecen distintas vistas del corazón y son esenciales para un análisis detallado del estado eléctrico cardíaco. La configuración de estas derivaciones permite identificar la orientación y magnitud de la actividad eléctrica del corazón desde diferentes ángulos, lo que es crucial para un diagnóstico preciso.
<p align="center"><img src="/ISB/Laboratorios/Imagenes/entregable4/deri.png" width="300" height="300"></p>
<p align="center">Figura 2. Derivaciones.[6] </p>

### Ejercicios

<p align="justify">Aquí va la explicación de los ejercicios.</p>

## **Objetivos** <a name="id1"></a>
---
Los objetivos del laboratorio son:
* Adquirir señales biomédicas de ECG.
* Hacer una correcta configuración de BiTalino.
* Extraer la información de las señales ECG del software OpenSignals (r)evolution 

<div align="center">

## **Materiales y equipos** <a name="id2"></a>
---

|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |

</div>

## **Procedimiento** <a name="id3"></a>

1. Preparación de la zona: Se lavó con agua, jabón y paños la zona en la que se determinó que irían colocados los electrodos.
2. Ubicación de los electrodos: Aquí explicar donde los pusimos y porque, con bibliografía.

</div>
<p align="center"><b>Figura 3. </b> Colocación de electrodos para el plomo I: IN+ (rojo) e IN-(negro) en las muñecas y REF (blanco) en la cresta ilíaca [3].</p>


3. Registro de la señal ECG: Se grabó la señal en 3 momentos
     * Estado basal: Evaluamos en estado de reposo.
     * Respiración prolongada: Evaluamos al mantener la respiración por 10 segundos y reposo basal.
     * Ejercicio intenso: Evaluamos luego de 5 minutos de abdominales.

       
 
## **Resultados** <a name="id4"></a>
<p align="justify">Antes de proceder con la lectura de los resultados cabe mencionar que el sujeto de estudio, el cual se sometió a diferentes estados de actividad y reposo, tiene una condición la piel que genera ciertas perturbaciones en la señal que se deben tomar en cuenta.</p>

### **Conexión usada** <a name="id5"></a>
#
<p align="justify">Para la conexión de electrodos al cuerpo utilizamos la guía proporcionada por el propio Bitalino de nombre: "BITalino HOME-GUIDE #2 ELECTROCARDIOGRAPHY (ECG) Exploring Cardiac Signals at the Skin Surface" y a su vez la “GUÍA DE PROCEDIMIENTO ASISTENCIAL: TOMA DE ELECTROCARDIOGRAMA DEL HOSPITAL NACIONAL HIPOLITO UNANUE”.</p>

Se posicionaron los electrodos en base las guías mencionadas:
<div align="center">
  <img src="https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/5e54075fb7fb07deb67fbf35833cefc78f600d1a/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/setup.jpeg" alt="Colocación de electrodos" width="300px">
<p align="center">Figura 4. Posición de los electrodos.
     
### **Video de la señal** <a name="id6"></a>
#
1. **Estado basal**: El sujeto se mantuvo en reposo y tranquilo.
2. **Mantener la respiración**: El sujeto de prueba contuvo la respiración por 10 segundos.
3. **Reposo basal**: El sujeto de prueba descansó luego de mantener la respiración.
4. **Después de una actividad física**:El sujeto de prueba realizó ejercicios aeróbicos hasta cansarse (3 minutos).
   
     
|                 **Modelo**                 | **Video** |
|:------------------------------------------:|:---------:|
|                **Estado Basal**                |<video src="https://user-images.githubusercontent.com/128627001/231584957-8ee3fbcc-b6b3-440b-9237-7660d613ff81.mp4"></video>|
| **Manteniendo la respiración por 10 segundos** |<video src="https://user-images.githubusercontent.com/128627001/231585634-4ff1e093-c272-44b3-9570-a781d223fcda.mp4"></video>|
|                **Reposo basal**                |<video src="https://user-images.githubusercontent.com/128627001/231586327-8ea808a1-fc5f-4bc7-bb96-a590a6cf875a.mp4"></video>|
|       **Después de la actividad física**       |<video src="https://user-images.githubusercontent.com/128627001/231586016-d47e613a-6b33-4284-9bc8-8974b8fd2e24.mp4"></video>|

     
### **Archivos** <a name="id8"></a>
#
- [Documentos (.txt)](https://github.com/Grupo2-IntroduccionSenalesMedicas/S_biomedica/tree/main/Programación/Laboratorio%204)
- [Programa de ploteo](https://github.com/Grupo2-IntroduccionSenalesMedicas/S_biomedica/blob/main/Programación/Laboratorio%204/SignalPlot.ipynb)
- [Programa de ploteo en Google Colab](https://colab.research.google.com/drive/1u2PKFSx2E9Nheg8XYQldKUHyYO6rB3Q5?usp=sharing) 
     
### **Ploteo de la señal en Python** <a name="id9"></a>
<p align="justify">Se ha realizado un ploteo de las señales en python para poder analizar segmentos específicos. Para poder calcular los latidos por minuto (lpm) y compararlos con el dispositivo patron, se calculó el intervalo R-R en las señales. En un electrocardiograma con ritmo regular el cálculo es simple, solo hay que dividir 6000 entre la frecuencia cardiaca. Además, se permite observar las frecuencias de la señal.</p>
La señales se sometieron a un filtrado pasa baja y el efecto que se obtuvo fue mínimo, esto debido al existente acondicionamiento que integra el BITalino. Es por este motivo que el análisis realizado fue directamente de las señales sin procesado.

#### a) Estado basal

| **Señal**            | **Raw Signal** | **Fourier Transform** | **Processed Signal** |
|----------------------|----------------|-----------------------|----------------------|
| **D1 - Estado basal** | ![Raw signal D1](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/estado_basal/D1/raw2.png) | ![Fourier Transform D1](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/estado_basal/D1/ft2.png) | ![Processed Signal D1](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/estado_basal/D1/proce3.png) |
| **D2 - Estado basal** | ![Raw signal D2](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/estado_basal/D2/raw1.png) | ![Fourier Transform D2](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/estado_basal/D2/ft2.png) | ![Processed Signal D2](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/estado_basal/D2/proce1.png) |
| **D3 - Estado basal** | ![Raw signal D3](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/estado_basal/D3/raw1.png) | ![Fourier Transform D3](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/estado_basal/D3/ft1.png) | ![Processed Signal D3](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/estado_basal/D3/proce1.png) |

En estado basal, el usuario se encontraba en reposo por lo cuál el valor de R-R es 0.98s que equivale a 61 latidos por minuto que esta dentro del rango normal de palpitaciones cardiacas.</p>

#### b)  Manteniendo la respiración por 10 segundos

| **Señal**            | **Raw Signal** | **Fourier Transform** | **Processed Signal** |
|----------------------|----------------|-----------------------|----------------------|
| **D1 - Ejercicio (post)** | ![Raw signal D1](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/b2c66f57bfbc3f1187102f2b4a360bdbd339e289/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/respiracion/D1/raw3.png) | ![Fourier Transform D1](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/b2c66f57bfbc3f1187102f2b4a360bdbd339e289/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/respiracion/D1/ft3.png) | ![Processed Signal D1](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/b2c66f57bfbc3f1187102f2b4a360bdbd339e289/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/respiracion/D1/proce3.png) |
| **D2 - Ejercicio (post)** | ![Raw signal D2](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/respiracion/D2/raw.png) | ![Fourier Transform D2](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/respiracion/D2/ft.png) | ![Processed Signal D2](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/respiracion/D2/proce.png) |
| **D3 - Ejercicio (post)** | ![Raw signal D3](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/respiracion/D3/raw.png) | ![Fourier Transform D3](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/respiracion/D3/ft.png) | ![Processed Signal D3](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/respiracion/D3/proce.png) |

En este parámetro, el usuario contuvo la respiración durante 10 segundos por lo cuál el valor del intervalo R-R es de 0.9s que equivale a 67 latidos por minuto.</p> 

#### c) Después de una actividad física

| **Señal**            | **Raw Signal** | **Fourier Transform** | **Processed Signal** |
|----------------------|----------------|-----------------------|----------------------|
| **D1 - Respiración (post)** | ![Raw signal D1](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/b2c66f57bfbc3f1187102f2b4a360bdbd339e289/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/post_ejercicio/D1/raw.png) | ![Fourier Transform D1](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/b2c66f57bfbc3f1187102f2b4a360bdbd339e289/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/post_ejercicio/D1/ft.png) | ![Processed Signal D1](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/b2c66f57bfbc3f1187102f2b4a360bdbd339e289/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/post_ejercicio/D1/proce.png) |
| **D2 - Respiración (post)** | ![Raw signal D2](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/post_ejercicio/D2/raw.png) | ![Fourier Transform D2](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/post_ejercicio/D2/ft.png) | ![Processed Signal D2](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/post_ejercicio/D2/proce.png) |
| **D3 - Respiración (post)** | ![Raw signal D3](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/post_ejercicio/D3/raw.png) | ![Fourier Transform D3](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/post_ejercicio/D3/ft.png) | ![Processed Signal D3](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/88b6efb04a00bb0f66d4c0b0a4ddb6df55e027b2/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/post_ejercicio/D3/proce.png) |

Inmediatamente, después de la actividad física de 5 minutos, el intervalo R-R es de 0.45 que equivale a 133 latidos por minuto.</p> 

### **Señal del Promsim4 (dispositivo de metrología que genera una señal patrón)** <a name="id9"></a>

<div align="center">

| **Frecuencia (BPM)** | **Señal**                                                                                                           | **Video**                                                                                                             |
|----------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| **60 BPM**            | ![Señal 60 BPM](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/c3abe242220634df98239676713d727e5e407712/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/fluke/60bpm/proce.png) | [Ver Video 60 BPM](https://github.com/Peeta18/ISB_Grupo3/blob/c3abe242220634df98239676713d727e5e407712/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/fluke/60bpm/60bpm.mp4) |
| **90 BPM**            | ![Señal 90 BPM](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/c3abe242220634df98239676713d727e5e407712/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/fluke/150bpm/proce.png) | [Ver Video 90 BPM](https://github.com/Peeta18/ISB_Grupo3/blob/c3abe242220634df98239676713d727e5e407712/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/fluke/90bpm/90bpm.mp4) |
| **120 BPM**           | ![Señal 120 BPM](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/c3abe242220634df98239676713d727e5e407712/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/fluke/90bpm/proce.png) | [Ver Video 120 BPM](https://github.com/Peeta18/ISB_Grupo3/blob/c3abe242220634df98239676713d727e5e407712/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/fluke/120bpm/120bpm.mp4) |
| **150 BPM**           | ![Señal 150 BPM](https://raw.githubusercontent.com/Peeta18/ISB_Grupo3/c3abe242220634df98239676713d727e5e407712/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/fluke/120bpm/proce.png) | [Ver Video 150 BPM](https://github.com/Peeta18/ISB_Grupo3/blob/c3abe242220634df98239676713d727e5e407712/ISB/Laboratorios/L5_adquisicion_se%C3%B1al_ecg/fotos_y_videos/fluke/150bpm/150bpm.mp4) |



</div>
     
## **Conclusiones** <a name="id10"></a>
* Aquí van las conclusiones

---
## **Referencias** <a name="id11"></a>
---
[1] 
[2] 
[3] 
[4] 
[5] 
‌
