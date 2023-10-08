import tkinter as tk

def borrar():
    entry1.delete(0,tk.END)
    entry1.insert(0,"0.0")
    entry2.delete(0,tk.END)
    entry2.insert(0,"0.0")

def convert_celcius():
    faren = float(entry1.get())
    cels = (faren -32)*5.0/0.9
    entry1.delete(0,tk.END)
    entry2.insert(0,f"{faren:.2}")

def convert_faren():
    cels = float(entry2.get())
    faren = (cels*9/5)+32
    entry2.delete(0,tk.END)
    entry1.insert(0,f"{cels:.2}")


App = tk.Tk()
App.title("Volumenes")

labell = tk.Label(App,text ="volumenes de un cilindro")
labell.grid(row=0, column=0)

entry1 = tk.Entry(App)
entry1.grid(row=0, column=1)

buttonl = tk.Button(App,text= "Convertir a Celsius",command=convert_celcius)
buttonl.grid(row=0, column=2)

label2 = tk.Label(App, text="celsius")
label2.grid(row=1, column=0)

entry2 =tk.Entry(App)
entry2.grid(row=1, column= 1)

button2 =tk.Button(App, text="Convertir a Fahrenheit", command=convert_faren)
button2. grid(row=1, column=2)

button3 = tk.Button(App, text= "Restablecer",command = borrar)
button3.grid(row=2, column=1)

App.mainloop()
