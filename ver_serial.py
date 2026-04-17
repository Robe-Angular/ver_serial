import serial
import time

PUERTO = '/dev/ttyUSB0'   # cámbialo si tu Arduino salió como ttyUSB0
BAUDIOS = 9600

ser = serial.Serial(PUERTO, BAUDIOS, timeout=1)
time.sleep(2)  # esperar reinicio del Arduino

print(f"Escuchando {PUERTO} a {BAUDIOS} baudios... Ctrl+C para salir.")

try:
    while True:
        if ser.in_waiting > 0:
            linea = ser.readline().decode('utf-8', errors='ignore').strip()
            if linea:
                print(linea)
except KeyboardInterrupt:
    print("\nSaliendo...")
finally:
    ser.close()