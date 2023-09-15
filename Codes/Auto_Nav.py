#Código realizado por Ulises Jaramillo Portilla; A01798380.
#Reto área de programación Quantum Robotics: Autonomous Navigation.

#========================================================================

#Importamos las librerías necesarias para nuestro código.
import random
import math
import turtle as t


# Función para calcular la distancia entre dos puntos.
def distancia_entre_puntos(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Función para verificar choques con obstáculos.
def verificar_choq(x, y, obstaculos, radio_choq):
    for obstaculo_x, obstaculo_y in obstaculos:
        distancia = distancia_entre_puntos(x, y, obstaculo_x, obstaculo_y)
        if distancia < radio_choq:
            return True  # Muy cerca del choque.
    return False  # No hay posible choque.


# Definimos el rango de coordenadas en X y Y en metros.
rango_X = (-10, 10) 
rango_Y = (-10, 10) 


# Se generan las coordenadas aleatorias para el objetivo.
X_aruco = random.uniform(rango_X[0], rango_X[1])
Y_aruco = random.uniform(rango_Y[0], rango_Y[1])


# Se imprimen las coordenadas generadas en terminal para su primer visualización.
print(f"Coordenada X del código ArUco: {X_aruco} metros")
print(f"Coordenada Y del código ArUco: {Y_aruco} metros")


# Se definen las coordenadas aproximadas del código ArUco (objetivo).
X_aruco_objetivo = X_aruco 
Y_aruco_objetivo = Y_aruco 


# Se define una distancia final para considerar que el robot ha llegado al objetivo.
distancia_final = 0.1  


# Se define la velocidad de movimiento del robot.
velocidad = 0.2  

# Se inicializan las coordenadas actuales del robot.
XR = 0.0
YR = 0.0


# Se generan obstáculos alrededor del objetivo.
num_obstaculos = 10 
radio_choq = 0.5  # Radio de seguridad para evitar obstáculos.
obstaculos = []
for _ in range(num_obstaculos):
    angulo = random.uniform(0, 2 * math.pi)
    distancia = random.uniform(1.0, 3.0)  # Controla la distancia de los obstáculos al objetivo.
    obstaculo_x = X_aruco_objetivo + distancia * math.cos(angulo)
    obstaculo_y = Y_aruco_objetivo + distancia * math.sin(angulo)
    obstaculos.append((obstaculo_x, obstaculo_y))


# Se define la posición de un obstáculo fijo en línea recta entre el rover y el objetivo para forzar la evasión
# para visualizar el funcionamiento.
posicion_obstaculo_x = (X_aruco_objetivo + XR) / 2
posicion_obstaculo_y = (Y_aruco_objetivo + YR) / 2


# Se agrega el obstáculo a la lista de obstáculos.
obstaculos.append((posicion_obstaculo_x, posicion_obstaculo_y))


# Configuración de la ventana de Turtle.
t.speed(1)  # Velocidad de dibujo baja para visualizar claramente.
t.title("Trayectoria del Rover")


# Se dibuja un cuadrado representando el mapa de nuestra simulación.
t.penup()
t.goto(-250, -250)
t.pendown()
t.goto(250, -250)
t.goto(250, 250)
t.goto(-250, 250)
t.goto(-250, -250)


# Se dibujan las coordenadas iniciales del robot y objetivo en la parte superior.
t.penup()
t.goto(-250, 290) 
t.pendown()
t.write(f"Inicial - Coordenadas del Rover: ({XR}, {YR}) - Objetivo: ({X_aruco_objetivo}, \
    {Y_aruco_objetivo})", align="left", font=("Arial", 12, "normal"))


# Se dibujan los puntos en base las coordenadas actuales del robot y objetivo.
t.penup()
t.goto(XR * 20, YR * 20)  # Se escalan las coordenadas para que quepan en la ventana de Turtle.
t.pendown()
t.dot(10, "green")  # Robot.
t.penup()
t.goto(X_aruco_objetivo * 20, Y_aruco_objetivo * 20)
t.pendown()
t.dot(10, "red")  # Objetivo final.


# Se dibujan los obstáculos.
for obstaculo_x, obstaculo_y in obstaculos:
    t.penup()
    t.goto(obstaculo_x * 20, obstaculo_y * 20)
    t.pendown()
    t.dot(7, "black")  # Obstáculos.


# Se inicializa la lista para almacenar las coordenadas actuales.
coordenadas = []


# Mientras la distancia al objetivo sea mayor que la distancia final.
while distancia_entre_puntos(XR, YR, X_aruco_objetivo, Y_aruco_objetivo) > distancia_final:
    # Se calcula la dirección hacia el objetivo.
    angulo_objetivo = math.atan2(Y_aruco_objetivo - YR, X_aruco_objetivo - XR)
    
    # Se calcula el movimiento en X y Y para acercarse al objetivo.
    delta_X = velocidad * math.cos(angulo_objetivo)
    delta_Y = velocidad * math.sin(angulo_objetivo)
    
    # Se verifica si se va a chocar con los obstáculos.
    if verificar_choq(XR + delta_X, YR + delta_Y, obstaculos, radio_choq):
        # Si se acerca mucho, se ajusta la dirección para alejarse del obstáculo.
        angulo_objetivo += random.uniform(math.pi / 2, math.pi)  # El ajuste es en un ángulo aleatorio hacia afuera.
    
    # Se actualizan las coordenadas actuales del robot.
    XR += velocidad * math.cos(angulo_objetivo)
    YR += velocidad * math.sin(angulo_objetivo)
    
    # Se añade las coordenadas actuales a la lista.
    coordenadas.append((XR, YR))
    
    # Se dibuja la nueva posición de nuestro robot.
    t.penup()
    t.goto(XR * 20, YR * 20)
    t.pendown()
    t.dot(5, "blue")


# Se dibujan las coordenadas en el costado para visualizar en cada paso que se dió.
t.penup()
t.goto(290, 250) 
t.pendown()
t.write("Coordenadas:", align="left", font=("Arial", 12, "normal"))


for i, (x, y) in enumerate(coordenadas, start=1):
    t.penup()
    t.goto(290, 240 - i * 20)
    t.pendown()
    t.write(f"Paso {i}: ({x:.2f}, {y:.2f})", align="left", font=("Arial", 12, "normal"))


# Comando para cerrar la ventana de Turtle al hacer clic.
t.exitonclick()

