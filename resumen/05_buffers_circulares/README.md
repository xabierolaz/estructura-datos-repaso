# B05 - Buffers circulares

Checklist rapida del bloque: [abrir B05](../../checklist_1min/index.html#b05)

## Que es este bloque

Este tema explica una idea que suele confundirse mucho:

- una queue es un ADT
- un buffer es un caso de uso

El bloque existe para dejar clara esa diferencia y para introducir el buffer circular.

## 1. Que es un buffer

Definicion operativa:

- un buffer es un almacenamiento temporal entre un productor y un consumidor

Sirve cuando:

- no producen al mismo ritmo
- no consumen al mismo ritmo
- llegan rafagas de datos

Idea mental:

- el buffer absorbe desajustes temporales

### Ejemplo guiado

Piensa en este caso:

- una fuente de datos genera mensajes muy rapido durante un momento
- quien los procesa va mas lento

Sin buffer, se pierden o bloquean mensajes enseguida.

Con buffer, los datos se guardan temporalmente hasta que el consumidor los vaya sacando.

## 2. Buffer frente a queue

Esta es la comparacion que debe quedar limpia.

### Queue

- es una estructura logica
- la define la regla FIFO

### Buffer

- lo define su funcion en un sistema
- suele tener capacidad limitada
- importa mucho que pasa cuando se llena

Conclusion:

- muchos buffers se implementan con una queue
- pero buffer y queue no son sinonimos

## 3. Por que el tema separa buffer de queue

Porque una queue por si sola no responde a preguntas como:

- cual es la capacidad maxima
- que pasa cuando no cabe un dato nuevo
- si me interesan todos los datos o solo los mas recientes

Esas preguntas son propias del buffer.

## 4. Buffer circular

El buffer circular aparece cuando:

- hay capacidad fija
- quieres reutilizar el espacio
- te interesa tratar la memoria como una estructura que vuelve al principio

Ideas clave:

- hay una logica FIFO sobre los datos almacenados
- fisicamente el indice puede dar la vuelta
- no hay un principio absoluto de la memoria, sino de los datos activos

### Ejemplo visual minimo

Con capacidad 5:

```text
[0] [1] [2] [3] [4]
```

si un indice esta en `4` y avanza una posicion mas, no cae fuera:

```text
4 -> 0
```

## 5. Politicas cuando se llena

Esta es la parte mas importante del bloque.

Cuando el buffer esta lleno, no hay una unica respuesta correcta. La teoria plantea varias:

- descartar el dato nuevo
- sobrescribir el dato mas antiguo
- bloquear hasta que haya sitio

La pregunta correcta en un examen teorico es:

- que politica se esta asumiendo en este caso

### Microtraza

Capacidad 3. Politica: sobrescribir el dato mas antiguo.

Llegan:

```text
1, 2, 3, 4
```

Estado correcto al final:

```text
2, 3, 4
```

No porque el buffer deje de ser FIFO, sino porque la politica de llenado ha decidido expulsar el dato mas antiguo al entrar el nuevo.

## 6. Implementacion con indices

La mejora teorica del bloque introduce indices circulares.

Regla central:

```python
indice = (indice + 1) % capacidad
```

Lo que debes entender, no solo repetir:

- `% capacidad` hace que el indice vuelva a `0` cuando supera el final
- esto permite reutilizar posiciones sin crecer indefinidamente

### Microtraza

Si `capacidad = 5`:

- si `indice = 2`, el siguiente es `3`
- si `indice = 4`, el siguiente es `0`

## 7. Cuando pensar en buffer y no en queue

Piensa en **buffer** cuando el problema habla de:

- streaming
- almacenamiento temporal
- capacidad fija
- productor y consumidor
- conservar solo datos recientes

Piensa en **queue** cuando el foco esta solo en:

- orden de llegada
- insercion y extraccion FIFO

## 8. Preguntas de autoexplicacion

Si de verdad controlas B05, deberias poder contestar sin mirar:

- que define a un buffer y que define a una queue
- por que capacidad fija cambia el problema
- que decisiones hay que tomar cuando el buffer se llena
- por que `% capacidad` resuelve la vuelta al principio
- en que caso tiene sentido conservar solo los datos mas recientes

## 9. Confusiones tipicas

- llamar queue a cualquier buffer
- olvidar que la capacidad fija cambia el problema
- pensar que FIFO y buffer son exactamente lo mismo
- no distinguir politica de llenado
