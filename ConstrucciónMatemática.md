# Construcción Matemática

## Modelación Matemática

> Definición: Modelo

    Representación simplificada de la realidad.

    Ejemplos:
    - Mapas
    - Pinturas

> Definición: Modelo Matemático

    Representación de un objeto o fenómeno utilizando un lenguaje simplificado (matemático).
    
    Características:
    - Identificación del problema.
    - Formulación de un objetivo.
    - Determinación de las herramientas matemáticas para resolverlo.
    - Validación y verificación del modelo.

### Tipos de modelos

#### Clasificación de los modelos matemáticos

* Estáticos $\longrightarrow$ Cantidades que no cambian (Determinista)
* Dinámicos $\longrightarrow$ Cantidades que cambian (Probabilista)

### ¿Cuál sería el mejor modelo?

Aquel modelo más simple posible que reproduzca los resultados.

## Modelación y Simulación

* Definición del problema que será resuelto.
* Definición del sistemma (parte de la "realidad") qué está involucrado en el problema.

### Análisis del sistema

* Identificación de las partes del sistema que son relevantes para resolver el problema.

### Simulación

* Aplicación del modelo en cuestión.
* Elaboración de una estrategia para resolver el problema.

### Validación

* Hacemos las siguientes preguntas. 
    * ¿La simulación resuelve el problema?
    * ¿Reproduce alguna parte de la realidad?
    * ¿El modelo reproduce los resultados del sistema?

> Definición: Simmulación
    
    Es la aplicación del modelo con el objetivo de comparar sus resultados o predicaciones con el fenómeno en cuestión.

> Definición: Sistema

    El objeto o conjunto de ojetos que queremos estudiar.

## Sistema de Entrada-Salida

$$\text{Entrada}\longrightarrow\text{Sistema}\longrightarrow\text{Salida}$$

> Definición: Modelo matemático

    Un modelo matemático es una tupla (S, Q, M), donde S es un sistemma, Q es una pregunta o cuestión que se hace acerca del sistema S, y M es un conjunto de formulas matemáticas que se usan para responder a Q.

## Ecuaciones diferenciales

$P$: número de habitantes (Miles o Millones).

$t$: Tiempo (Años).

$\frac{dP}{dt}$: Razón de cambio, velocidad de crecimiento.

$P(t)$: Número de habitanntes en el tiempo $t$.

$P(2)=30$: "Pasados dos años hay treinta mil habitantes".

$P'(5)=6$: "Al quinto año, la velocidad de crecimiento es de seis mil habitantes por año ($6\frac{hab}{año}$)".

Esa información la da el experimento

Decimos que $A$ es directamente proporcional a $B$ si y solo si $A\propto B$, $A=KB$.

$$\frac{dP}{dt}=kP(t) \text{ Ecuación diferencial ordinaria separable}$$

Decimos que $A$ es inverdamente proporcional a $B$ si y solo si $A=\frac{k}{B}$.

## Diferencias entre $dy,\:dx$ y  $\Delta y,\:\Delta x$

| Aproximación | Cambios (Valores exactos) |
|:------------:|:-------------------------:|
|   $dy,\:dx$  |   $\Delta y,\:\Delta x$   |

$$\frac{dy}{dx}=f'(x)$$

$$\frac{\Delta y}{\Delta x}=\frac{y_2-y_1}{x_2-x_1}\text{ pendiente}$$

A estos los une un límite

$$\frac{dy}{dx}=\lim_{\Delta x\to0}{\frac{\Delta x}{\Delta y}}$$

> Definición: 
    
    Una ecuación diferencial ordinaria de dice separable si tiene la forma de.

$$\frac{dy}{dx}=f(x)g(y)$$
$$\frac{dy}{g(y)}=f(x)dx$$

## Teoría de ecuaciones diferenciales ordinarias (EDO)

> Ordinarias: 

    "Solo hay una variable independiente".

> Definición: Orden de una EDO

    Es el orden de la derivada mayor.

> Definición: Grado de una EDO

    Es la potenciaque tenga la derivada de mayor orden.

Una EDO lineal de orden $n$ se escribe como:
$$a_n(x)\frac{d^ny}{dx^n}+a_{n-1}(x)\frac{d^{n-1}y}{dx^{n-1}}+\dotsb+a_1(x)\frac{dy}{dx}+a_0(x)y=g(x)$$

### Solución a una EDO de orden y grado uno

Sea $a_1(x)y'+a_0(x)y=g(x)$, procedemos a anular el coeficiente $a_1$.

$$\frac{a_1(x)y'+a_0(x)y=g(x)}{a_1(x)}$$
$$y'+\frac{a_0(x)}{a_1(x)}y=\frac{g(x)}{a_1(x)}$$
$$y'+P(x)y=Q(x) \text{...(1)}$$

Ahora multiplicamos por el factor integrante $\mu(x)$
$$\mu(x)y'+\mu(x)P(x)y=\mu(x)Q(x) \text{...(2)}$$
Buscamos que 
$$\frac{d}{dx}\left(\mu(x)y\right)=\mu(x)y'+\mu(x)'y$$
Sumamos y restamos $\mu(x)'y$ en la ecuación $\text{(2)}$
$$\mu(x)y'+\mu(x)P(x)y+\mu(x)'y-\mu(x)'y=\mu(x)Q(x)$$
$$\mu(x)P(x)y-\mu(x)'y=0$$
$$y(\mu(x)P(x)-\mu(x)')=0$$
$$\mu(x)P(x)-\mu(x)'=0\text{ Pues $y$ no puede ser 0}$$
$$\mu(x)P(x)-\frac{d\mu}{dx}=0$$
$$\mu(x)P(x)=\frac{d\mu}{dx}$$
$$P(x)dx=\frac{d\mu}{\mu(x)}$$
Integramos
$$\int{P(x)dx}=ln(\mu(x))$$
$$exp\left(\int{P(x)dx}\right)=\mu(x)$$
Por lo tanto
$$\mu(x)=e^{\int{P(x)dx}}$$
Luego 
$$(\mu(x)y)'=Q(x)\mu(x)$$
$$\frac{d(\mu(x)y)}{dx}=Q(x)\mu(x)$$
$$yd\mu(x)=Q(x)\mu(x)dx$$
Integramos
$$y\int{d\mu(x)}=\int{Q(x)\mu(x)dx}$$
Por lo tanto
$$y=\frac{\int{Q(x)\mu(x)dx}}{\mu(x)}$$
$$y=\frac{\int{Q(x)e^{\int{P(x)dx}}dx}}{e^{\int{P(x)dx}}}$$