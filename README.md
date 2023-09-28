# Librería de Teoría Cuántica

## Descripción 📑
---
Este es un proyecto que contiene funciones para simular experimentos de teoría cuántica sobre las probabilidades de hallar partículas en determinados puntos del espacio.

## Tabla de Contenidos 🗂️
---
Funciones incluidas en la librería:

1. Cálculo de la probabilidad de hallar una partícula en un punto de un vector de estados |ψ⟩
2. Calculo de la probabilidad de transitar de un vector de estados |ψ⟩ a otro vector de estados |φ⟩

## Requisitos 🧾
---
Para poder implementar la librería en su máquina local, se recomienda tener las siguientes ***especificaciones mínimas***:

- **Sistema Operativo:** Windows 8.1 / macOS 10.8 Mountain Lion / Linux Ubuntu 18.04 LTS Bionic Beaver
- **Procesador:** Intel Celeron / AMD Athlon
- **Almacenamiento:** 128 Gb (2 Gb libres)
- **Memoria RAM:** 4 Gb
- [IDE](https://es.wikipedia.org/wiki/Entorno_de_desarrollo_integrado) con soporte para Python [IDLE](https://docs.python.org/es/3/library/idle.html), [PyCharm](https://www.jetbrains.com/es-es/pycharm/download/?section=windows), [VSC](https://code.visualstudio.com/), [PyDev](https://www.pydev.org/), [Spyder](https://www.spyder-ide.org/), [Atom](https://github.com/atom))

Para una óptima implementación de la librería, se sugieren las siguientes ***especificaciones recomendadas***:

- **Sistema Operativo:** Windows 10 / macOS 13.0 Ventura / Linux Ubuntu 22.04 LTS Jammy Jellyfish
- **Procesador:** Intel Core i3 o i5 10ma Gen. / AMD Ryzen 3 o 5 Serie 3000 / Apple M1
- **Almacenamiento:** 256 Gb (4 Gb libres)- 
- **Memoria RAM:** 8 Gb
- [IDE](https://es.wikipedia.org/wiki/Entorno_de_desarrollo_integrado) con soporte para Python ([IDLE](https://docs.python.org/es/3/library/idle.html), [PyCharm](https://www.jetbrains.com/es-es/pycharm/download/?section=windows), [VSC](https://code.visualstudio.com/), [PyDev](https://www.pydev.org/), [Spyder](https://www.spyder-ide.org/), [Atom](https://github.com/atom))

## Comenzando 🚀
---
Para usar esta proyecto se recomienda seguir los siguientes pasos:

1. Crear una nueva carpeta en su máquina local
2. Dar clic derecho en el interior de la carpeta y abrir "Open Git Bush here"
3. Clonar el repositorio:
     ```sh
     $ git clone https://github.com/JAPV-X2612/Libreria_Teoria_Cuantica.git
     ```
4. Verificar que se hallan descargado 5 archivos
5. Salir de la terminal de Git:
     ```sh
     $ git exit
     ```

## Instalación 🔧
---
Una vez descargada una copia del repositorio en su máquina local, se recomienda:

1. Abrir el entorno de desarrollo integrado ([IDE](https://es.wikipedia.org/wiki/Entorno_de_desarrollo_integrado)) de su preferencia
2. Abrir el archivo `Pruebas Libreria_Teoria_Cuantica`
3. Instalar la librería `Numpy` en el IDE en caso de no tenerla
4. Ejecutar el intérprete de Python predeterminado
5. Verificar que no haya problemas de ejecución o errores
6. Si la respuesta fue `FAILED (failures=#)`, absténgase de usar la librería y reporte el error a jesus.pinzon-v@mail.escuelaing.edu.co
7. En otro caso, si la respuesta fue `OK`, entonces la librería está lista para su uso personal. 💻😎👍

## Ejecutando Pruebas ⚙️
---
A continuación se muestra un ejemplo de ejecución de cada función en [IDLE](https://docs.python.org/es/3/library/idle.html):

#### 1. Cálculo de la probabilidad de hallar una partícula en un punto de un vector de estados |ψ⟩
```
>>> Prob_Sist_Linea([-1j, 2.5-3j, 6+2j, 5-9j, -1+2j], 3)
     0.633781763826607
```

#### 2. Calculo de la probabilidad de transitar de un vector de estados |ψ⟩ a otro vector de estados |φ⟩
```
>>> Prob_Trans_Est([sqrt(2)/2j, -sqrt(2)/2], [sqrt(2)/2, sqrt(2)/2j])
     1.0000000000000004
``` 

## Textos y Wikis 📖
---
Para mayor información sobre los temas descritos en este proyecto se recomienda revisar los siguientes enlaces:

* [Números Complejos](https://es.wikipedia.org/wiki/N%C3%BAmero_complejo)
* [Qubit](https://es.wikipedia.org/wiki/C%C3%BAbit)
* [Computación Cuántica](https://es.wikipedia.org/wiki/Computaci%C3%B3n_cu%C3%A1ntica)
* [Quantum Computing for Computer Scientists](https://www.cambridge.org/core/books/quantum-computing-for-computer-scientists/8AEA723BEE5CC9F5C03FDD4BA850C711)

## Autor ✒️
---
Este proyecto es de la autoría de ***Jesús Alfonso Pinzón Vega***, Ingeniero de Sistemas de la Escuela Colombiana de Ingeniería Julio Garavito ([ECIJG](https://www.escuelaing.edu.co/es/)).  
**Correo:** jesus.pinzon-v@mail.escuelaing.edu.co

## Licencia 📄
---
Este proyecto tiene licencia de código abierto, por lo cual puede ser usado por cualquier persona u organización con fines educativos y de investigación. No obstante, está **PROHIBIDA SU DISTRIBUCIÓN** parcial o completa con fines lucrativos sin expreso consentimiento del autor.  
Se recomienda revisar el archivo [LICENSE](https://github.com/JAPV-X2612/Libreria_Simulacion_Clasico_a_Cuantico/blob/main/LICENSE.md) adjunto al repositorio para mayor información.

## Información Adicional 💡
---
También de recominda visitar las siguientes librerías de operaciones con objetos complejos para un mayor entendimiento de los temas tratados en este proyecto:

* [Librería con Números Complejos](https://github.com/JAPV-X2612/Libreria_Numeros_Complejos)
* [Librería de Operaciones con Vectores y Matrices Complejos](https://github.com/JAPV-X2612/Libreria_Vectores_Matrices_Complejos)
* [Librería de Simulación de lo Clásico a lo Cuántico](https://github.com/JAPV-X2612/Libreria_Simulacion_Clasico_a_Cuantico)

Próximamente se agregaran más funciones a la librería para ampliar su capacidad de cálculo y demostraciones de experimentos cuánticos...