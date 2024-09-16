import tkinter as tk
from tkinter import ttk

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

# Cuadro opción
create_rounded_rectangle(canvas, 10, 10, 300, 690, radius=10, fill="lightgray", outline="black")

# Cuadro base 690
create_rounded_rectangle(canvas, 312, 88, 1289, 655, radius=10, fill="lightgray", outline="black")


canvas.create_text(20, 29, text="Opciones", anchor="nw", font=("Arial", 20, "bold"))

canvas.create_text(435, 29, text="Soluciones Plasticas Metálicas SAC", anchor="nw", font=("Arial", 20, "bold"))

# Botones base 1210
button_sig = tk.Button(root, text="Siguiente", width=10, height=1)
button_sig.place(x=1210, y=665)

button_ant = tk.Button(root, text="Anterior", width=10, height=1)
button_ant.place(x=1120, y=665)


# Botones opcion
button_nr = tk.Button(root, text="Agregar Nuevo Registro", width=37, height=1)
button_nr.place(x=20, y=94)

button_ar = tk.Button(root, text="Actualizar Registro", width=37, height=1)
button_ar.place(x=20, y=140)

button_vd = tk.Button(root, text="Ver Detalles", width=37, height=1)
button_vd.place(x=20, y=186)

button_allreg = tk.Button(root, text="Ver Todos los Registros", width=37, height=1)
button_allreg.place(x=20, y=232)

button_exit = tk.Button(root, text="Salir", width=37, height=1, command=root.destroy)
button_exit.place(x=20, y=278)

# Buscador
search_entry = tk.Entry(root, font=("Arial", 10), width=23)
search_entry.place(x=1010, y=29, width=280, height=30)


# Tabla del cuadro base
tree = ttk.Treeview(root, columns=("cotizacion", "nombre", "ruc", "descripcion", "fecha", "cancelado"), show="headings")
tree.place(x=312, y=88, width=978, height=568) #w-977 / h-567

# Configurar las columnas
tree.heading("cotizacion", text="N° de Cotización")
tree.heading("nombre", text="Nombre/Empresa")
tree.heading("ruc", text="RUC")
tree.heading("descripcion", text="Descripción")
tree.heading("fecha", text="Fecha de Registro")
tree.heading("cancelado", text="Cancelado")

# Ajustar el tamaño de las columnas
tree.column("cotizacion", anchor="center", width=100)
tree.column("nombre", anchor="center", width=150)
tree.column("ruc", anchor="center", width=100)
tree.column("descripcion", anchor="center", width=200)
tree.column("fecha", anchor="center", width=100)
tree.column("cancelado", anchor="center", width=80)


# Ejecutar la interfaz
root.mainloop()