# B02 - Clases y objetos

Autotest del bloque: [abre `autotest.ipynb` y ve a B02](autotest.ipynb)

## Que es este bloque

Este tema explica por que el curso usa clases para modelar estructuras de datos.

No basta con saber escribir `class ...`. Hay que entender:

- por que una clase mejora ciertas representaciones simples
- que diferencia hay entre clase y objeto
- como se crea un objeto
- como se llama a un metodo
- que es un atributo
- que es un metodo
- que hace `__init__`
- que significa `self`
- como controlar acceso y validez de los datos

## 1. El problema que intenta resolver la teoria

La teoria arranca comparando varias formas de guardar estudiantes:

- listas paralelas
- diccionarios
- clases

La idea de fondo es esta:

- cuando varios datos pertenecen a una misma entidad, separarlos en estructuras paralelas genera errores
- una clase permite agrupar datos y comportamiento bajo un mismo concepto

Eso es justo lo que luego haremos con `Stack`, `Queue` y `LinkedList`.

### Ejemplo guiado

Si representas estudiantes con listas paralelas:

```python
nombres = ["Ana", "Luis"]
edades = [20, 21]
notas = [8.5, 6.0]
```

el estudiante `i` queda repartido entre tres estructuras.

Si usas una clase:

```python
class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
```

cada estudiante queda modelado como una sola entidad coherente.

## 2. Clase frente a objeto

Esta es la distincion que mas conviene fijar bien:

- **clase** = plantilla, definicion general
- **objeto** = instancia concreta creada a partir de la clase

Ejemplo mental:

- `CuentaBancaria` es la idea general
- "la cuenta de Ana con saldo 100" es un objeto concreto

Confusion que debes evitar:

- pensar que la clase almacena los datos concretos

Los datos concretos viven en cada objeto.

## 3. Como se crea y se usa un objeto

Esta parte conviene verla de forma muy operativa.

Si tienes:

```python
class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def imprimir_info(self):
        print(f"{self.nombre} tiene una nota de {self.nota}")
```

entonces puedes hacer:

```python
ana = Estudiante("Ana", 20, 8.5)
ana.imprimir_info()
```

Lectura correcta:

- `Estudiante(...)` crea un objeto
- `ana` guarda una referencia a ese objeto
- `ana.imprimir_info()` llama al metodo de ese objeto concreto

### Microtraza

```python
ana = Estudiante("Ana", 20, 8.5)
```

Deberias entender esto:

1. se crea un objeto nuevo
2. Python ejecuta `__init__(self, "Ana", 20, 8.5)`
3. `self.nombre`, `self.edad` y `self.nota` quedan cargados
4. `ana` apunta a ese objeto ya inicializado

## 4. Atributos y metodos

Una clase define dos cosas:

- datos que el objeto guardara -> atributos
- acciones o comportamientos -> metodos

Ejemplo:

```python
class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def imprimir_info(self):
        print(f"{self.nombre} tiene una nota de {self.nota}")
```

Aqui:

- `nombre`, `edad`, `nota` son atributos
- `imprimir_info` es un metodo

## 5. Que hace `__init__`

`__init__` es el metodo que se ejecuta al crear el objeto.

Su papel:

- recibir los datos iniciales
- dejar el objeto en un estado valido desde el principio

No es simplemente "un metodo mas". Marca como nace el objeto.

## 6. Que significa `self`

`self` significa:

- este objeto concreto

Sirve para:

- acceder a atributos del propio objeto
- llamar a otros metodos del mismo objeto
- distinguir el estado del objeto de variables locales temporales

Ejemplo:

```python
class Counter:
    def __init__(self):
        self.total = 0

    def add(self, value):
        self.total += value
```

Si escribieras:

```python
total = self.total + value
```

no estarias cambiando el atributo del objeto, sino creando una variable local distinta.

## 7. Funcion frente a metodo

Esto tambien conviene fijarlo temprano.

Una funcion se llama asi:

```python
resultado = suma(2, 4)
```

Un metodo se llama sobre un objeto:

```python
ana.imprimir_info()
```

Regla conceptual:

- la funcion recibe datos y trabaja con ellos
- el metodo actua sobre el estado de un objeto concreto

No siempre la frontera es filosoficamente profunda, pero en este curso te conviene verla asi porque luego todas las estructuras se usan como objetos con metodos.

## 8. Por que no basta un diccionario

La teoria pasa por una version con diccionarios para mostrar que sigue habiendo limites:

- puedes equivocarte con las claves
- no queda claro que operaciones comunes existen
- no controlas bien las reglas del dato

La clase mejora esto porque:

- da un nombre al concepto
- encapsula comportamiento
- permite imponer invariantes

## 9. Control de acceso a los datos

Otro punto central del tema es proteger el estado interno.

Ejemplo de la teoria:

- una cuenta bancaria no deberia permitir saldo negativo sin control
- no deberias modificar un atributo sensible de cualquier manera

Por eso aparecen los nombres con doble guion bajo:

```python
self.__saldo = saldo
```

La idea que debes retener:

- marca que el atributo es interno
- obliga a pensar que el acceso correcto deberia pasar por metodos

## 10. Invariantes

Un invariante es una regla que el objeto debe mantener siempre.

Ejemplos que la teoria pone sobre la mesa:

- el saldo no deberia ser negativo
- una nota deberia ser numerica
- una nota deberia estar en un rango valido

Por eso no basta con guardar datos; hay que decidir como se validan.

### Ejemplo guiado

Si `retirar(cantidad)` deja el saldo en negativo sin control, el objeto entra en un estado invalido.

La clase sirve precisamente para evitar eso:

- no solo guarda datos
- tambien protege reglas del modelo

## 11. Como conecta esto con estructuras de datos

Este tema no es una parada decorativa. Sirve para que luego entiendas por que:

- una stack tiene atributos internos
- una queue ofrece un conjunto concreto de metodos
- una linked list expone operaciones y esconde enlaces internos

Si entiendes bien B02, luego las clases de estructuras se leen mucho mejor.

## 12. Preguntas de autoexplicacion

Si de verdad controlas B02, deberias poder contestar sin mirar:

- por que una clase mejora frente a listas paralelas
- que diferencia hay entre clase y objeto
- que hace `__init__`
- que significa `self`
- que diferencia practica hay entre llamar a una funcion y llamar a un metodo
- por que un metodo puede ser mejor sitio para validar una operacion que tocar un atributo directamente
- por que `__saldo` no es solo una mania estetica

## 13. Errores tipicos

- pensar que clase y objeto son lo mismo
- usar `self` sin entender que representa
- creer que un metodo es solo una funcion escrita dentro de una clase sin relacion con el estado
- creer que un atributo con `__` es solo una mania estetica
- no distinguir entre estado del objeto y variable local
- pensar que encapsular es solo esconder datos, en vez de proteger reglas del modelo
