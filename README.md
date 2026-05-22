README:

Simulador de Combate: Análisis de Jerarquías

Descripción

Este programa es un simulador basado en la teoría de grafos que analiza el historial de enfrentamientos entre un grupo de luchadores. Utiliza conexiones direccionales (quién ha ganado a quién) para establecer un ranking oficial y predecir los ganadores de futuros combates mediante el cálculo de rutas lógicas y puntos de dominio.

Requisitos

Para ejecutar este programa, necesitas tener Python instalado  y las siguientes librerías:

* networkx (Para la creación y cálculos del grafo direccional)
* matplotlib (Para la visualización gráfica del mapa de jerarquía)

Puedes instalar las librerias ejecutando el siguiente comando en tu terminal:


pip install networkx matplotlib


 Características Principales

 Opción del Menú : Funcionalidad 
 1. Ver Ranking : Calcula los puntos de cada luchador sumando victorias directas y las victorias de los rivales derrotados (dominio indirecto). |
 2. Predecir Pelea : Analiza dos luchadores y busca la ruta más corta (O(V+E)) entre ellos. Si no hay conexión directa o indirecta, decide por puntos. |
 3. Ver Grafo : Genera una ventana interactiva con un mapa visual de nodos y flechas que representa toda la jerarquía de los combates históricos. |
 4. Salir : Termina la ejecución y muestra un reporte automático de eficiencia en consola con las funciones que más tiempo consumieron. |

 Cómo Ejecutarlo

Abre tu terminal, navega hasta la carpeta donde se encuentra el proyecto y ejecuta el archivo principal:


python simulador_combate.py


Notas Técnicas y Rendimiento

El núcleo del programa funciona mediante el algoritmo de Búsqueda en Anchura (BFS) gestionado por networkx.
El análisis de eficiencia integrado (cProfile) demuestra que las operaciones de predicción y cálculo de adyacencia se resuelven en tiempo casi instantáneo para bases de datos pequeñas y medianas, escalando de manera lineal.
