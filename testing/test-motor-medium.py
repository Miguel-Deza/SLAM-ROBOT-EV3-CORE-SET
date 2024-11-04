#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# Inicializamos el EV3 y el motor en el puerto A
ev3 = EV3Brick()
motorA = Motor(Port.A)

# Configuramos la velocidad para el movimiento (en grados por segundo)
velocidad = 200

# Girar el motor una vuelta completa (360 grados) hacia adelante
motorA.run_target(velocidad, 360, Stop.BRAKE)
wait(500)  # Esperamos un momento

# Regresar el motor a la posición original (0 grados)
motorA.run_target(velocidad, 0, Stop.BRAKE)
