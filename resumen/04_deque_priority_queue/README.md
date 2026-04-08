# B04 - Deque y priority queue

Autotest del bloque: [abre `autotest.ipynb` y ve a B04](../../autotest.ipynb)

## Que es este bloque

Este tema amplia la idea de queue en dos direcciones distintas:

- una estructura mas flexible por extremos -> deque
- una estructura donde manda la prioridad -> priority queue

La clave del bloque es no meterlas en el mismo saco.

## 1. De queue a deque

Una queue normal deja fija una regla:

- se entra por un lado
- se sale por el otro

La pregunta que abre la teoria es esta:

- que pasa si permitimos meter o sacar elementos por ambos extremos

La respuesta es la **deque**.

## 2. Deque

`Deque` significa **double-ended queue**.

Idea central:

- permite insertar y extraer por ambos extremos

Por eso es mas general que una queue normal.

### Operaciones naturales

- insertar por la izquierda
- insertar por la derecha
- extraer por la izquierda
- extraer por la derecha

### Que problema resuelve

Una queue normal te fija un extremo de entrada y otro de salida.

Una deque te sirve cuando el problema necesita trabajar por los dos lados.

## 3. Relacion con stack y queue

Esta idea debe quedar cristalina:

- si usas una deque de una forma, puedes comportarte como una queue
- si usas una deque de otra forma, puedes comportarte como una stack

Por eso la deque es una estructura mas flexible.

Pero esa flexibilidad no significa que siempre sea la respuesta correcta. Si el problema ya es claramente LIFO o FIFO, sigue siendo mejor pensarlo como stack o queue.

## 4. `collections.deque`

La teoria muestra la implementacion ya disponible en Python.

Operaciones mostradas:

- `append`
- `appendleft`
- `pop`
- `popleft`

Lectura correcta:

- `append` mete por la derecha
- `appendleft` mete por la izquierda
- `pop` saca por la derecha
- `popleft` saca por la izquierda

Nota teorica importante:

- el material explica que esta estructura se implementa usando linked lists

### Microtraza

Empieza con una deque vacia y ejecuta:

```python
append("b")
appendleft("a")
append("c")
popleft()
```

Estado correcto:

```text
[]                 inicial
[b]                append("b")
[a, b]             appendleft("a")
[a, b, c]          append("c")
[b, c]             popleft()
```

## 5. Priority queue

La priority queue cambia la regla de salida.

En una queue normal manda la antiguedad.

En una priority queue manda primero la prioridad.

Traduccion practica:

- el elemento mejor posicionado sale antes
- el orden de llegada por si solo ya no basta

## 6. Dos enfoques teoricos para implementarla

La teoria presenta dos caminos:

### Insercion ordenada

- al insertar, colocas el elemento en su sitio correcto
- extraer luego es facil

### Busqueda al extraer

- insertas sin dejar todo ordenado
- cuando quieres sacar, buscas el mejor candidato

Criterio claro:

- si quieres pagar el coste antes, ordena al insertar
- si quieres pagar el coste despues, busca al extraer

### Ejemplo guiado

Supongamos prioridades mas altas para numeros mayores.

Si llega:

```text
3, 1, 5
```

entonces:

- con insercion ordenada, la estructura queda preparada para sacar antes `5`
- con busqueda al extraer, puedes guardar sin tanto orden y decidir al final quien sale primero

La diferencia no esta en el resultado conceptual. Esta en donde pagas el coste.

## 7. Como decidir entre deque y priority queue

Usa **deque** cuando:

- el problema habla de extremos
- necesitas operar por izquierda y derecha

Usa **priority queue** cuando:

- el problema dice explicitamente que unos elementos tienen prioridad sobre otros
- el orden de salida no depende solo de cuando entro cada elemento

Regla practica:

- extremos -> deque
- prioridad -> priority queue

## 8. Confusiones tipicas

- pensar que deque y priority queue son la misma "cola avanzada"
- creer que deque implica prioridad
- creer que priority queue opera por ambos extremos

No:

- deque trata sobre extremos
- priority queue trata sobre criterio de prioridad

## 9. Preguntas de autoexplicacion

Si de verdad controlas B04, deberias poder contestar sin mirar:

- por que una deque generaliza una queue
- en que se diferencia conceptualmente de una stack
- que hacen `appendleft` y `popleft`
- por que priority queue no significa "cola por los dos lados"
- que significa pagar el coste al insertar o al extraer
