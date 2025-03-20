# app.py
import tkinter as tk

def sumar():
    try:
        numero1 = float(entry1.get())
        numero2 = float(entry2.get())
        resultado = numero1 + numero2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa números válidos")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Suma")

# Crear y colocar los widgets
label1 = tk.Label(ventana, text="Número 1:")
label1.pack()

entry1 = tk.Entry(ventana)
entry1.pack()

label2 = tk.Label(ventana, text="Número 2:")
label2.pack()

entry2 = tk.Entry(ventana)
entry2.pack()

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack()

label_resultado = tk.Label(ventana, text="Resultado:")
label_resultado.pack()

# Iniciar la interfaz gráfica
ventana.mainloop()
