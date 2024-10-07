import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from tkcalendar import DateEntry
import os
import shutil



def cerrar_programa():
    # Mostrar mensaje de confirmación al cerrar
    if messagebox.askokcancel("Salir", "¿Está seguro de que desea salir?"):
        root.quit()  # Detiene la ejecución del programa por completo
        


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


def placeholder_search(event):
    if search_entry.get() == "":
        search_entry.insert(0, "Buscar...")
        search_entry.config(fg='grey')

def clear_placeholder(event):
    if search_entry.get() == "Buscar...":
        search_entry.delete(0, tk.END)
        search_entry.config(fg='black')
        
        
# Crear la ventana principal
root = tk.Tk()
root.title("Inicio")
root.geometry("1300x700")
root.resizable(False, False)  # Evitar que la ventana se redimensione
root.configure(bg="#373737")  
root.protocol("WM_DELETE_WINDOW", cerrar_programa)

# Crear un Canvas
canvas = tk.Canvas(root, width=1300, height=700, bg="#373737", highlightthickness=0)
canvas.pack()

# Cuadro opción
create_rounded_rectangle(canvas, 10, 10, 300, 689, radius=10, fill="#959595", outline="#959595")
                                            # 690
# tabla canvas
create_rounded_rectangle(canvas, 310, 80, 1289, 651, radius=10, fill="#959595", outline="#959595")

canvas.create_text(20, 22, text="Opciones", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

canvas.create_text(395, 23, text="Soluciones Plasticas Metálicas SAC", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

# Botones opcion
btn_cli = tk.Button(root, text="Registrar Nuevo Cliente", width=37, height=1, font=("Raleway", 9))
btn_cli.place(x=20, y=80)

btn_cot = tk.Button(root, text="Generar Cotización", width=37, height=1, font=("Raleway", 9))
btn_cot.place(x=20, y=125)

btn_oc = tk.Button(root, text="Registrar Orden de Compra", width=37, height=1, font=("Raleway", 9))
btn_oc.place(x=20, y=170)

btn_sef = tk.Button(root, text="Seguimiento de Factura", width=37, height=1, font=("Raleway", 9))
btn_sef.place(x=20, y=215)

btn_bus = tk.Button(root, text="Búsqueda de Documentos", width=37, height=1, font=("Raleway", 9))
btn_bus.place(x=20, y=260)

btn_act = tk.Button(root, text="Actualizar Registro", width=37, height=1, font=("Raleway", 9))
btn_act.place(x=20, y=305)

btn_ex = tk.Button(root, text="Salir", width=37, height=1, font=("Raleway", 9), command=root.destroy)
btn_ex.place(x=20, y=350)

btn_next = tk.Button(root, text="Siguiente", width=20, height=1, font=("Raleway", 9))
btn_next.place(x=1140, y=660)

btn_prev = tk.Button(root, text="Atrás", width=20, height=1, font=("Raleway", 9))
btn_prev.place(x=980, y=660)

# filtro
cbo_filtro = ttk.Combobox(canvas, values=["Todos los registros", "Factura Cancelada", "Factura no Cancelada"], state="readonly", font=("Raleway", 10))
cbo_filtro.place(x=310, y=660, width=250, height=30)
cbo_filtro.current(0)


# Buscador
search_canvas = tk.Canvas(root, width=350, height=40, bg="#373737", highlightthickness=0)
search_canvas.place(x=940, y=20)

create_rounded_rectangle(search_canvas, 0, 0, 350, 40, radius=10, fill="white", outline="gray")

search_entry = tk.Entry(search_canvas, font=("Raleway", 13), width=40, bd=0, relief="flat", fg='grey')
search_entry.insert(0, "Buscar...")  # Insertar texto de placeholder
search_entry.bind("<FocusIn>", clear_placeholder)  # Limpiar cuando el usuario hace clic
search_entry.bind("<FocusOut>", placeholder_search)  # Volver a mostrar si está vacío
search_entry.place(x=6, y=7, width=337, height=27)


# Crear el estilo para el Treeview
style = ttk.Style()
style.configure("mystyle.Treeview", font=("Raleway", 11), rowheight=25)  # Cambiar tamaño de fuente y altura de fila
style.configure("mystyle.Treeview.Heading", font=("Raleway", 11))  # Cambiar tamaño de fuente de encabezados

# Crear la tabla
columns = ("N° de OC", "Estado", "Empresa - Cliente", "Descripción", "Estado de la factura", "Fecha")
table = ttk.Treeview(root, columns=columns, show="headings", style="mystyle.Treeview")

# Definir las columnas con tamaños específicos y desactivar el redimensionado con el mouse
table.heading("N° de OC", text="N° de OC")
table.column("N° de OC", width=90, anchor='center', stretch=False)

table.heading("Estado", text="Estado")
table.column("Estado", width=100, anchor='center', stretch=False)

table.heading("Empresa - Cliente", text="Empresa - Cliente")
table.column("Empresa - Cliente", width=200, anchor='center', stretch=False)

table.heading("Descripción", text="Descripción")
table.column("Descripción", width=250, anchor='center', stretch=False)

table.heading("Estado de la factura", text="Estado de la factura")
table.column("Estado de la factura", width=150, anchor='center', stretch=False)

table.heading("Fecha", text="Fecha")
table.column("Fecha", width=150, anchor='center', stretch=False)

# Agregar filas de prueba
for i in range(1, 21):
    table.insert("", "end", values=(f"OC-{i}", "Pendiente", f"Cliente {i}", f"Descripción {i}", "Sin factura", f"2024-10-{i+10}"))

# Colocar la tabla dentro del canvas
table.place(x=310, y=80, width=980, height=572)


# Ejecutar la interfaz
root.mainloop()
