import socket

# Dirección IP del EV3 y el puerto que configuraste en el EV3
EV3_IP = '10.7.134.40'  # Reemplaza con la IP real de tu EV3
PORT = 12345

# Configuramos el socket para conectarnos al EV3
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((EV3_IP, PORT))

try:
    while True:
        # Recibimos datos desde el EV3
        data = client_socket.recv(1024)
        
        if data:
            # Imprimimos los datos recibidos (la distancia en este caso)
            print("Distancia recibida del EV3:", data.decode())
finally:
    # Cerramos el socket al terminar
    client_socket.close()
