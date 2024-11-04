#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Inicializamos el EV3 y el sensor de color
ev3 = EV3Brick()
color_sensor = ColorSensor(Port.S4)

# Bucle infinito para revisar continuamente el color detectado
while True:
    # Detecta el color actual
    color_detectado = color_sensor.color()
    
    # Si el color detectado es rojo, hacer un pitido
    if color_detectado == Color.RED:
        ev3.speaker.beep()
    
    # Pequeña pausa para no saturar el procesador
    wait(100)
