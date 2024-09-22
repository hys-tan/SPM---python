#IGNORAR ESTE ARCHIVO, SOLO ES DE PRUEBAS


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import DateEntry
import os

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




def ajustar_texto(texto, max_length=20):
    # Ajusta el texto para que no exceda la longitud máxima y agrega '...' al final si es necesario.
    if len(texto) > max_length:
        return texto[:max_length - 3] + '...'
    return texto

def adjuntar_archivo(label):
    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    if archivo:
        # Obtener solo el nombre del archivo
        nombre_archivo = os.path.basename(archivo)
        texto_ajustado = ajustar_texto(nombre_archivo)
        label.config(text=texto_ajustado)

def vent_registro():
    # Ventana registro
    new_reg = tk.Toplevel(root)
    new_reg.title("Nuevo Registro")
    new_reg.geometry("624x600")
    new_reg.resizable(False, False)
    new_reg.configure(bg="#373737")

    # Crear un Canvas en la ventana de registro
    canvas_reg = tk.Canvas(new_reg, width=624, height=600, bg="#373737", highlightthickness=0)
    canvas_reg.pack()

    # Nuevo registro
    canvas_reg.create_text(170, 10, text="Nuevo Registro", anchor="nw", font=("Raleway", 30, "bold"), fill="White")
    
    # Cuadro 1
    create_rounded_rectangle(canvas_reg, 10, 80, 307, 550, radius=10, fill="#959595", outline="#959595")

    # Cuadro 2
    create_rounded_rectangle(canvas_reg, 317, 80, 614, 550, radius=10, fill="#959595", outline="#959595")

    # coti--
    canvas_reg.create_text(20, 92, text="N° de Cotización", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_reg, 20, 110, 297, 140, radius=10, fill="white", outline="#959595")

    input_coti = tk.Text(new_reg, font=("Raleway", 11), bd=0)
    input_coti.place(x=25, y=115, width=267, height=20)
    
    # nombre--
    canvas_reg.create_text(20, 156, text="Empresa", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_reg, 20, 174, 297, 204, radius=10, fill="white", outline="#959595")
    
    input_nom = tk.Text(new_reg, font=("Raleway", 11), bd=0)
    input_nom.place(x=25, y=179, width=267, height=20)
    
    # descripcion--
    canvas_reg.create_text(20, 220, text="Descripción", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_reg, 20, 238, 297, 328, radius=10, fill="white", outline="#959595")
    
    input_desc = tk.Text(new_reg, font=("Raleway", 11), bd=0, wrap="word")
    input_desc.place(x=25, y=243, width=267, height=80)
    
    # tiempo de ejecucion
    canvas_reg.create_text(20, 344, text="Tiempo de Ejecución", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_reg, 20, 362, 297, 392, radius=10, fill="white", outline="#959595")
    
    input_temp = tk.Text(new_reg, font=("Raleway", 11), bd=0)
    input_temp.place(x=25, y=367, width=267, height=20)
    
    # costo
    canvas_reg.create_text(20, 408, text="Costo Estimado", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_reg, 20, 426, 297, 456, radius=10, fill="white", outline="#959595")
    
    label_costo = tk.Label(new_reg, text="S/.", font=("Raleway", 10), bg="white")
    label_costo.place(x=25, y=429)
    
    input_costo = tk.Text(new_reg, font=("Raleway", 11), bd=0)
    input_costo.place(x=50, y=431, width=242, height=20)
    
    # fecha de coti
    canvas_reg.create_text(20, 472, text="Fecha de Cotización", anchor="nw", font=("Raleway", 10), fill="black")
    
    date_entry = DateEntry(new_reg, font=("Raleway", 11), width=17, background='darkblue', foreground='white', borderwidth=2)
    date_entry.place(x=20, y=491, width=278, height=30)
    
    # DOCUMENTOS A ADJUNTAR
    
    # Cotizacion
    canvas_reg.create_text(327, 92, text="Doc. Cotización", anchor="nw", font=("Raleway", 10), fill="black")
    
    button_coti = tk.Button(new_reg, text="Seleccionar archivo", command=lambda: adjuntar_archivo(label_coti))
    button_coti.place(x=327, y=111, height=29)

    # Etiqueta para mostrar el nombre del archivo seleccionado
    global label_coti
    label_coti = tk.Label(new_reg, text="Ningún archivo seleccio...", font=("Raleway", 9), bg="#373737", fg="white")
    label_coti.place(x=450, y=111, width=155, height=29)
    
    # Orden de compra
    canvas_reg.create_text(327, 156, text="Doc. Orden de Compra", anchor="nw", font=("Raleway", 10), fill="black")
    
    button_oc = tk.Button(new_reg, text="Seleccionar archivo", command=lambda: adjuntar_archivo(label_oc))
    button_oc.place(x=327, y=175, height=29)
    
    global label_oc
    label_oc = tk.Label(new_reg, text="Ningún archivo seleccio...", font=("Raleway", 9), bg="#373737", fg="white")
    label_oc.place(x=450, y=175, width=155, height=29)
    
    # botones
    button_save = tk.Button(new_reg, text="Guardar", width=13, height=1, font=("Raleway", 9))
    button_save.place(x=207, y=560)
    
    button_cancel = tk.Button(new_reg, text="Cancelar", width=13, height=1, font=("Raleway", 9), command=new_reg.destroy)
    button_cancel.place(x=317, y=560)

