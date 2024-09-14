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

### Pruebas en OpenSignals

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


### Gráficas en el Dominio del Tiempo
![Señal EMG en el tiempo - Reposo](ruta/a/tu/imagen1.png)
*Figura 1: Señal EMG durante el reposo.*

![Señal EMG en el tiempo - Actividad 1](ruta/a/tu/imagen2.png)
*Figura 2: Señal EMG durante la Actividad 1.*

![Señal EMG en el tiempo - Actividad 2](ruta/a/tu/imagen3.png)
*Figura 3: Señal EMG durante la Actividad 2.*

### Gráficas en el Dominio de la Frecuencia
![Señal EMG en la frecuencia - Reposo](ruta/a/tu/imagen4.png)
*Figura 4: Transformada de Fourier de la señal EMG en reposo.*

![Señal EMG en la frecuencia - Actividad 1](ruta/a/tu/imagen5.png)
*Figura 5: Transformada de Fourier de la señal EMG durante la Actividad 1.*

![Señal EMG en la frecuencia - Actividad 2](ruta/a/tu/imagen6.png)
*Figura 6: Transformada de Fourier de la señal EMG durante la Actividad 2.*

## Video, Imágenes y Fundamento de la Señal

### Video
[Enlace al video de las pruebas realizadas.](ruta/a/tu/video)

### Fundamento de la Señal
El grupo muscular de interés para este experimento es el [nombre del grupo muscular], seleccionado debido a su [justificación de por qué se eligió este grupo muscular]. Este grupo muscular es esencial para [explicación sobre su relevancia en la actividad estudiada] y nos permitirá obtener señales EMG claras y relevantes para el análisis.

### Imágenes
![Electrodos en el grupo muscular](ruta/a/tu/imagen7.png)
*Figura 7: Colocación de electrodos en el [grupo muscular].*

## Referencias
1. Autor 1, "Título del paper," *Nombre de la Revista*, vol. xx, no. xx, pp. xx-xx, Año.
2. Autor 2, "Título del paper," *Nombre de la Revista*, vol. xx, no. xx, pp. xx-xx, Año.
3. Autor 3, "Título del paper," *Nombre de la Revista*, vol. xx, no. xx, pp. xx-xx, Año.
4. Autor 4, "Título del paper," *Nombre de la Revista*, vol. xx, no. xx, pp. xx-xx, Año.
5. Autor 5, "Título del paper," *Nombre de la Revista*, vol. xx, no. xx, pp. xx-xx, Año.

