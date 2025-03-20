import tkinter as tk

# Función de suma que puede ser testeada sin la interfaz
def sumar(numero1, numero2):
    return numero1 + numero2

def interfaz():
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

    label_resultado = tk.Label(ventana, text="Resultado:")
    label_resultado.pack()

    def sumar_interfaz():
        try:
            numero1 = float(entry1.get())
            numero2 = float(entry2.get())
            resultado = sumar(numero1, numero2)
            label_resultado.config(text=f"Resultado: {resultado}")
        except ValueError:
            label_resultado.config(text="Por favor, ingresa números válidos")

    boton_sumar = tk.Button(ventana, text="Sumar", command=sumar_interfaz)
    boton_sumar.pack()

    # Iniciar la interfaz gráfica
    ventana.mainloop()