# Crear la ventana principal
root = tk.Tk()
root.title("Inicio")
root.geometry("1300x700")
root.resizable(False, False)  # Evitar que la ventana se redimensione
root.configure(bg="#373737")  

# Crear un Canvas
canvas = tk.Canvas(root, width=1300, height=700, bg="#373737", highlightthickness=0)
canvas.pack()

# Cuadro opción
create_rounded_rectangle(canvas, 10, 10, 300, 690, radius=10, fill="#959595", outline="#959595")

# Cuadro base 690
create_rounded_rectangle(canvas, 312, 88, 1289, 651, radius=10, fill="#959595", outline="#959595")

canvas.create_text(22, 24, text="Opciones", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

canvas.create_text(435, 23, text="Soluciones Plasticas Metálicas SAC", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

# Botones base
button_sig = tk.Button(root, text="Siguiente", width=10, height=1, font=("Raleway", 9))
button_sig.place(x=1210, y=661)

button_ant = tk.Button(root, text="Anterior", width=10, height=1, font=("Raleway", 9))
button_ant.place(x=1118, y=661)

# Botones opcion
button_nr = tk.Button(root, text="Agregar Nuevo Registro", width=37, height=1, font=("Raleway", 9), command=vent_registro)
button_nr.place(x=22, y=88)

button_ar = tk.Button(root, text="Actualizar Registro", width=37, height=1, font=("Raleway", 9))
button_ar.place(x=22, y=134)

button_vd = tk.Button(root, text="Ver Detalles", width=37, height=1, font=("Raleway", 9))
button_vd.place(x=22, y=180)

button_allreg = tk.Button(root, text="Ver Todos los Registros", width=37, height=1, font=("Raleway", 9))
button_allreg.place(x=22, y=226)

button_exit = tk.Button(root, text="Salir", width=37, height=1, font=("Raleway", 9), command=root.destroy)
button_exit.place(x=22, y=272)

# Buscador
search_entry = tk.Entry(root, font=("Raleway", 11), width=23)
search_entry.place(x=1010, y=29, width=280, height=30)

# Tabla del cuadro base
tree = ttk.Treeview(root, columns=("cotizacion", "nombre", "ruc", "descripcion", "fecha", "cancelado"), show="headings")
tree.place(x=312, y=88, width=978, height=564)

# Configurar las columnas
tree.heading("cotizacion", text="N° de Cotización")
tree.heading("nombre", text="Empresa")
tree.heading("ruc", text="RUC")
tree.heading("descripcion", text="Descripción")
tree.heading("fecha", text="Fecha de Registro")
tree.heading("cancelado", text="Cancelado")

# Ajustar el tamaño de las columnas
tree.column("cotizacion", anchor="center", width=70)
tree.column("nombre", anchor="center", width=150)
tree.column("ruc", anchor="center", width=100)
tree.column("descripcion", anchor="center", width=280)
tree.column("fecha", anchor="center", width=100)
tree.column("cancelado", anchor="center", width=50)

# Ejecutar la interfaz
root.mainloop()
