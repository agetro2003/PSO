# PSO

### Asignatura: Optimización

### Curso: 2025/2026

### Alumno: Jesús Daniel Ortega Briceño

## Descripción

    Este proyecto cuenta con una archivo pso.py que cuenta con la clase PSO usada 
    para calcular una aproximación usando el algoritmo Particle Swarm Optimization (PSO).
    Asimismo, se cuenta los archivos f1.py, f4.py y f8.py que implementan la clase PSO 
    usando distintas funciones a partir de las que se hara la aproximación. 

## Uso

```shell
    $ python .\fn.py 
```
## Ejemplo de uso
```shell
    $ python .\f1.py
```
## Implementaciones

A continuación, se detalla las implementaciones del algoritmo PSO de pso.py. 

### f1.py
**Funcion evaluada**

$f_1(\mathbf{x}) = \sum_{i=1}^{n} x_i^2$ 

**Párametros usados para la ejecución**

| Número de dimensiones | Número de partículas | Espacio de búsqueda | Iteraciones | Peso de inercia | Peso de la mejor posición local | Peso de la mejor posición global |
|:---------------------:|:--------------------:|:------------------:|:-----------:|:---------------:|:-------------------------------:|:--------------------------------:|
| 30 | 30 | [-100, 100] | 50000 | 0.5 | 1 | 1.5 |


**Resultados**

* Posicion de la mejor particula:
```python
[8.400513518237767e-17, 3.499712735004395e-17, -5.7388965770117305e-18, -3.130516298500713e-17, 3.585490325412386e-13, -1.870849801103132e-17, 1.8880851263186453e-12, -9.067867961648191e-09, -6.48321513113908e-18, 1.85011511600383e-17, -1.7762872316547577e-15, -1.6170458836032565e-12, -2.5126380452483726e-15, -7.831361611986779e-17, 5.369672461989989e-16, 2.7592219903085556e-17, -2.0240827218594985e-17, -3.237693012073813e-17, -6.325633773010786e-16, 1.240691248306213e-16, -9.449702958878844e-17, 2.1990288432153925e-17, 2.695329721844695e-16, 4.287345372152463e-15, -5.04312334255715e-13, 1.8782564450873746e-17, -5.330715616939142e-17, 7.783771405624445e-17, -6.2651026601233766e-15, -6.589422896076105e-17]  
 ```

* Datos de ejecución:

| Parámetro              | Valor                    |
|------------------------|--------------------------|
| Función evaluada       | f1.py                    |
| Mejor aptitud obtenida | `8.222623593254475e-17`  |
| Tiempo de ejecución    | `22.518 segundos`        |
| Valor mínimo de la función | 0 |

**Conclusiones**
```
Se puede observar como el resultado obtenido es bastante cercano al mínimo global de la función.
Alcanzando un valor cercano a 0 de forma relativamente rápida, por lo que concluimos que el algoritmo funciona correctamente para este problema.
```


### f4.py

**Funcion evaluada**

$f_4(\mathbf{x}) = \max \{|x_i|, 1 \le i \le n\}$

**Parametos usados para la ejecución**

| Número de dimensiones | Número de partículas | Espacio de búsqueda | Iteraciones | Peso de inercia | Peso de la mejor posición local | Peso de la mejor posición global |
|:---------------------:|:--------------------:|:------------------:|:-----------:|:---------------:|:-------------------------------:|:--------------------------------:|
| 30 | 10000 | [-100, 100] | 100 | 0.5 | 2 | 1 |


**Resultados** 

* Posicion de la mejor particula
```python
[1.7511020696975077e-05, -2.069026525677592e-06, -3.904926253810421e-06, -9.675232433070568e-06, 4.977129619284357e-06, 1.0229853978338556e-05, -2.665932307642406e-06, -1.5331157347807865e-05, -1.54056126995521e-05, -2.6780591025210175e-06, 1.1634155715536576e-06, -7.682199062517945e-06, 5.434069700937737e-06, -4.335801853115365e-06, -8.280313164851055e-06, 1.234677884038824e-05, 9.790827923473237e-06, -1.6091758334714013e-05, -1.0631886053472801e-05, 9.158324930932285e-06, -8.638051405494647e-06, -7.3740263394020315e-06, 1.4089857378685494e-05, 4.881886532785882e-06, 1.5688811065572772e-05, 1.652525209604976e-05, -1.5354427189306463e-05, -4.749259081865544e-06, -1.0877309001033566e-05, -1.0949927765004995e-05]
 ```

* Datos de ejecución

