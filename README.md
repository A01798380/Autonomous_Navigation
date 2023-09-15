# Autonomous_Navigation
Este repositorio contiene un programa de simulación en Python para un rover en busca de un objetivo. Este permite que un rover navegue hacia un objetivo en un entorno bidimensional poblado de obstáculos. El rover se desplaza a una velocidad constante y ajusta su dirección para evitar chocar con los obstáculos detectados en su camino hacia el objetivo. Además, se garantiza que el rover mantenga una distancia de seguridad mínima tanto del objetivo como de los obstáculos.

=========================================================================================

Este algoritmo simula el movimiento de un rover en un entorno bidimensional con obstáculos mientras se dirige hacia un objetivo específico. El rover utiliza una estrategia de navegación para evitar choques con obstáculos y alcanzar su destino de manera segura. A continuación, se describen los pasos clave del algoritmo:

1. Generación de Coordenadas Aleatorias:

   - Se generan coordenadas aleatorias para el objetivo y los obstáculos en el espacio bidimensional. Estas coordenadas representan ubicaciones dentro del rango especificado en X y Y.

2. Inicialización del Rover y Obstáculos:

   - El rover comienza en una ubicación inicial en el espacio y se configuran los obstáculos alrededor del objetivo. También se define una distancia de seguridad mínima entre el rover y los obstáculos para evitar choques.

3. Movimiento hacia el Objetivo:

   - El rover inicia su movimiento hacia el objetivo utilizando una velocidad predefinida. Calcula el ángulo hacia el objetivo y avanza en esa dirección.

4. Detección de Obstáculos:

   - En cada paso, el algoritmo verifica si el rover está a punto de chocar con un obstáculo. Esto se hace calculando la distancia entre la posición actual del rover y la posición de los obstáculos.

5. Evitar los choques:

   - Si se detecta un posible choque con un obstáculo, el rover ajusta su dirección moviéndose en un ángulo aleatorio, esto le permite evadir eficientemente los obstáculos sin chocar.

6. Seguridad Adicional:

   - Además de evitar los obstáculos, el rover también verifica si está lo suficientemente lejos de estos para garantizar una distancia segura. Si no lo está, realiza ajustes para alejarse antes de continuar hacia el objetivo.

7. Registro de Coordenadas:

   - El algoritmo registra las coordenadas actuales del rover en cada paso para rastrear su trayectoria.

8. Visualización:

   - Se utiliza la biblioteca Turtle para visualizar el movimiento del rover y la posición de los obstáculos en una ventana gráfica.
