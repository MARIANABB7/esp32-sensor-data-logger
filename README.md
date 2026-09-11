# ESP32 Sensor Data Logger 🛡️📊

Este repositorio contiene un script en Python diseñado para registrar y almacenar lecturas de sensores (Temperatura, Humedad y Presión) provenientes de un microcontrolador **ESP32** a través de comunicación por puerto serie (UART).

---

## 🛠️ Requisitos e Instalación

Para ejecutar este código se requiere **Python 3.x** y la biblioteca `pyserial`.

Puedes instalar las dependencias ejecutando:

---

## 🚀 Uso

1. Conecta tu ESP32 a la computadora mediante USB.
2. Identifica el puerto COM asignado (ejemplo: `COM4` en Windows o `/dev/ttyUSB0` en Linux/Mac).
3. Modifica la variable `puerto` en el archivo `pra5.py` si es necesario:
4. Ejecuta el archivo desde la terminal:

El programa recopilará los datos enviados por el ESP32 y los guardará automáticamente en un archivo local denominado `datos_sensores.csv`.

---

## 📋 Estructura de Salida (`datos_sensores.csv`)

| Temperatura | Humedad | Presion |
| ----------- | ------- | ------- |
| 24.5        | 55.0    | 1013.2  |
