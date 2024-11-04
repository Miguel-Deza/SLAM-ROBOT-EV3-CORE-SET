#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Inicializamos el EV3 y el sensor giroscópico en el puerto S2
ev3 = EV3Brick()
gyro = GyroSensor(Port.S2)

# Restablecemos el sensor giroscópico para comenzar en ángulo cero
gyro.reset_angle(0)

# Bucle infinito para mostrar el ángulo detectado
while True:
    # Obtenemos el ángulo actual del giroscopio
    angulo = gyro.angle()
    
    # Mostramos el ángulo en la pantalla del EV3
    ev3.screen.clear()
    ev3.screen.draw_text(0, 50, "Angulo: " + str(angulo))
    
    # Espera breve para que la lectura sea más estable
    wait(200)
