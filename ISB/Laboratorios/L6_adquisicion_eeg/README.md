# **Laboratorio 5: Electroencefalograma**
### Fecha: 19/04/2023

# **Tabla de contenidos**
1. [Introducción al laboratorio](#id0)\
1.1 [¿Qué es EEG?](#id1)\
1.2 [Aplicaciones](#id2)\
1.3 [Tipos de medición de EEG](#id3)\
2. [Objetivos](#id5)
3. [Materiales y equipos](#id6)
4. [Procedimiento](#id7)\
4.1 [Medición y Adquisición por electrodos](#id8)\
4.2 [Protocolo de adquisición](#id9)
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

Montaje Monopolar o Referencial: En esta configuración, se mide la diferencia de potencial entre un electrodo colocado sobre una región activa del cerebro y un electrodo de referencia en una zona neutra. Es ideal para detectar la actividad en áreas específicas del cerebro y es muy utilizado en estudios clínicos que requieren la identificación precisa de zonas de interés cerebral.

Montaje Bipolar: Este método mide la diferencia de potencial entre dos electrodos activos colocados en distintas zonas del cuero cabelludo. Es eficaz para registrar variaciones locales en la actividad cerebral y se utiliza comúnmente para detectar patrones que surgen de interacciones entre áreas cercanas del cerebro.

Montaje Laplaciano: Este montaje compara la señal de un electrodo con el promedio de los electrodos cercanos, mejorando la precisión espacial y reduciendo el ruido. Se emplea para detectar actividad cerebral más localizada y ofrece una mejor discriminación de fuentes de señal cercanas entre sí.

Montaje de Promedio Referencial: Aquí, cada electrodo se compara con el promedio de la actividad registrada en todos los electrodos, lo que permite una medición más global. Es útil para obtener una visión general del cerebro y minimizar artefactos derivados de la actividad cerebral no deseada.

Montaje Stereoelectroencefalografía (sEEG): Este método implica la inserción de electrodos en el cerebro para registrar la actividad de áreas profundas. Se utiliza principalmente en casos de epilepsia intratable o para estudios prequirúrgicos, proporcionando información detallada sobre la actividad cerebral interna.

Montaje de la Red Internacional 10-20: Esta configuración estandarizada se basa en un sistema de proporciones de la cabeza para la colocación precisa de electrodos. Es ampliamente utilizado tanto en la práctica clínica como en la investigación, ya que permite un registro consistente y reproducible de la actividad cerebral global.
<p align="center"> <img src="https://i.imgur.com/qgZ7UsC.jpg" width="60%" /></p>
<p align="center"> Figura 4. Montaje para registro: (a) Monopolar (b) Bipolar.[5]</p>

    
## **Objetivos** <a name="id5"></a>
- Establecer un conocimiento teórico y práctico sobre la utilización y adquisición de señales EEG.
- Adquirir señales EEG biomédicas

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

## **Procedimiento** <a name="id7"></a>

### **Medición y Adquisición por electrodos** <a name="id8"></a>
De manera general, los métodos de adquisición de señales EEG diseñados en el presente laboratorio utilizarán el estándar de posicionamiento 10/20 el cual se describe a continuación:

<p align="center"> Sistema 10/20 <img src="https://i.imgur.com/0O6KnqV.jpg" width="100%" /> </p>
<p align="center"> Figura 5. Distribución de electrodos. [8] </p>

**Tipo de electrodo:** El electrodo del Bitalino es un sensor bipolar (conjuntos de dos pines de medición más una referencia) que mide las diferencias de potencial entre dos electrodos adyacente.Algunas consideraciones son:</p>
    - La alta amplificación (ganancia=40000) lo hace muy sensible a los artefactos circundantes como la luz, los movimientos y las fuentes de alimentación (ruido de línea de 50/60 Hz).</p>
    - La señal medida es la diferencia amplificada entre las dos señales de medición, que se filtra con un paso de banda de 0,8 a 48 Hz para eliminar las señales comunes no deseadas.</p>
    - La piel debe estar debidamente preparada antes de la adherencia de los electrodos.Para ello, es necesario una desinfección de la piel para eliminar las partículas viejas así como la eliminación del vello.



### **Protocolo de adquisición** <a name="id9"></a>
La adquisición y medición de señal EEG  en BITalino es un proceso que implica la utilización de un dispositivo de adquisición de datos llamado BITalino y el conjunto de sensores EEG los cuales son capaces de adquirir señales bioeléctricas del cerebro y convertirlas en señales digitales que pueden ser analizadas por el software especializado OpenSignal. A continuación se detalla el procedimiento realizado para la adquisición y medición de la señal:

1. **Posición de electrodo bipolar (fp1-fp2)**
    <p align="center"> <img src="https://i.imgur.com/8IGiiIx.png" width="50%" /></p>
    
    <p align="center"> Figura 6. Colocación de electrodos EEG del Bitalino. </p>

2. **Adquisición de datos**
    1. Abrir el software OpenSignals y conectar el Bitalino
    2. Conectar el sensor EEG al canal especificado del Bitalino según la ficha técnica.
    3. Colocar los electrodos húmedos con el debido gel en los pines de los sensores EEG.
    4. Colocar los electrodos instalados en la zona fp1 y fp2 de la cabeza del participante. Tener en cuenta las recomendaciones del tipo de electrodo detallado en la sección anterior.
    5. Color el electrodo de referencia en la zona interoposterior de la oreja.
    6. Empezar con el procedimiento de registro:</p>
        a. Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal,sin movimientos oculares/ojos cerrados) durante 30 segundos.</p>
        b.  Repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambasfases durante cinco segundos.</p>
        c. Registre otra fase de referencia de 30 segundos (paso 1).</p>
        d. Que uno de tus compañeros lea en voz alta una serie de ejercicios matemáticos (verindicaciones abajo) y resuelve cada uno de ellos mentalmente enfocando tu mirada en unpunto específico para evitar artefactos.</p>
        <p align="center"> <img src="https://i.imgur.com/Ulv3Rrn.jpg" width="100%" /></p>
        <p align="center"> Figura 7. Preguntas de distinta complejidad. </p>
        e. Detenga la grabación y guarde sus datos.</p>
    7. Como una adquisición extra de señales, seguir los siguientes pasos:</p>
        a. Vendar los ojos al sujeto de estudio por 30 segundos.</p>
        b. Usar una luz intermitente y ver la reacción de la vista del sujeto.</p>
        c. Recolectar las señales y guardar la información.</p>


Cabe mencionar que el procedimiento se repitió en diferentes sujetos de estudio.

 
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
<p align="center"><img src="/ISB/Laboratorios/Imagenes/entregable5/S1.png" width="100%"></p>
<p align="center"><img src="/ISB/Laboratorios/Imagenes/entregable5/S2.png" width="100%"></p>
<p align="center"><img src="/ISB/Laboratorios/Imagenes/entregable5/S3.png" width="100%"></p>
<p align="center"><img src="/ISB/Laboratorios/Imagenes/entregable5/S4.png" width="100%"></p>
<p align="center"><img src="/ISB/Laboratorios/Imagenes/entregable5/S5.png" width="100%"></p>

En el Bitalino, al realizar la medición, trabajan con un sensor de EEG el cuál brinda la señal medida como la diferencia amplificada entre las dos señales de medición que se filtra con un paso de banda de 0,8-48Hz para eliminar la señales no deseadas.[3]
Asimismo, al considerar la posición de los electrodos del Bitalino los cuales fueron en fp1 y fp2, estas regiones están relacionadas con diversas funciones cognitivas y emocionales.
De las 5 gráficas la que tiene mayor amplitud es en la que se expone al sujeto a una luz parpadeante luego de tener los ojos vendados por un periodo de tiempo.


## **Conclusiones** <a name="id17"></a>
---
- 
- 
    
## **Referencias** <a name="id18"></a>
[1] J. Gray, "The 5 Types of Brain Waves," DIY Genius. [En línea]. Disponible en: https://www.diygenius.com/the-5-types-of-brain-waves/. Fecha de acceso: 25-sep-2024.
[2] Mayo Clinic Staff, "Electroencefalograma (EEG)," Mayo Clinic. [En línea]. Disponible en: https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875. Fecha de acceso: 25-sep-2024.

‌
‌

