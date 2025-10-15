import tkinter as tk 
import time

def actualizar_reloj():
    hora_actual = time.strftime('%H:%M:%S')
    etiqueta_reloj.config(text=hora_actual)
    etiqueta_reloj.after(1000, actualizar_reloj) #llama a la funcion que actualiza cada un segundo

#configuracion de la ventana principal
ventana = tk.Tk()
ventana.title("Simple Watch")
ventana.geometry("300x150")

#Etiqueta para que se vea la hora
etiqueta_reloj = tk.Label(ventana,
                          font=("Helvetica", 48),
                          bg="black",
                          fg="cyan")
etiqueta_reloj.pack(expand=True)

#iniciar el reloj
actualizar_reloj()
ventana.mainloop()