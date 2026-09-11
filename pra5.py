import serial
import csv
import time

# CONFIGURA TU PUERTO (IMPORTANTE)
puerto = 'COM4'   # Cambia si es diferente
baudrate = 115200

# Número de datos a guardar
limite_datos = 10000

# Nombre del archivo
archivo_csv = 'datos_sensores.csv'

try:
    ser = serial.Serial(puerto, baudrate, timeout=1)
    time.sleep(2)  # Espera a que el ESP32 reinicie

    print("Conectado al puerto:", puerto)

    with open(archivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Encabezados
        writer.writerow(["Temperatura", "Humedad", "Presion"])

        contador = 0

        while contador < limite_datos:
            linea = ser.readline().decode('utf-8').strip()

            if linea:
                try:
                    datos = linea.split(",")

                    if len(datos) == 3:
                        writer.writerow(datos)
                        contador += 1

                        print(f"{contador}: {datos}")
                
                except:
                    print("Error en datos:", linea)

    print("Datos guardados en", archivo_csv)

except Exception as e:
    print(" Error:", e)
    