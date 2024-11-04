#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# Inicializamos el EV3 y los motores
ev3 = EV3Brick()
motorB = Motor(Port.B)
motorC = Motor(Port.C)

# Configuramos un pitido de inicio
ev3.speaker.beep()

# Definimos la velocidad de movimiento en grados por segundo
velocidad = 200

# Movemos el robot hacia adelante durante 2 segundos
motorB.run(velocidad)
motorC.run(velocidad)
wait(2000)

# Detenemos los motores
motorB.stop(Stop.BRAKE)
motorC.stop(Stop.BRAKE)
wait(500)

# Movemos el robot hacia atrás durante 2 segundos
motorB.run(-velocidad)
motorC.run(-velocidad)
wait(2000)

# Detenemos los motores
motorB.stop(Stop.BRAKE)
motorC.stop(Stop.BRAKE)
