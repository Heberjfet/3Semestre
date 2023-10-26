import serial
import tkinter as tk
from tkinter import Scale

# Configura la conexión serial con el Arduino (ajusta el puerto según sea necesario)
ser = serial.Serial('COM8', 9600)  # Cambia 'COM3' al puerto correcto

# Función para enviar el valor del slider al Arduino
def enviar_valor(valor):
    valor = int(valor)
    ser.write(f'{valor}\n'.encode())

# Crea una ventana
ventana = tk.Tk()
ventana.title("Control de Servomotor")

# Crea un slider para controlar la posición del servo
slider = Scale(ventana, from_=0, to=180, orient="horizontal", label="Ángulo del Servo")
slider.pack()

# Configura una función para enviar el valor cuando el slider se mueve
slider.bind("<Motion>", lambda event: enviar_valor(slider.get()))

# Cierra la conexión serial al cerrar la ventana
def cerrar_ventana():
    ser.close()
    ventana.destroy()

ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)
ventana.mainloop()
