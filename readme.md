# SLAM-ROBOT-EV3-CORE-SET

Este proyecto **SLAM-ROBOT-EV3-CORE-SET** tiene como objetivo desarrollar y probar las capacidades de un robot construido con el conjunto LEGO Mindstorms EV3 para realizar mapeo y localización (SLAM). A través de pruebas individuales de cada sensor y motor, buscamos optimizar el rendimiento y entender mejor sus limitaciones en la implementación de un sistema de navegación autónomo.

## Archivos Principales

- **main.py**: Archivo principal que integra el control de sensores y motores del robot.
- **pc.py**: Script para establecer conexión con una computadora, permitiendo control y monitoreo externos.

## Pruebas de Sensores y Motores

### 1. Probando el Sensor de Color
Para verificar la precisión del sensor de color, se realizó una prueba específica en la que el robot identifica diferentes colores bajo condiciones controladas. Esta prueba permite evaluar cómo responde el sensor a distintos colores y su capacidad para realizar lecturas rápidas y precisas.

<video src="videos/sensors-motors/test-color-sensor.mp4" controls width="640"></video>

### 2. Probando el Sensor de Giroscopio
El sensor de giroscopio se probó para garantizar que puede detectar y medir los cambios en la orientación del robot. Esta funcionalidad es esencial para que el robot mantenga una trayectoria estable y recta.

<video src="videos/sensors-motors/test-gyro-sensor.mp4" controls width="640"></video>

### 3. Probando el Motor Medio
En esta prueba se verifica el funcionamiento del motor medio, que es utilizado para movimientos precisos y controlados. Es ideal para tareas donde se requiere un control detallado, como el giro de una herramienta o el control de un brazo robótico.

<video src="videos/sensors-motors/test-motor-medium.mp4" controls width="640"></video>

### 4. Pruebas de los Motores Principales
Los motores principales se evaluaron para garantizar un movimiento fluido y coordinado, esencial para la locomoción del robot. Estas pruebas ayudan a ajustar la velocidad y la respuesta de los motores para que el robot pueda desplazarse correctamente en diversas superficies.

<video src="videos/sensors-motors/test-robot-union.mp4" controls width="640"></video>

### 5. Probando el Sensor Ultrasónico
La prueba del sensor ultrasónico se centra en la capacidad del robot para detectar obstáculos a diferentes distancias. Esta función es crítica para la navegación autónoma y la prevención de colisiones.

<video src="videos/sensors-motors/test-sonic-sensor.mp4" controls width="640"></video>

### 6. Prueba de Conexión Wi-Fi
Para garantizar la comunicación remota con el robot, se realizó una prueba de conexión Wi-Fi. Esta conexión permite el monitoreo y control del robot desde una distancia, mejorando su capacidad de operar en entornos complejos.

<video src="videos/sensors-motors/test-wifi-conection.mp4" controls width="640"></video>

## Próximos Pasos
El siguiente paso en el proyecto es integrar todos estos componentes en un sistema de navegación autónoma que pueda mapear y localizarse en un espacio. Con los datos de estos sensores y motores, el robot podrá identificar su entorno y desplazarse de manera autónoma, completando así la base del sistema SLAM.

---

Este README se actualizará conforme el proyecto avance.
    