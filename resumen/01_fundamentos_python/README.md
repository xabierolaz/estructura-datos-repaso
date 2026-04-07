# B01 - Fundamentos de Python

Checklist rapida del bloque: [abrir B01](../../checklist_1min/index.html#b01)

## Que es este bloque

Este bloque fija el lenguaje base que luego se reutiliza en toda la asignatura. No introduce una estructura nueva, pero deja claras las piezas que aparecen despues en todos los ejercicios.

Ideas del tema:

- ejecucion de scripts
- funciones, parametros y retorno
- listas y recorrido
- desempaquetado
- `enumerate`
- ficheros y rutas
- `f-strings`
- type hints
- comentarios y docstrings
- `__name__` y `main`

## 1. Que debe quedarte claro antes de seguir

Antes de entrar en estructuras de datos debes tener claras estas diferencias:

- una variable puede guardar un valor o una referencia a un objeto
- una lista es una secuencia ordenada y mutable
- leer un fichero no es lo mismo que procesar su contenido
- imprimir algo no es lo mismo que devolverlo
- ejecutar un archivo directamente no es lo mismo que importarlo

Si esto no esta firme, luego todo lo demas se vuelve confuso.

## 2. Funciones, parametros y retorno

Esta parte tiene que quedar muy limpia porque luego todo el curso depende de ella.

Una funcion:

- se define con `def`
- puede recibir datos de entrada
- puede devolver un resultado con `return`

Ejemplo minimo:

```python
def doble(x: int) -> int:
    return 2 * x
```

Lectura correcta:

- `doble` es el nombre de la funcion
- `x` es el parametro
- `-> int` indica que se espera devolver un entero
- `return` devuelve el resultado al sitio donde se llamo a la funcion

### Parametro frente a argumento

- **parametro** = nombre que aparece en la definicion
- **argumento** = valor concreto que pasas al llamar

Ejemplo:

```python
def suma(a, b):
    return a + b


resultado = suma(3, 5)
```

Aqui:

- `a` y `b` son parametros
- `3` y `5` son argumentos

### `print` frente a `return`

Esta diferencia es critica.

```python
def mal(x):
    print(x + 1)


def bien(x):
    return x + 1
```

`print`:

- muestra algo por pantalla
- no convierte ese valor en el resultado reutilizable de la funcion

`return`:

- entrega un resultado
- permite guardarlo, compararlo o usarlo despues

### Ejemplo guiado

```python
def suma(a, b):
    return a + b


x = suma(2, 4)
```

La lectura correcta es:

1. se llama a `suma` con los argumentos `2` y `4`
2. dentro de la funcion, `a = 2` y `b = 4`
3. `return a + b` produce `6`
4. `x` pasa a valer `6`

### Microtraza

Sin ejecutar, di que ocurre aqui:

```python
def siguiente(x):
    print(x + 1)


valor = siguiente(4)
```

Lo correcto es responder:

- por pantalla aparece `5`
- `valor` no vale `5`
- `valor` queda en `None`, porque la funcion no devuelve nada con `return`

## 3. Listas, orden y recorrido

Una lista Python:

- mantiene el orden de los elementos
- permite acceder por indice
- permite recorrer los elementos uno a uno

Tres patrones que debes distinguir:

### Solo necesito el valor

```python
for value in values:
    ...
```

### Necesito el indice y el valor

```python
for index, value in enumerate(values):
    ...
```

### Necesito controlar el rango exacto de indices

```python
for i in range(len(values)):
    ...
```

Regla practica:

- si no necesitas el indice, no lo inventes
- si necesitas indice y valor, `enumerate` suele ser la opcion mas clara
- si necesitas controlar saltos, limites o posiciones concretas, `range(len(...))` puede tener sentido

### Ejemplo guiado

Si `values = ["a", "b", "c"]`:

- con `for value in values` recorres `"a"`, `"b"`, `"c"`
- con `for index, value in enumerate(values)` obtienes `(0, "a")`, `(1, "b")`, `(2, "c")`
- con `for i in range(len(values))` obtienes `0`, `1`, `2` y luego decides que hacer con `values[i]`

### Microtraza

Sin ejecutar, di que imprime este codigo:

```python
values = [10, 20, 30]
for index, value in enumerate(values):
    print(index, value)
```

Deberias poder responder:

- `0 10`
- `1 20`
- `2 30`

## 4. Asignacion multiple y desempaquetado

Python permite escribir:

```python
x, y = 3, 5
```

Y tambien:

```python
first, *middle, last = [10, 20, 30, 40, 50]
```

La idea importante es esta:

- Python reparte la estructura de la derecha sobre la forma de la izquierda
- solo puede haber una variable con `*`
- este patron aparece mucho cuando una funcion devuelve varias piezas de informacion

### Ejemplo guiado

```python
first, *middle, last = [10, 20, 30, 40, 50]
```

Resultado correcto:

- `first = 10`
- `middle = [20, 30, 40]`
- `last = 50`

Confusion tipica:

- creer que `middle` guarda un solo valor; no, guarda una lista

## 5. Ficheros y rutas

La teoria insiste en que un fichero no aparece por magia. Hay que saber:

- donde esta
- con que ruta lo nombras
- en que modo lo abres

### Ruta absoluta

Da la localizacion completa del fichero.

### Ruta relativa

Se interpreta respecto al directorio actual desde el que se ejecuta el programa.

Esto explica muchos errores de "no encuentro el archivo".

### Modos de apertura

Debes distinguir claramente:

- `r`: leer
- `w`: escribir borrando el contenido previo si existe
- `a`: escribir al final sin borrar lo anterior
- `r+`, `w+`, `a+`: variantes con lectura y escritura

Confusion tipica:

- usar `w` cuando querias conservar el contenido

### Ejemplo guiado

Si un fichero ya existe y contiene:

```text
hola
```

entonces:

- abrir con `w` y escribir `"x"` deja solo `"x"`
- abrir con `a` y escribir `"x"` deja `hola` seguido de `"x"`

## 6. Leer y transformar texto

Dos patrones base:

```python
with open(path, "r", encoding="utf-8") as f:
    text = f.read()
```

y

```python
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        ...
```

Transformaciones que debes dominar:

- `strip()` para limpiar espacios o saltos al principio y final
- `split()` para separar en trozos
- `int(...)` para pasar de texto a numero

Ejemplo:

```python
line = "1 2 3\n"
tokens = line.strip().split()
numbers = [int(token) for token in tokens]
```

Lectura correcta del ejemplo:

- `line` es texto
- `strip()` elimina el salto de linea final
- `split()` produce `["1", "2", "3"]`
- el resultado final es `[1, 2, 3]`

## 7. `f-strings`

Una `f-string` es una cadena con `f` delante:

```python
print(f"Hola {name}")
```

Ventajas:

- es mas clara que concatenar trozos
- permite meter expresiones validas dentro de llaves
- permite formato de salida

### Formato minimo que debes reconocer

```python
value = 3.14159
print(f"{value:.2f}")
```

Esto imprime `3.14`.

Interpretacion:

- `:` introduce formato
- `.2f` pide dos decimales en formato de numero real

No hace falta memorizar todas las variantes, pero si debes reconocer que el formato existe y que controla como se presenta el valor.

Confusion que hay que evitar:

- no es una sintaxis decorativa; es una forma de construir texto de manera controlada

## 8. Type hints y lectura de firmas

Los type hints:

- documentan intencion
- hacen mas facil leer funciones y atributos
- no obligan a Python a comprobar tipos durante la ejecucion por si solos

Ejemplo:

```python
def get(matrix: list, i: int, j: int) -> int:
    ...
```

Lectura correcta de la firma:

- la funcion se llama `get`
- espera tres entradas: `matrix`, `i`, `j`
- `i` y `j` deberian ser enteros
- se espera devolver un entero

Lo importante para examen es poder leer una firma y entender que promete la funcion:

- que espera como entrada
- que pretende devolver

## 9. Comentarios y docstrings

Un comentario bueno:

- explica una decision
- aclara un caso no obvio
- evita que alguien tenga que adivinar una intencion

Un comentario malo:

- repite lo mismo que ya dice el codigo

Un docstring describe para que sirve una funcion y como usarla.

Ejemplo minimo razonable:

```python
def load_numbers(path: str) -> list[int]:
    """Read a text file and return the integers it contains."""
```

Lo que debes retener:

- comentario y docstring no son lo mismo
- el comentario aclara una parte concreta
- el docstring documenta una funcion o clase completa

## 10. `__name__` y `main`

Esta parte suele generar confusion al principio.

Si un archivo se ejecuta directamente:

```python
__name__ == "__main__"
```

Si el archivo se importa:

- `__name__` sera el nombre del modulo

Patron canonico:

```python
def main():
    ...


if __name__ == "__main__":
    main()
```

Esto sirve para separar:

- definiciones reutilizables
- codigo que solo debe correr cuando lanzas ese archivo como script

### Microtraza

Si `utils.py` contiene:

```python
print(__name__)
```

y otro archivo hace `import utils`, entonces `utils.py` no vera `"__main__"`. Vera el nombre del modulo.

## 11. Preguntas de autoexplicacion

Si de verdad controlas B01, deberias poder contestar sin mirar:

- que diferencia hay entre parametro y argumento
- que diferencia real hay entre `print` y `return`
- cuando usarias `enumerate` en lugar de un `for value in ...`
- que diferencia real hay entre `w` y `a`
- por que una ruta relativa puede fallar aunque el fichero exista
- que hace `first, *middle, last = ...`
- que problema resuelve `if __name__ == "__main__":`
- que diferencia hay entre comentario y docstring

## 12. Errores tipicos del bloque

- confundir `print` con `return`
- usar rutas relativas sin saber desde donde se ejecuta el programa
- olvidar `strip()` y arrastrar `\n`
- usar `w` cuando querias `a`
- recorrer con indices cuando no hacen falta
- no entender que `__name__ == "__main__"` depende de como se usa el archivo
- leer una firma de funcion sin saber que esta prometiendo
