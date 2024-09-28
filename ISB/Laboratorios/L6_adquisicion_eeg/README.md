# **Laboratorio 5: Electroencefalograma**
### Fecha: 19/04/2023

# **Tabla de contenidos**
1. [Introducción al laboratorio](#id0)\
1.1 [¿Qué es EEG?](#id1)\
1.2 [Aplicaciones](#id2)\
1.3 [Tipos de medición de EEG](#id3)\
2. [Objetivos](#id5)
3. [Materiales y equipos](#id6)
4. [Metodología](#id7)\
5. [Resultados](#id10)\
5.1 [Fotos de conexión usada](#id11)\
5.2 [Señal con MarckOpenBCI4](#id12)\
    5.2.1 [Gráficas del OpenBCI](#id13)\
5.3 [Señal con Bitalino](#id14)\
    5.3.1 [Videos utilizando el Bitalino](#id15)\
    5.3.2 [Análisis de gráficas](#id16)
6. [Conclusiones](#id17)
7. [Referencias](#id18)

## **Introducción al laboratorio** <a name="id0"></a>


### ¿Qué es el EEG? <a name="id1"></a>
<p align="justify"> La electroencefalografía (EEG) es una técnica de neuroimagen que registra la actividad eléctrica del cerebro mediante electrodos colocados en el cuero cabelludo. Esta técnica es esencial para el diagnóstico y monitoreo de trastornos neurológicos como la epilepsia, así como para la investigación de procesos cognitivos y estados de conciencia.

Las ondas cerebrales detectadas por el EEG se clasifican según su frecuencia y están asociadas a diferentes estados mentales y niveles de actividad cerebral.
</p>

<p align="center"> 
    
| **_Tipos de Frecuencia de Ondas Cerebrales_** | **_Frecuencia (Hz)_** |Estado del cerebro|
|:---------------------------------------------:|:---------------------:|:------------:|
|               Ondas Delta                     |          0.5 - 4      |Sueño profundo, inconsciencia|
|               Ondas Theta                     |            4 - 8      |Somnolencia, meditación profunda, sueño ligero |
|               Ondas Alpha                     |       8 - 13          |Relajación, estado de reposo, meditación|
|                Ondas Beta                     |       13 - 22         |Atención, alerta, concentración activa|
|               Ondas Gamma                     |       22 - 30         |Procesamiento cognitivo elevado, percepción consciente|

</p>
    
Las ondas delta (0.5 - 4 Hz) son las más lentas y se asocian con el sueño profundo y la regeneración celular. Se observan durante las fases de sueño profundo sin sueños, siendo esenciales para la curación física y la consolidación de la memoria.

Las ondas theta (4 - 8 Hz) aparecen en estados de somnolencia, sueño ligero o meditación profunda. Estas ondas están relacionadas con la creatividad, la intuición y el acceso al subconsciente, facilitando la resolución de problemas y la relajación profunda.

Las ondas alfa (8 - 13 Hz) se manifiestan cuando estamos relajados pero despiertos, como en momentos de calma mental o meditación ligera. Representan un estado de reposo consciente, común cuando cerramos los ojos y nos encontramos tranquilos sin realizar tareas activas.

Las ondas beta (13 - 30 Hz) son más rápidas y están vinculadas con la actividad mental intensa, el pensamiento lógico, la concentración y el procesamiento activo de información. Estas ondas predominan cuando estamos atentos, resolviendo problemas o bajo estrés.

Las ondas gamma (30 - 100 Hz) son las más rápidas y están asociadas con el procesamiento cognitivo elevado y la percepción consciente. Están involucradas en la integración de la información entre distintas áreas del cerebro y son fundamentales para funciones cognitivas como la atención, la memoria y el aprendizaje.

<p align="center">
  <img src="https://github.com/user-attachments/assets/ea92704d-366b-4d97-85f7-de37db7e7831" alt="Señales"/>
</p>

<p align="center"> Figura 1. Clasificación de los tipos de ondas.[1]</p>

### Aplicaciones <a name="id2"></a>
---
<p align="justify"> El electroencefalograma (EEG) tiene múltiples aplicaciones en el ámbito clínico, de investigación y tecnológico. Es un pilar para el diagnóstico y monitoreo de trastornos neurológicos como la epilepsia, los trastornos del sueño y otros desórdenes que afectan la actividad cerebral. Además, se utiliza ampliamente en la investigación neurocientífica para estudiar procesos cognitivos como la atención y la memoria, gracias a su alta resolución temporal. También es clave en el desarrollo de interfaces cerebro-computadora (BCI), permitiendo a personas con discapacidades motoras controlar dispositivos externos mediante la actividad cerebral. Finalmente, el EEG es esencial en el análisis del sueño, ayudando a diagnosticar y tratar trastornos como la apnea o el insomnio. [2]</p>

### Tipos de medición de EEG <a name="id3"></a>
___
Las mediciones de EEG (Electroencefalograma) se clasifican en varios tipos según la configuración y el montaje de los electrodos. Estas configuraciones definen cómo los electrodos están colocados en el cuero cabelludo y cómo se mide la actividad eléctrica cerebral. Los principales tipos de configuración de electrodos en EEG son:

- Montaje Monopolar o Referencial: En esta configuración, se mide la diferencia de potencial entre un electrodo colocado sobre una región activa del cerebro y un electrodo de referencia en una zona neutra. Es ideal para detectar la actividad en áreas específicas del cerebro y es muy utilizado en estudios clínicos que requieren la identificación precisa de zonas de interés cerebral.

- Montaje Bipolar: Este método mide la diferencia de potencial entre dos electrodos activos colocados en distintas zonas del cuero cabelludo. Es eficaz para registrar variaciones locales en la actividad cerebral y se utiliza comúnmente para detectar patrones que surgen de interacciones entre áreas cercanas del cerebro.

- Montaje Laplaciano: Este montaje compara la señal de un electrodo con el promedio de los electrodos cercanos, mejorando la precisión espacial y reduciendo el ruido. Se emplea para detectar actividad cerebral más localizada y ofrece una mejor discriminación de fuentes de señal cercanas entre sí.

- Montaje de Promedio Referencial: Aquí, cada electrodo se compara con el promedio de la actividad registrada en todos los electrodos, lo que permite una medición más global. Es útil para obtener una visión general del cerebro y minimizar artefactos derivados de la actividad cerebral no deseada.

- Montaje Stereoelectroencefalografía (sEEG): Este método implica la inserción de electrodos en el cerebro para registrar la actividad de áreas profundas. Se utiliza principalmente en casos de epilepsia intratable o para estudios prequirúrgicos, proporcionando información detallada sobre la actividad cerebral interna.

- Montaje de la Red Internacional 10-20: Esta configuración estandarizada se basa en un sistema de proporciones de la cabeza para la colocación precisa de electrodos. Es ampliamente utilizado tanto en la práctica clínica como en la investigación, ya que permite un registro consistente y reproducible de la actividad cerebral global.
<div align="center">
  <img src="https://github.com/user-attachments/assets/3d7e9274-757d-4f67-ad04-f852232bf483" alt="monopolar" />
</div>

<p align="center"> Figura 4. Montaje para registro Monopolar.</p>

    
## **Objetivos** <a name="id5"></a>
- 
- 

---

## **Materiales y equipos** <a name="id6"></a>

<center>
    
|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |  Kit BITalino   |      1       |
|      -       |     Laptop      |      1       |
|      OpenBCI       |     Ultracortex Mark IV EEG Headset      |      1       |
|      OpenBCI       |     OpenBCI Cyton 8-channel Board      |      1       |
|      Inkafarma       |     Electrodos con gel      |      3       |

</center>

## **Metodología** <a name="id7"></a>


1. **Posición de electrodo bipolar (fp1-fp2)**
    <p align="center"> <img src="https://i.imgur.com/8IGiiIx.png" width="50%" /></p>
    
    <p align="center"> Figura 6. Colocación de electrodos EEG del Bitalino. </p>

# Metodología de Registro EEG en Voluntarios

Para el experimento, se utilizó un procedimiento con **dos voluntarios** y **dos tipos de equipamiento**. En ambos casos, los voluntarios siguieron los mismos pasos, descritos a continuación.

## Protocolo de Captura de Señal EEG (Común a Ambos Equipos)
1. **Registro de Línea Base (30 segundos)**:
   - El voluntario se mantuvo en reposo, con respiración normal y ojos cerrados. Se registró una señal limpia, con poco ruido y sin movimientos durante 30 segundos.
   
2. **Ciclo de OJOS ABIERTOS - OJOS CERRADOS**:
   - Se repitió el ciclo de abrir y cerrar los ojos cinco veces. Cada fase (ojos abiertos y cerrados) duró cinco segundos.
   
3. **Registro de Línea Base (30 segundos)**:
   - Se repitió el paso 1 para obtener una nueva referencia de la señal EEG.

4. **Resolución de Problemas Matemáticos**:
   - Mientras el voluntario mantenía la vista fija en un punto, otro compañero leyó una serie de ejercicios matemáticos (3 simples y 3 complejos) que el voluntario debía resolver mentalmente.

5. **Finalización del Registro**:
   - Se detuvo la grabación y se guardaron los datos obtenidos.

---

## Procedimiento 1: Captura de EEG con Kit BITalino (R)evolution

Para este procedimiento, se utilizó el Kit BITalino (R)evolution conectado a una laptop mediante **Bluetooth**. La secuencia de preparación y registro fue la siguiente:

1. **Instalación de Software**:
   - Se descargó e instaló la plataforma **OpenSignals** para la adquisición y visualización de los datos EEG.

2. **Alimentación del Kit BITalino**:
   - La tarjeta BITalino se alimentó utilizando una **batería de litio** incluida en el kit de compra.

3. **Conexión de Electrodos**:
   - Se conectaron **3 electrodos** (Positivo, Negativo y Referencia) a la placa de sensado del kit a través del conector correspondiente en el canal de EEG.

4. **Conexión Bluetooth**:
   - Se estableció una conexión Bluetooth entre la tarjeta BITalino y la laptop.

5. **Colocación de Electrodos en el Voluntario**:
   - Se colocaron los electrodos de la siguiente manera:
     - **2 electrodos frontales**: ubicados por encima de cada ceja.
     - **1 electrodo de referencia**: colocado por debajo de la oreja derecha.

6. **Ejecución del Protocolo EEG**:
   - Una vez realizadas todas las conexiones, se procedió a ejecutar los pasos detallados anteriormente para la captura de señal EEG en el voluntario.

---

## Procedimiento 2: Captura de EEG con UltraCortex MARK IV y Tarjeta Cyton

Para el segundo procedimiento, se utilizó el casco **UltraCortex MARK IV** junto a la tarjeta **Cyton**, y la secuencia de preparación fue la siguiente:

1. **Instalación de Software**:
   - Se descargó e instaló la plataforma **OpenBCI GUI** para la adquisición y visualización de los datos EEG.

2. **Alimentación de la Tarjeta Cyton**:
   - La tarjeta Cyton se alimentó utilizando una **batería de litio** incluida en el kit de compra.

3. **Conexión del UltraCortex MARK IV con la Tarjeta Cyton**:
   - Se conectó el casco UltraCortex MARK IV con la tarjeta Cyton.

4. **Ajuste del UltraCortex en el Voluntario**:
   - El casco UltraCortex MARK IV se ajustó en la cabeza del voluntario, siguiendo el **sistema 10-20** para el posicionamiento de los electrodos (voluntario: **profesor Moises**).

5. **Conexión de Laptop y Tarjeta Cyton**:
   - Se conectó la laptop a la tarjeta Cyton para la adquisición de datos.

6. **Ejecución del Protocolo EEG**:
   - Tras realizar todas las conexiones, se ejecutaron los pasos del protocolo general mencionados al inicio de la metodología.


 
## **Resultados** <a name="id10"></a>
___
### 1. **Fotos de conexión usada** <a name="id11"></a>
<p align="center"><img src="/ISB/Laboratorios/Imagenes/entregable5/IMG_20230419_112630.jpg" width=60%></p>
<p align="center">Figura 8. Posición de los electrodos en el Bitalino (vista frontal).</p>

<p align="center"><img src="/ISB/Laboratorios/Imagenes/entregable5/IMG_20230419_112617.jpg" width=60% ></p>

<p align="center">Figura 9. Posición de los electrodos en el vitalino (vista lateral).</p>

<p align="center"><img src="/ISB/Laboratorios/Imagenes/entregable5/IMG_20230419_115212.jpg" width="400" height="600"></p>
<p align="center">Figura 10. Posición de los electrodos del ULTRACORTEX "MARK IV" (vista posterior).</p>

<p align="center"><img src="/ISB/Laboratorios/Imagenes/entregable5/IMG_20230419_115202.jpg" width="400" height="600"></p>
<p align="center">Figura 11. Posición de los electrodos del ULTRACORTEX "MARK IV" (vista posterior).</p>

### 2. **Señal con MarckOpenBCI4** <a name="id12"></a>

#### **Videos con Ultracortex "Mark IV** <a name="id13"></a>

|                 **Fase**                 | **Video** |
|:------------------------------------------:|:---------:|
| **Fase de referencia de 30 segundos**                     |<video src="https://user-images.githubusercontent.com/128627001/233262542-abe3f2d1-9a1c-4e73-bcf2-d244204a3a26.mp4">|
| **Realizando secuencia de OJOS ABIERTOS - OJOS CERRADOS** |<video src="https://user-images.githubusercontent.com/128627001/233263555-8cf4f756-8c59-486e-9940-6db5c5b835cc.mp4">|
|                **Respondiendo preguntas categoría simple** |<video src="https://user-images.githubusercontent.com/128627001/233265792-14ec51f3-7390-4b74-82d9-f2054a0887cf.mp4">|
|                **Respondiendo preguntas categoría compleja (parte 1)** |<video src="https://user-images.githubusercontent.com/128627001/233266949-0d0af3dc-0e56-472a-ab08-0d0c0a24689f.mp4">|
|                **Respondiendo preguntas categoría compleja (parte 2)** |<video src="https://user-images.githubusercontent.com/128627001/233267165-a7fe473c-ae95-4366-bc09-a43da290e3de.mp4">|  

####  **Gráficas del OpenBCI**

<p align="center"><img src="/ISB/Laboratorios/Imagenes/FP1-FP3/1.jpg" width="100%"></p>
<p align="center"><img src="/ISB/Laboratorios/Imagenes/FP1-FP3/2.jpg" width="100%"></p>
<p align="center"><img src="/ISB/Laboratorios/Imagenes/FP1-FP3/3.jpg" width="100%"></p>
<p align="center"><img src="/ISB/Laboratorios/Imagenes/FP1-FP3/4.jpg" width="100%"></p>

<p align="justify">Si analizamos los canales, estos guardan relación con la ubicación 10/20 de un EEG, los canales que van del Fp1-F3-C3-P3-O1 corresponden al hemisferio izquierdo y los canales Fp2-F4-C4-P4-O2 al hemisferio derecho.
Podemos observar que el canal 5 y 6 contiene una mayor amplitud que el resto, estos se encuentran ubicados en el lóbulo frontal derecho, cabe resaltar que el hemisferio derecho izquierdo  lobulo frontal se encarga del pensamiento consciente, atención e inteligencia [9], por ello en los ultimos segundos cuando se empezo a desarrollar la ronde de preguntas se ve un mayor incremento en la amplitud.</p> 
Un caso contrario ocurrió para el canal 1 y 2 donde se observa una mínima amplitud, estos corresponden al FP1-F3-C3 los cuáles se ubican en el lóbulo frontal izquierdo.</p>

<p align="center"><img src="https://i.imgur.com/0MHKduk.png" width="70%"></p>
<p align="center">Figura 12. Explicación de lo que se encarga el hemisferio derecho e izquierdo. [10]</p>

<p align="center"><img src="https://i.imgur.com/I3K4YSs.jpg" width="100%"></p>   
<p align="center">Figura 13. Frecuencias de los 8 canales.</p>

### 3. **Señal con Bitalino** <a name="id14"></a>
####  **Videos utilizando el Bitalino** <a name="id15"></a>
|                 **Fase**                 | **Video** |
|:------------------------------------------:|:---------:|
| **Fase de referencia de 30 segundos**                     |<video src="https://user-images.githubusercontent.com/128627001/233433130-74e1f631-57b8-41d9-8dc4-dcd53a9f2d0f.mp4">|
| **Realizando secuencia de OJOS ABIERTOS - OJOS CERRADOS** |<video src="https://user-images.githubusercontent.com/128627001/233433248-e4648f16-ceac-4c42-b650-0853c8717613.mp4">|
|                **Respondiendo preguntas categoría simple** |<video src="https://user-images.githubusercontent.com/128627001/233433318-5b2c0ddb-5e23-4794-8f56-6cc35eefba0e.mp4">|
|                **Respondiendo preguntas categoría compleja** |<video src="https://user-images.githubusercontent.com/128627001/233433394-42610a9a-4101-4d07-a59d-6cc748af243c.mp4">|
|                **Reacción a la luz artificial** |<video src="https://user-images.githubusercontent.com/128627001/233433534-2aebb116-354d-4ba0-9717-40c2a81b055b.mp4">|
####  **Análisis de las gráficas** <a name="id16"></a>

## **Conclusiones** <a name="id17"></a>
---
- 
- 
    
## **Referencias** <a name="id18"></a>
[1] J. Gray, "The 5 Types of Brain Waves," DIY Genius. [En línea]. Disponible en: https://www.diygenius.com/the-5-types-of-brain-waves/. Fecha de acceso: 25-sep-2024.
[2] Mayo Clinic Staff, "Electroencefalograma (EEG)," Mayo Clinic. [En línea]. Disponible en: https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875. Fecha de acceso: 25-sep-2024.

‌
‌

