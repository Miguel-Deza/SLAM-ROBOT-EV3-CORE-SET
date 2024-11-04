#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Inicializamos el EV3 y el sensor ultrasónico en el puerto S1
ev3 = EV3Brick()
ultrasonic_sensor = UltrasonicSensor(Port.S1)

# Distancia límite en centímetros para activar el pitido
distancia_limite = 10  # Puedes cambiar este valor a la distancia deseada

# Bucle infinito para verificar continuamente la distancia
while True:
    # Medimos la distancia actual en centímetros
    distancia = ultrasonic_sensor.distance()

    # Si la distancia es menor o igual a la distancia límite, hacer un pitido
    if distancia <= distancia_limite * 10:  # Convertimos la distancia a mm
        ev3.speaker.beep()

    # Pequeña pausa para evitar lecturas muy rápidas
    wait(200)