| Parámetro              | Valor                    |
|------------------------|--------------------------|
| Función evaluada       | f4.py                    |
| Mejor aptitud obtenida | `1.7511020696975077e-05`  |
| Tiempo de ejecución    | `17.214 segundos`        |
| Valor mínimo de la función | 0 |

**Conclusiones**
```
Se puede observar como el resultado obtenido es bastante cercano al mínimo global de la función, aunque mas lejano que el primer problema.
Alcanzando un valor cercano a 0 de forma rápida, por lo que concluimos que el algoritmo funciona correctamente para este problema.
Aunque, es importante destacar, que para obtener estos resultados fue necesario aumentar la cantidad de particulas, disminuyendo el número de iteraciones y ajustar los pesos de las mejores posiciones locales y la mejor posición global, para priorizar la exploración de las soluciones.
```

### f8.py

**Funcion evaluada**

$f_8(\mathbf{x}) = \sum_{i=1}^{n} -x_i \sin(\sqrt{|x_i|})$

**Parametos usados para la ejecución**

| Número de dimensiones | Número de partículas | Espacio de búsqueda | Iteraciones | Peso de inercia | Peso de la mejor posición local | Peso de la mejor posición global |
|:---------------------:|:--------------------:|:------------------:|:-----------:|:---------------:|:-------------------------------:|:--------------------------------:|
| 30 | 10000 | [-500, 500] | 100 | 0.5 | 2 | 1 |


**Resultados**

* Posicion de la mejor particula
```python
[420.96874500742086, 420.96886469750217, 420.9685723550708, 420.968613197161, 420.96884341462714, 420.96886808536, -302.5250802346872, 420.9688922930749, 420.9689005906468, 420.9690084008145, 420.96898228042727, -302.5248994141379, -302.5249808704057, 420.968679437693, -302.52486900339255, -302.5249081063435, -302.5247632279272, -302.5246056139697, 420.96871949323463, 420.9686739569522, 420.96879126659, 420.96889805969806, -302.5248799249596, -302.5250119088655, 420.96844122034344, 203.81407404799563, 420.96881663477143, 420.9686706976138, 420.9687067344502, 420.9686896543691]
 ```

* Datos de ejecución

| Parámetro              | Valor                    |
|------------------------|--------------------------|
| Función evaluada       | f8.py                    |
| Mejor aptitud obtenida | `-11286.40193717558`  |
| Tiempo de ejecución    | `20.929 segundos`        |
| Valor mínimo de la función | -12569.5 |

**Conclusiones**

Se puede observar como el resultado obtenido aunque cercano, no se aproxima tanto al mínimo global de la función, como las funciones anteriores. 
Al analizar los resultados obtenidos, se ve como en la mejor solución tiene varias dimensiones que convergen en distintos mínimos locales y el mínimo global.
Siendo aquellas dimensiones cuyo valor se aproximó a 420 las que contribuyeron a alcanzar el mínimo global. Mientras que el resto las dimensiones que se aproximaron a -302 y 203, minimos locales de la función, impidieron a la particula acercarse al mínimo global de la función.
Asimismo, ya que la mejor particula tiene dimensiones atrapadas en mínimos locales, no ayuda o directamente entorpese al resto de particulas a obtener mejores resultados al acercar estas dimensiones a la supuesta mejor solucion.
Por lo tanto, el algoritmo PSO, no es adecuado para este problema, siendo la forma de obtener mejores resultados priorizar la exploración de las soluciones, incrementando el numero de particulas o el peso de la mejor posición local, para intentar que alguna particula consiga llegar al mínimo global en la mayoria de sus dimensiones.

## Explicación de código

- `Particle`: Clase que representa a las partículas que forman parte del enjambre, recibe el número de dimensiones y el rango del espacio de búsqueda. Inicializando la posición de forma aleatoria, la velocidad en 0, la mejor posicion pasada en su posicon actual y el fitness por defecto en infinito, para que sea actualizado despues de la inicialización.



- `PSO`: Clase que recibe todos los parámetros de configuración, como los pesos, la función para el cálculo del fitness, los rangos de búsqueda o el número de iteraciones y partículas. Esta clase tiene funciones para la actualización de las velocidades (getVelocity) y la posición (updatePosition) de las partículas.
Esta clase, crea el enjambre con sus particulas en la inicialización, junto a una función run para ejecutar el algoritmo PSO y retornar la posición y el fitness de la mejor particula encontrada.

- `Fitness`: son funciones encontradas en cada una de las implementaciones, y son enviadas a la clase PSO como argmento durante la inicialización de la clase. Estas funciones reciben la particula, a partir de la cual calcula el fitness.
