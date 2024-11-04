# LAB 9: PROCESAMIENTO DE SEÑALES EMG

#### **Tabla de Contenido**
1. [Introducción](#introduccion)
2. [Objetivos](#objetivos)
3. [Materiales](#materiales)
4. [Procedimiento](#procedimiento)
5. [Resultados](#resultados)
6. [Discusión](#discusion)
7. [Conclusiones](#conclusiones)
8. [Bibliografía](#bibliografia)

## Introducción

La electromiografía de superficie (sEMG) es una técnica de registro que permite analizar la actividad eléctrica de los músculos a través de la piel, proporcionando una herramienta no invasiva para el estudio de los procesos neuromusculares. Su aplicación es especialmente relevante en el ámbito de la rehabilitación y la detección de condiciones musculares, como la sarcopenia. Según estudios recientes, las señales de sEMG pueden revelar cambios en la función neuromuscular asociados al envejecimiento y a la disminución de masa muscular, característicos de esta condición. Esta tecnología también ha mostrado potencial para el desarrollo de algoritmos de aprendizaje automático que ayudan en la clasificación y diagnóstico de estas condiciones en poblaciones mayores, permitiendo enfoques más precisos y personalizados en la atención clínica&#8203;:contentReference[oaicite:0]{index=0}.

La extracción de características de las señales sEMG incluye el uso de transformadas y análisis de la entropía, que ayudan a identificar patrones específicos de actividad muscular, facilitando así la clasificación de movimientos y el control de dispositivos de asistencia robótica en la rehabilitación. Estos métodos, combinados con técnicas de optimización y algoritmos de aprendizaje automático como las máquinas de soporte vectorial (SVM), permiten reconocer movimientos específicos a partir de patrones de sEMG, mejorando la precisión en aplicaciones de rehabilitación asistida&#8203;:contentReference[oaicite:1]{index=1}&#8203;:contentReference[oaicite:2]{index=2}.

El presente trabajo explora el uso de sEMG para la detección de patrones de actividad muscular y su procesamiento mediante algoritmos avanzados, con el objetivo de contribuir al desarrollo de herramientas diagnósticas y sistemas de rehabilitación en el contexto de enfermedades musculares y neuromusculares.


## Objetivos <a name="objetivos"></a>
- Diseñar un filtro adecuado para señales EMG utilizando técnicas avanzadas.
- Extraer y analizar características relevantes de señales EMG, aplicando métodos de normalización y cálculo de parámetros.

## Materiales <a name="materiales"></a>
| Material | Cantidad |
|----------|----------|
| Software de procesamiento de datos (*Python*) | N.A |

