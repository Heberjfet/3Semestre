import serial
import tkinter as tk

# Configura el puerto serie
puerto = serial.Serial('COM7', 9600)

def enviar_angulo(angulo):
    # Envia el ángulo al Arduino
    puerto.write('<{}>'.format(angulo).encode())

# Crea la ventana de la aplicación
root = tk.Tk()
root.title("Control del Servomotor")

# Crea el control deslizante
scale = tk.Scale(root, from_=0, to=180, orient='horizontal', command=enviar_angulo)
scale.pack(fill='x')

# Inicia la aplicación
root.mainloop()
