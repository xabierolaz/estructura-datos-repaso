# B06 - Linked lists

Autotest del bloque: [abre `autotest.ipynb` y ve a B06](autotest.ipynb)

## Que es este bloque

Este tema introduce una estructura donde el concepto clave no es el indice, sino la referencia entre nodos.

Si este bloque queda borroso, luego fallan justo las operaciones que mas suelen romperse en examen:

- insertar sin perder la cadena
- borrar sin desconectar mal los nodos
- gestionar lista vacia y lista de un elemento

## 1. Que es una linked list

Una linked list es una secuencia de nodos donde cada nodo conoce el siguiente.

Cada nodo guarda:

- el dato
- la referencia al siguiente nodo

Modelo minimo:

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
```

La lista no necesita guardar todos los nodos por separado. Le basta con una referencia al primero:

```python
self.__head
```

### Esquema minimo

```text
head -> [12 | next] -> [99 | next] -> [37 | None]
```

La idea no es memorizar el dibujo. Es ver que la lista se sigue saltando de nodo en nodo.

## 2. Que es `head` y por que es tan importante

`head` es la puerta de entrada a toda la lista.

Idea central:

- si tienes `head`, puedes llegar al resto saltando de `next` en `next`
- si pierdes `head`, has perdido el acceso a la estructura

Esto explica por que tantas operaciones empiezan en la cabeza.

## 3. Como se recorre

Patron base:

```python
current = self.__head
while current is not None:
    ...
    current = current.next
```

Esta idea sostiene:

- `size`
- `contains`
- `get`
- `set`
- llegar a la cola
- localizar un nodo para insertar o borrar

Si este patron no esta interiorizado, no hay linked list estable.

### Microtraza

Si:

```text
head -> [9] -> [4] -> [7] -> None
```

y haces:

```python
current = head
current = current.next
current = current.next
```

entonces acabas en el nodo que contiene `7`.

## 4. Que diferencia una linked list de una lista Python

Esta comparacion debe quedar muy clara.

### Lista Python

- acceso por indice natural
- muy comoda para uso general

### Linked list

- acceso por recorrido desde `head`
- cada paso depende del enlace al siguiente nodo

Criterio conceptual:

- en una linked list el indice no da acceso directo; representa cuantos saltos haces desde `head`

## 5. Operaciones de lectura

### `size`

Cuenta nodos recorriendo desde `head` hasta `None`.

### `contains`

Busca secuencialmente hasta encontrar el dato o llegar al final.

### `get` y `set`

No saltan magicamente al indice. Avanzan nodo a nodo.

Esto es importante porque evita una confusion habitual:

- pensar linked list como si fuera una lista Python con otra sintaxis

No lo es.

## 6. Insertar

La teoria distingue tres situaciones:

- insertar en cabeza
- insertar en cola
- insertar despues de un indice

### Insertar en cabeza

Es la operacion mas simple:

1. el nodo nuevo apunta a la cabeza antigua
2. `head` pasa a ser el nodo nuevo

Si alteras ese orden, puedes perder la cadena.

#### Ejemplo guiado

Estado inicial:

```text
head -> [4] -> [7] -> None
```

Creas `new = Node(2, head)` y luego haces `head = new`.

Estado final:

```text
head -> [2] -> [4] -> [7] -> None
```

### Insertar en cola

Hay que llegar al ultimo nodo real, el que tiene `next == None`.

No basta con saber que existe un final. Hay que recorrer hasta el nodo que lo marca.

### Insertar despues de un indice

La idea correcta es:

1. llegar al nodo objetivo
2. guardar el enlace que antes iba despues
3. enganchar el nodo nuevo
4. mantener el resto de la lista accesible

#### Esquema

Antes:

```text
[A] -> [B] -> [C] -> None
```

Quieres insertar `X` despues de `B`.

Despues:

```text
[A] -> [B] -> [X] -> [C] -> None
```

Confusion tipica:

- reasignar `next` demasiado pronto y perder el resto de la cadena

## 7. Borrar

La teoria distingue:

- borrar cabeza
- borrar cola
- borrar por indice
- borrar por valor

### Borrar cabeza

Solo exige mover `head` al siguiente nodo.

Antes:

```text
head -> [4] -> [7] -> None
```

Despues de `remove_head()`:

```text
head -> [7] -> None
```

### Borrar cola

Aqui esta uno de los puntos mas traicioneros:

- no basta con llegar al ultimo
- necesitas llegar al penultimo para poder hacer que apunte a `None`

#### Esquema

Antes:

```text
head -> [4] -> [7] -> [9] -> None
```

Despues de borrar cola:

```text
head -> [4] -> [7] -> None
```

El nodo clave no era `9`. Era `7`, porque es quien tiene que cambiar su `next`.

### Borrar por indice o por valor

Necesitas mantener el nodo anterior para reconectar la cadena despues del borrado.

Si borras un nodo del medio, el trabajo real es unir bien el anterior con el siguiente.

## 8. Casos limite

Este bloque exige pensar siempre en:

- lista vacia
- lista de un elemento
- indice fuera de rango

La teoria insiste en el manejo defensivo precisamente porque linked lists falla mucho aqui.

Preguntas que debes saber contestar:

- que pasa si intentas insertar o borrar en una posicion que no existe
- que cambia si la lista tiene un solo nodo

## 9. Mejoras y dunder methods

La teoria no se queda solo en operaciones basicas. Tambien propone:

- devolver el elemento borrado
- mantener un contador de tamano
- implementar `__len__`
- implementar `__contains__`
- implementar `__str__`

La idea es acercar la estructura a una interfaz mas natural de Python sin perder su logica interna.

## 10. Cuando usar esta idea en examen

Piensa en linked list cuando el foco conceptual esta en:

- nodos
- enlaces
- recorrido lineal
- inserciones y borrados reenganchando referencias

No la pienses como una simple lista Python peor. El objetivo del tema es entrenar pensamiento sobre referencias y estructura.

Comparacion practica corta:

- si quieres acceso por indice y una secuencia general, piensa antes en `list`
- si quieres trabajo por ambos extremos sin razonar con nodos, piensa antes en `deque`
- si el problema exige razonar con `head`, `next` y reconexion de enlaces, entonces es linked list

## 11. Preguntas de autoexplicacion

Si de verdad controlas B06, deberias poder contestar sin mirar:

- que es un nodo
- que es `head`
- por que casi todas las operaciones empiezan ahi
- por que insertar en cabeza es mas simple que insertar en cola
- por que `remove_tail` necesita el penultimo nodo
- que casos limite hay que comprobar antes de tocar `next`
- por que linked list no se debe pensar como lista Python con otra sintaxis

## 12. Errores tipicos

- confundir nodo con lista completa
- creer que `get(index)` es acceso directo
- olvidar que `head` es la unica puerta de entrada
- perder la cadena al insertar
- llegar al ultimo en `remove_tail` cuando necesitabas el penultimo
- no tratar lista vacia y lista de un elemento
