# Laboratorio 4 - Adquisición de Señales EMG

## Tabla de Contenidos
1. [Objetivos](#objetivos)
2. [Materiales y Equipos Usados](#materiales-y-equipos-usados)
3. [Setup de las mediciones](#setup-de-las-mediciones)
4. [Resultados](#resultados)
   - [Pruebas](#pruebas)
   - [Gráficas en el Dominio del Tiempo](#gráficas-en-el-dominio-del-tiempo)
   - [Gráficas en el Dominio de la Frecuencia](#gráficas-en-el-dominio-de-la-frecuencia)
5. [Video, Imágenes y Fundamento de la Señal](#video-imágenes-y-fundamento-de-la-señal)
6. [Referencias](#referencias)

## Objetivos
- Adquirir señales biomédicas de EMG y ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolution

## Materiales y Equipos Usados

| Materiales         | Detalles                        | Cantidad |
|--------------------|---------------------------------|----------|
| Kit Bitalino       | (R)Evolution                    | 1        |
| Electrodos         | 4 electrodos de superficie      | 1        |
| Laptop             | Lenovo Thinkpad                 | 1        |

## Setup de las mediciones

| Región Muscular   | Imagen                          |
|-------------------|---------------------------------|
| Dedo              | <img src="./Fotos%20y%20videos/1-1%20-%20Dedo%20en%20reposo/1-1-3.jpeg" alt="Imagen del dedo en reposo" width="400px"> |
| Brazo             | <img src="./Fotos%20y%20videos/2-1%20-%20Brazo%20reposo/2-1-2.jpeg" alt="Imagen del brazo en reposo" width="400px"> |
| Pantorrilla       | <img src="./Fotos%20y%20videos/3-1%20-%20Pantorrilla%20relajada%20en%20reposo/3-1-2.jpeg" alt="Imagen de la pantorrilla relajada en reposo" width="400px"> |
| Antebrazo         | <img src="./Fotos%20y%20videos/4-1%20-%20Antebrazo%20en%20reposo/4-1-1.jpeg" alt="Imagen del antebrazo en reposo" width="400px" style="transform: rotate(-90deg);"> |

## Resultados

### Señales en OpenSignal

#### Prueba 1: Reposo
   
   | Dedo                                              | Brazo                                             |
|---------------------------------------------------|--------------------------------------------------|
| <img src="./Fotos%20y%20videos/1-1%20-%20Dedo%20en%20reposo/1-1-7.gif" alt="GIF del dedo en reposo" width="400px">  | <img src="./Fotos%20y%20videos/2-1%20-%20Brazo%20reposo/2-1-3.gif" alt="GIF del brazo en reposo" width="400px"> |

En la señal obtenida del dedo, observamos una línea prácticamente recta, lo que indica que el músculo se encontraba en reposo o no había actividad muscular significativa durante la adquisición de la señal. Esto es característico de un músculo en estado de reposo, ya que la señal electromiográfica (EMG) es mínima o nula cuando no hay contracción.

Por otro lado, la señal capturada del brazo muestra una actividad oscilatoria que refleja una contracción muscular. Las oscilaciones en la señal representan la actividad eléctrica generada por las fibras musculares al contraerse, lo que indica que el brazo estaba activo durante la adquisición. La mayor frecuencia y amplitud de la señal EMG confirman una contracción muscular activa en el brazo.

#### Prueba 2: Sin oposición

| Dedo                                              | Brazo                                             |
|---------------------------------------------------|--------------------------------------------------|
| <img src="./Fotos%20y%20videos/1-2%20-%20Movimiento%20voluntario%20del%20dedo/1-2-2.gif" alt="GIF del movimiento voluntario del dedo" width="400px">  | <img src="./Fotos%20y%20videos/2-2%20-%20Brazo%20en%20movimiento%20voluntario/2-2-1.gif" alt="GIF del brazo en movimiento voluntario" width="400px"> |

En la señal del movimiento voluntario del dedo, se observan oscilaciones que reflejan la actividad muscular durante la contracción. La amplitud de la señal muestra la activación de las unidades motoras mientras el dedo se mueve, evidenciando una contracción controlada.

Por otro lado, la señal del brazo muestra oscilaciones de mayor amplitud y frecuencia, lo que indica una contracción más intensa. Esta mayor actividad refleja el esfuerzo muscular necesario para mover el brazo, generando una señal EMG más robusta y sostenida.

#### Prueba 3: Con oposición

| Brazo con fuerza                                   | Antebrazo con fuerza                               |
|---------------------------------------------------|--------------------------------------------------|
| <img src="./Fotos%20y%20videos/2-3%20-%20Movimiento%20de%20brazo%20con%20fuerza/2-3-1.gif" alt="GIF del movimiento de brazo con fuerza" width="400px">  | <img src="./Fotos%20y%20videos/4-3%20-%20Antebrazo%20en%20movimiento%20con%20fuerza/4-3-1.gif" alt="GIF del antebrazo en movimiento con fuerza" width="400px"> |

En la señal del movimiento del brazo con fuerza, se observa un incremento significativo en la amplitud y frecuencia de las oscilaciones, lo que refleja una mayor activación de las fibras musculares. Esta señal indica un esfuerzo muscular considerable, generado por la contracción sostenida del músculo al aplicar fuerza durante el movimiento.

De manera similar, en la señal del antebrazo en movimiento con fuerza, se visualizan oscilaciones densas y de alta amplitud, que representan la contracción intensa del músculo del antebrazo. La alta actividad electromiográfica capturada refleja la necesidad de mayor reclutamiento muscular para ejecutar el movimiento con fuerza, comparado con un movimiento más suave o en reposo.


### Gráficas en el dominio de la frecuencia

| Dedo con oposición                                               | Brazo sin oposición                                                 | Antebrazo con oposición                                               |
|------------------------------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------------|
| ![Dedo - Con oposición](https://github.com/Peeta18/ISB_Grupo3/blob/c5fde3c2ca0f6d93bd5c6b4f28c96dddf2c606c3/ISB/Laboratorios/L4_adquisicion_se%C3%B1al_emg/Fotos%20y%20videos/1-3%20-%20Movimiento%20ejerciendo%20fuerza/ft.png)  | ![Brazo - Sin oposición](https://github.com/Peeta18/ISB_Grupo3/blob/c5fde3c2ca0f6d93bd5c6b4f28c96dddf2c606c3/ISB/Laboratorios/L4_adquisicion_se%C3%B1al_emg/Fotos%20y%20videos/2-2%20-%20Brazo%20en%20movimiento%20voluntario/ft.png)  | ![Antebrazo - Con oposición](https://github.com/Peeta18/ISB_Grupo3/blob/859505e24b96cf0eaba71b5b6a983df9d61c0004/ISB/Laboratorios/L4_adquisicion_se%C3%B1al_emg/Fotos%20y%20videos/4-3%20-%20Antebrazo%20en%20movimiento%20con%20fuerza/ft.png)  |


### Gráficas en el Dominio del Tiempo

| Grupo Muscular | Condición       | Señal Raw                                         | Señal Procesada                                   |
|----------------|-----------------|--------------------------------------------------|--------------------------------------------------|
| **Dedo**       | Reposo           | <img src="./Fotos%20y%20videos/1-1%20-%20Dedo%20en%20reposo/raw.png" width="400px"> | <img src="./Fotos%20y%20videos/1-1%20-%20Dedo%20en%20reposo/proc.png" width="400px"> |
| **Dedo**       | Sin oposición    | <img src="./Fotos%20y%20videos/1-2%20-%20Movimiento%20voluntario%20del%20dedo/raw.png" width="400px"> | <img src="./Fotos%20y%20videos/1-2%20-%20Movimiento%20voluntario%20del%20dedo/proce.png" width="400px"> |
| **Dedo**       | Con oposición    | <img src="./Fotos%20y%20videos/1-3%20-%20Movimiento%20ejerciendo%20fuerza/raw.png" width="400px"> | <img src="./Fotos%20y%20videos/1-3%20-%20Movimiento%20ejerciendo%20fuerza/proce.png" width="400px"> |
| **Brazo**      | Reposo           | <img src="./Fotos%20y%20videos/2-1%20-%20Brazo%20reposo/raw.png" width="400px"> | <img src="./Fotos%20y%20videos/2-1%20-%20Brazo%20reposo/proce.png" width="400px"> |
| **Brazo**      | Sin oposición    | <img src="./Fotos%20y%20videos/2-2%20-%20Brazo%20en%20movimiento%20voluntario/raw.png" width="400px"> | <img src="./Fotos%20y%20videos/2-2%20-%20Brazo%20en%20movimiento%20voluntario/proce.png" width="400px"> |
| **Brazo**      | Con oposición    | <img src="./Fotos%20y%20videos/2-3%20-%20Movimiento%20de%20brazo%20con%20fuerza/raw.png" width="400px"> | <img src="./Fotos%20y%20videos/2-3%20-%20Movimiento%20de%20brazo%20con%20fuerza/proce.png" width="400px"> |
| **Antebrazo**  | Reposo           | <img src="./Fotos%20y%20videos/4-1%20-%20Antebrazo%20en%20reposo/raw.png" width="400px"> | <img src="./Fotos%20y%20videos/4-1%20-%20Antebrazo%20en%20reposo/proce.png" width="400px"> |
| **Antebrazo**  | Sin oposición    | <img src="./Fotos%20y%20videos/4-2%20-%20Antebrazo%20en%20movimiento%20voluntario/raw.png" width="400px"> | <img src="./Fotos%20y%20videos/4-2%20-%20Antebrazo%20en%20movimiento%20voluntario/proce.png" width="400px"> |
| **Antebrazo**  | Con oposición    | <img src="./Fotos%20y%20videos/4-3%20-%20Antebrazo%20en%20movimiento%20con%20fuerza/raw.png" width="400px"> | <img src="./Fotos%20y%20videos/4-3%20-%20Antebrazo%20en%20movimiento%20con%20fuerza/proce.png" width="400px"> |

#### Dedo
En las condiciones del dedo, se observa una baja actividad en reposo, como era de esperar. La señal "Raw" refleja esta baja actividad, y la señal procesada la confirma tras el filtrado, mostrando una señal limpia y sin artefactos. Durante el movimiento sin oposición, la señal "Raw" comienza a mostrar oscilaciones asociadas con la activación muscular, pero también contiene ruido. Tras el filtrado, la señal procesada resalta claramente los momentos de activación muscular, eliminando el ruido. En la condición de oposición, la señal "Raw" muestra una actividad más intensa y oscilaciones de mayor amplitud, reflejo del esfuerzo muscular. La señal procesada limpia esta actividad, permitiendo observar con precisión los picos de contracción muscular bajo esfuerzo.

#### Brazo
Para el brazo, en reposo, la señal "Raw" muestra una actividad baja, acorde a la ausencia de contracción muscular. La señal procesada confirma que no hay ruido relevante en esta condición. En la condición sin oposición, la señal "Raw" presenta una estructura de activación muscular más evidente, aunque algo contaminada por ruido. La señal procesada elimina este ruido, mostrando los momentos clave de contracción muscular. Al aplicar fuerza en el movimiento con oposición, la señal "Raw" refleja un aumento significativo en la actividad muscular, con oscilaciones amplias. La señal procesada resalta estas contracciones intensas, eliminando el ruido y ofreciendo una imagen clara del esfuerzo realizado.

#### Antebrazo
En el reposo del antebrazo, la señal "Raw" muestra baja actividad muscular, como era de esperar. La señal procesada confirma la ausencia de ruido y mantiene la baja actividad del músculo en reposo. Durante el movimiento sin oposición, la señal "Raw" muestra oscilaciones que indican actividad muscular, pero con cierto nivel de ruido. La señal procesada, tras el filtrado, ofrece una visualización más clara de los picos de activación. Finalmente, en la condición de oposición, la señal "Raw" refleja una activación muscular significativa con oscilaciones amplias. La señal procesada elimina los artefactos y ruido, destacando los momentos clave de contracción durante el esfuerzo muscular intenso.

## Referencias
1. Campanini, I., Merlo, A., Disselhorst-Klug, C., Mesin, L., Muceli, S., & Merletti, R. (2022). Fundamental Concepts of Bipolar and High-Density Surface EMG Understanding and Teaching for Clinical, Occupational, and Sport Applications: Origin, Detection, and Main Errors. Sensors (Basel, Switzerland), 22(11), 4150. https://doi.org/10.3390/s22114150
2. Da Silva, H. P., Guerreiro, J., Lourenço, A., Fred, A., & Martins, R. (2014, January). BITalino: A novel hardware framework for physiological computing. In International Conference on Physiological Computing Systems (Vol. 2, pp. 246-253). SciTePress.

