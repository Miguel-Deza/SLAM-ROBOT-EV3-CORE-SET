#!/usr/bin/env pybricks-micropython
import socket
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Inicializamos el EV3 y el sensor ultrasónico en el puerto S1
ev3 = EV3Brick()
ultrasonic_sensor = UltrasonicSensor(Port.S1)

# Configuramos el socket para que el EV3 actúe como servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 12345))  # Usamos el puerto 12345
server_socket.listen(1)  # Escucha hasta una conexión

# Aceptamos la conexión
print("Esperando conexión...")
client_socket, address = server_socket.accept()
print("Conectado a:", address)

try:
    while True:
        # Medimos la distancia con el sensor ultrasónico
        distancia = ultrasonic_sensor.distance()
        
        # Enviamos la distancia a la computadora
        client_socket.send(str(distancia).encode())
        
        # Espera breve antes de la próxima lectura
        wait(1000)
finally:
    # Cerramos el socket al terminar
    client_socket.close()
    server_socket.close()
