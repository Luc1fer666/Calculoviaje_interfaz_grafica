import tkinter as tk
from tkinter import messagebox

# Funciones del programa
def calcular_tiempo_viaje(distancia, velocidad):
    tiempo_horas = distancia / velocidad
    horas = int(tiempo_horas)
    minutos = int((tiempo_horas - horas) * 60)
    return horas, minutos

def sugerir_parada(tiempo_horas):
    if tiempo_horas > 5:
        return "Es recomendable hacer una parada de descanso."
    return ""

def calcular():
    try:
        distancia = float(entry_distancia.get())
        velocidad = float(entry_velocidad.get())

        if velocidad <= 0:
            messagebox.showerror("Error", "La velocidad debe ser mayor que cero.")
            return

        horas, minutos = calcular_tiempo_viaje(distancia, velocidad)
        tiempo_total_horas = horas + minutos / 60

        resultado = f"Tiempo estimado de viaje: {horas} horas y {minutos} minutos."
        label_resultado.config(text=resultado)

        sugerencia = sugerir_parada(tiempo_total_horas)
        if sugerencia:
            label_sugerencia.config(text=sugerencia)
        else:
            label_sugerencia.config(text="")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Tiempo de Viaje")
ventana.geometry("400x300")

# Widgets de la interfaz
label_distancia = tk.Label(ventana, text="Distancia (km):")
label_distancia.pack(pady=5)

entry_distancia = tk.Entry(ventana)
entry_distancia.pack(pady=5)

label_velocidad = tk.Label(ventana, text="Velocidad (km/h):")
label_velocidad.pack(pady=5)

entry_velocidad = tk.Entry(ventana)
entry_velocidad.pack(pady=5)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack(pady=10)

label_resultado = tk.Label(ventana, text="", font=("Arial", 12))
label_resultado.pack(pady=5)

label_sugerencia = tk.Label(ventana, text="", font=("Arial", 10), fg="green")
label_sugerencia.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
