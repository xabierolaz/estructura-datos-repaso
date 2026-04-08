# Resumen teorico autocontenido

Esta carpeta esta pensada para preparar la parte de teoria y conceptos del examen desde cero, sin depender de PDFs ni materiales externos.

Reglas de esta capa:

- el contenido esta reescrito aqui dentro
- la estructura sigue los temas teoricos reales del curso
- no sigue la organizacion de practicas, proyectos o examenes
- cada bloque intenta dejar cuatro cosas cerradas:
  - que es la idea
  - con que se suele confundir
  - cuando conviene
  - como se ve en un ejemplo corto
- esta capa ya no es el paso final del estudio: cada bloque debe continuarse en `../cuadernos/`
- aqui el objetivo es que la teoria quede operativa y no solo "sonada"

Bloques activos:

- [B01 - Fundamentos de Python](01_fundamentos_python/README.md)
- [B02 - Clases y objetos](02_clases_y_objetos/README.md)
- [B03 - ADT, stacks y queues](03_stacks_y_queues/README.md)
- [B04 - Deque y priority queue](04_deque_priority_queue/README.md)
- [B05 - Buffers circulares](05_buffers_circulares/README.md)
- [B06 - Linked lists](06_linked_lists/README.md)

## Como estudiar esto desde cero

Orden recomendado:

1. B01 para fijar lenguaje base y ejecucion.
2. B02 para entender por que luego las estructuras se implementan como clases.
3. B03 para separar ADT, stack y queue.
4. B04 para entender como se extiende una queue.
5. B05 para no confundir queue con buffer.
6. B06 para dominar referencias, nodos y operaciones de linked lists.

Metodo de estudio recomendado:

1. Lee un bloque completo una vez.
2. Rehaz mentalmente los ejemplos guiados sin mirar.
3. Haz las microtrazas a mano.
4. Abre el cuaderno correspondiente en `../cuadernos/`, preferiblemente en Google Colab, y completa sus `TODO`.
5. Haz `Restart & Run All` en el cuaderno.
6. Contesta en voz alta las preguntas de autoexplicacion.
7. Haz la [checklist de 1 minuto](../checklist_1min/index.html).
8. Cierra el bloque pasando a `../entrega/`.

## Que significa dominar la teoria

No significa recitar frases sueltas. Significa poder hacer estas cosas:

- definir la estructura o concepto con tus palabras
- distinguirla de las otras estructuras cercanas
- decir que operaciones tiene y que garantizan
- decidir en que situacion conviene usarla
- seguir su estado paso a paso en un ejemplo corto
- detectar el error tipico antes de programar

Si no puedes seguir el estado de una estructura en una microtraza, todavia no controlas la teoria de ese bloque.

## Como esta construido cada bloque

Cada bloque intenta incluir siempre estas piezas:

- una definicion operativa
- una comparacion con las ideas cercanas
- uno o mas ejemplos guiados
- una microtraza para comprobar si realmente lo entiendes
- preguntas de autoexplicacion para detectar lagunas

Eso es deliberado. Leer un resumen no basta. Hay que obligarse a recuperar y explicar.

Y despues hay que ejecutar. Si una idea solo aguanta en lectura pero no aguanta en el cuaderno o en `entrega_spyder.py`, todavia no esta estable.

## Mapa de decisiones rapido

Si el problema es este:

- "quiero una secuencia general con acceso por indice" -> `list` de Python
- "quiero agrupar datos y comportamiento" -> clase
- "quiero el ultimo que entro" -> stack
- "quiero el primero que entro" -> queue
- "quiero operar por ambos extremos" -> deque
- "quiero sacar antes lo mas prioritario" -> priority queue
- "quiero un almacenamiento temporal con capacidad fija" -> buffer
- "quiero entender una estructura basada en referencias y nodos" -> linked list

Reglas adicionales importantes:

- si el problema habla de indices y acceso por posicion, piensa primero en `list`
- si el problema habla de extremos, piensa primero en `deque`
- si el problema habla de productor/consumidor o capacidad fija, piensa en buffer
- si el problema habla de prioridad, piensa en priority queue
- si el problema habla de nodos y enlaces, piensa en linked list

## Confusiones que este material intenta evitar

- ADT no es lo mismo que implementacion.
- Queue no es lo mismo que buffer.
- Clase no es lo mismo que objeto.
- Nodo no es lo mismo que linked list.
- `print` no es lo mismo que `return`.
- Tener una lista Python no significa tener una linked list.
- "mas flexible" no significa "siempre mejor".

## Criterio de calidad del repaso

Este resumen no intenta ser bonito. Intenta ser util.

Un bloque esta suficientemente estudiado cuando puedes hacer estas tres cosas sin mirar:

- explicar que es
- decidir cuando conviene
- seguir un ejemplo corto sin perderte
