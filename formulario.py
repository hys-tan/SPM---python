import tkinter as tk

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=10, **kwargs):
    points = [
        x1 + radius, y1,
        x1 + radius, y1,
        x2 - radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

# Crear la ventana principal
root = tk.Tk()
root.title("Inicio")
root.geometry("1300x700")
root.resizable(False, False)  # Evitar que la ventana se redimensione

# Crear un Canvas
canvas = tk.Canvas(root, width=1300, height=700)
canvas.pack()

# Dibujar un rectángulo redondeado
create_rounded_rectangle(canvas, 10, 10, 300, 690, radius=10, fill="lightgray", outline="black")

create_rounded_rectangle(canvas, 312, 88, 1289, 690, radius=10, fill="lightgray", outline="black")


canvas.create_text(20, 29, text="Opciones", anchor="nw", font=("Arial", 20, "bold"))

canvas.create_text(385, 29, text="Soluciones Plasticas Metálicas SAC", anchor="nw", font=("Arial", 20, "bold"))


# Crear un botón de dimensiones 270x30 en las coordenadas x=20, y=94
button = tk.Button(root, text="Agregar Nueva Cotización", width=37, height=1)
button.place(x=20, y=94)

button = tk.Button(root, text="Actualizar Registro", width=37, height=1)
button.place(x=20, y=140)

button = tk.Button(root, text="Salir", width=37, height=1)
button.place(x=20, y=186)


search_entry = tk.Entry(root, font=("Arial", 10), width=23)
search_entry.place(x=920, y=29, width=370, height=30)


# Ejecutar la interfaz
root.mainloop()
