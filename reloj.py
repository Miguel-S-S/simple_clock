import tkinter as tk 
import time

def actualizar_reloj_argentina():
    hora_actual = time.strftime('%H:%M:%S')  
    reloj_argentina.config(text=hora_actual)
    reloj_argentina.config(font=("Courier", 36, "bold"))
    reloj_argentina.after(1000, actualizar_reloj_argentina) # la magia de la recursividad

def actualizar_reloj_paraguay():
    uso_horario_paraguay = time.localtime(time.time() - 3600)  # Paraguay es una hora menos de Argentina
    hora_actual = time.strftime('%H:%M:%S', uso_horario_paraguay)
    reloj_paraguay.config(text=hora_actual)
    reloj_paraguay.config(font=("Courier", 36, "bold"))
    reloj_paraguay.after(1000, actualizar_reloj_paraguay)

def actualizar_reloj_españa():
    uso_horario_españa = time.localtime(time.time() + 5 * 3600)  # 
    hora_actual = time.strftime('%H:%M:%S', uso_horario_españa)
    reloj_españa.config(text=hora_actual)
    reloj_españa.config(font=("Courier", 36, "bold"))
    reloj_españa.after(1000, actualizar_reloj_españa) # la magia de la recursividad

def actualizar_reloj_grecia():
    uso_horario_grecia = time.localtime(time.time() + 6 * 3600)  # 
    hora_actual = time.strftime('%H:%M:%S', uso_horario_grecia)
    reloj_grecia.config(text=hora_actual)
    reloj_grecia.config(font=("Courier", 36, "bold"))
    reloj_grecia.after(1000, actualizar_reloj_grecia) 

def crear_contenedor_de_relojes(contenedor, fila, columna, nombre_pais, fuente_pais, color_fondo_pais, color_texto_pais):
    etiqueta_pais = tk.Label(contenedor,
                             font=fuente_pais,
                             bg=color_fondo_pais,
                             fg=color_texto_pais,
                             text=nombre_pais)
    etiqueta_pais.grid(row=fila, column=columna, sticky="s", padx=10, pady=25)

    etiqueta_hora = tk.Label(contenedor,
                             font=("Arial", 24),
                             bg="black",
                             fg="cyan")
    etiqueta_hora.grid(row=fila + 1, column=columna, sticky="n", padx=10, pady=15)

    return etiqueta_hora

#configuracion de la ventana principal
ventana = tk.Tk()
ventana.title("Reloj Mundial")
ventana.geometry("550x400")

reloj_argentina = crear_contenedor_de_relojes(ventana, 0, 0, "Argentina",
                                             fuente_pais=("gothic", 16, "bold"),
                                             color_fondo_pais="blue",
                                             color_texto_pais="white")

reloj_paraguay = crear_contenedor_de_relojes(ventana, 0, 1, "Paraguay",
                                             fuente_pais=("italic", 16, "bold"),
                                             color_fondo_pais="red",
                                             color_texto_pais="darkblue")

reloj_españa = crear_contenedor_de_relojes(ventana,
                                            2, 0,
                                           "España", 
                                           fuente_pais=("Times New Roman", 16, "bold"),
                                           color_fondo_pais="red", 
                                           color_texto_pais="yellow")

reloj_grecia = crear_contenedor_de_relojes(ventana,
                                           2, 1, 
                                           "Grecia", 
                                            fuente_pais=("Helvetica", 16, "italic"),
                                           color_fondo_pais="lightblue", 
                                           color_texto_pais="darkblue")

#iniciar el reloj
actualizar_reloj_paraguay()
actualizar_reloj_argentina()
actualizar_reloj_españa()
actualizar_reloj_grecia()
ventana.mainloop()