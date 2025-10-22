import tkinter as tk 
import time


def actualizar_reloj():
    hora_actual = time.strftime('%H:%M:%S')
    etiqueta_reloj_1.config(text=hora_actual)
    etiqueta_reloj_1.after(1000, actualizar_reloj) #llama a la funcion que actualiza cada un segundo

    etiqueta_reloj_2.config(text=hora_actual)
    etiqueta_reloj_2.after(1000, actualizar_reloj)

#configuracion de la ventana principal
ventana = tk.Tk()
ventana.title("Simple Watch")
ventana.geometry("700x350")


etiqueta_Argentina = tk.Label(ventana, text="Buenos Aires", font=("Arial",25), fg="white", bg="blue")
etiqueta_Argentina.grid(row=0,column=1)

#Etiqueta para que se vea la hora
etiqueta_reloj_1 = tk.Label(ventana,
                          font=("Helvetica", 48),
                          bg="black",
                          fg="yellow",
                          padx=10)
etiqueta_reloj_1.grid(row=1,column=1)

etiqueta_España = tk.Label(ventana, text="Madrid", font=("Arial",25), fg="red", bg="yellow")
etiqueta_España.grid(row=0,column=0)

etiqueta_reloj_2 = tk.Label(ventana,
                          font=("Helvetica", 48),
                          bg="black",
                          fg="yellow",
                          padx=10)
etiqueta_reloj_2.grid(row=1,column=0)


#iniciar el reloj
actualizar_reloj()
ventana.mainloop()
