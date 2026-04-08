# B03 - ADT, stacks y queues

Autotest del bloque: [abre `autotest.ipynb` y ve a B03](../../autotest.ipynb)

## Que es este bloque

Este tema fija el vocabulario conceptual que luego se usa en todo el curso.

No basta con saber que stack es LIFO y queue es FIFO. Hay que entender antes:

- que es un ADT
- en que se diferencia de una implementacion concreta
- como se relacionan `list`, `map`, `stack` y `queue`
- en que situacion tiene sentido cada una

## 1. ADT frente a implementacion

Esta es la distincion mas importante del tema.

Un **ADT** define:

- que valores maneja
- que operaciones existen
- que comportamiento espera el usuario

Una **implementacion** decide:

- como se representa eso en memoria
- que codigo usa internamente

Ejemplo:

- una stack es un ADT
- usar una lista Python para implementarla es una decision de implementacion

Si en el examen te preguntan por un ADT, no debes contestar solo con codigo. Debes hablar de comportamiento y operaciones.

## 2. List y map como ADT generales

La teoria recuerda que Python ya incluye varios ADT utiles.

### List

Sirve para una secuencia ordenada de elementos.

Ideas clave:

- hay orden
- hay acceso por indice
- el tamano puede cambiar

### Map

Sirve para asociar claves con valores.

Ideas clave:

- trabajas con pares `<clave, valor>`
- preguntas por una clave para obtener un valor

## 3. Stack

La stack sigue la regla **LIFO**:

- last in, first out

Traduccion practica:

- el ultimo elemento que entra es el primero que sale

Operaciones canonicas:

- `push(item)` mete en la cima
- `pop()` saca la cima
- `peek()` mira la cima sin sacarla
- `is_empty()`
- `size()`

### Ejemplo guiado

Si haces:

```python
push(4)
push(9)
push(2)
```

la cima queda en `2`.

Si despues haces:

```python
x = pop()
y = peek()
```

entonces:

- `x = 2`
- `y = 9`

### Microtraza

Estado de la stack tras cada paso:

```text
[]                  inicial
[4]                 push(4)
[4, 9]              push(9)
[4, 9, 2]           push(2)
[4, 9]              pop()
```

No hace falta pensar en una representacion concreta. Basta con seguir la regla LIFO.

## 4. Queue

La queue sigue la regla **FIFO**:

- first in, first out

Traduccion practica:

- el elemento mas antiguo es el primero que sale

Operaciones canonicas:

- `enqueue(item)` inserta al final
- `dequeue()` saca el mas antiguo
- `peek()`
- `is_empty()`
- `size()`

### Ejemplo guiado

Si haces:

```python
enqueue("A")
enqueue("B")
enqueue("C")
```

la queue queda con `"A"` delante y `"C"` al final.

Si luego haces:

```python
x = dequeue()
```

entonces `x = "A"`.

### Microtraza

```text
[]                      inicial
[A]                     enqueue(A)
[A, B]                  enqueue(B)
[A, B, C]               enqueue(C)
[B, C]                  dequeue()
```

## 5. Stack frente a queue

Esta comparacion debe quedar limpia:

### Usa stack cuando...

- importa el ultimo elemento pendiente
- quieres deshacer o retroceder el ultimo paso
- trabajas con anidacion o cierres pendientes

### Usa queue cuando...

- importa respetar el orden de llegada
- quieres procesar elementos segun fueron entrando

Resumen corto:

- ultimo en entrar, primero en salir -> stack
- primero en entrar, primero en salir -> queue

## 6. Lo que no debes confundir

- una stack y una queue pueden implementarse con la misma estructura base, pero no por eso se comportan igual
- la diferencia clave esta en las reglas de insercion y extraccion
- "usar una lista Python" no define por si solo que tengas una stack o una queue; lo define como la uses

## 7. Preguntas de autoexplicacion

Si de verdad controlas B03, deberias poder contestar sin mirar:

- que describe un ADT y que deja sin fijar
- por que una stack y una queue pueden compartir implementacion y no compartir comportamiento
- si te doy una secuencia de operaciones, que queda dentro
- si te doy un problema, por que es stack y no queue
- por que "tiene append y pop" no basta para decidir que estructura conceptual es

## 8. Errores tipicos

- decir que stack y queue se diferencian solo por el nombre de los metodos
- no saber seguir el estado interno tras varias operaciones
- confundir ADT con implementacion concreta
- llamar queue a cualquier estructura con `append` y `pop`
