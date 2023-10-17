import tkinter as tk
import serial
from tkinter import Scale

# Configura el puerto serie de Arduino
arduino_port = "COM5"  # Cambia esto al puerto que esté utilizando tu Arduino
arduino_baudrate = 9600

# Inicializa la comunicación serial
arduino = serial.Serial(arduino_port, arduino_baudrate, timeout=1)

def set_servo_position(position):
    # Envía el comando al Arduino para mover el servomotor a la posición deseada
    command = f"S{position}\n"
    arduino.write(command.encode())

# Función para actualizar la posición del servomotor con el scroll del ratón
def update_servo_position(event):
    position = servo_position.get()
    position += event.delta // 120  # Utiliza el evento del scroll del ratón para mover el servo
    position = max(0, min(180, position))  # Limita el rango de movimiento del servo
    servo_position.set(position)
    set_servo_position(position)

# Configura la interfaz gráfica
window = tk.Tk()
window.title("Control de Servomotor")
window.geometry("400x200")

servo_position = Scale(window, from_=0, to=180, orient="horizontal", label="Posición del Servomotor")
servo_position.pack(pady=20)

# Asocia la función de actualización con el evento del scroll del ratón
window.bind("<MouseWheel>", update_servo_position)

window.mainloop()
