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
        

def crear_coti():
    
    # Ocultar la ventana principal
    root.withdraw()
    
    # Ventana registro
    crear_coti = tk.Toplevel(root)
    crear_coti.title("Crear Cotización")
    crear_coti.geometry("700x713")
    crear_coti.resizable(False, False)
    crear_coti.configure(bg="#373737")
    crear_coti.protocol("WM_DELETE_WINDOW", cerrar_programa)

    # Crear un Canvas en la ventana de registro
    canvas_coti = tk.Canvas(crear_coti, width=700, height=713, bg="#373737", highlightthickness=0)
    canvas_coti.pack()                                  # 714

    # Nuevo registro
    canvas_coti.create_text(180, 0, text="Generar Cotización", anchor="nw", font=("Raleway", 30, "bold"), fill="White")

    # Cuadro arriba
    create_rounded_rectangle(canvas_coti, 10, 66, 690, 308, radius=10, fill="#959595", outline="#959595")

    create_rounded_rectangle(canvas_coti, 10, 318, 690, 386, radius=10, fill="#959595", outline="#959595")
    
    # tabla
    create_rounded_rectangle(canvas_coti, 10, 436, 690, 586, radius=10, fill="#959595", outline="#959595")
    
    create_rounded_rectangle(canvas_coti, 10, 596, 690, 664, radius=10, fill="#959595", outline="#959595")


    # Definimos las columnas para la tabla de materiales
    columns = ("descripcion", "material", "unidad", "preciounit", "subtotal")

    # Creamos la tabla
    tree_materiales = ttk.Treeview(crear_coti, columns=columns, show="headings")
    tree_materiales.place(x=10, y=436, width=681, height=151)

    # Configuramos los encabezados de cada columna
    tree_materiales.heading("descripcion", text="Descripción")
    tree_materiales.heading("material", text="Material")
    tree_materiales.heading("unidad", text="Unidad(es)")
    tree_materiales.heading("preciounit", text="Precio Unit.")
    tree_materiales.heading("subtotal", text="Sub Total")

    # Configuramos el ancho de cada columna
    tree_materiales.column("descripcion", anchor="center", width=180)
    tree_materiales.column("material", anchor="center", width=150)
    tree_materiales.column("unidad", anchor="center", width=30)
    tree_materiales.column("preciounit", anchor="center", width=30)
    tree_materiales.column("subtotal", anchor="center", width=30)


    # n° de cotizacion
    canvas_coti.create_text(20, 76, text="N° de Cotización", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 94, 170, 124, radius=10, fill="white", outline="#959595")

    input_gcoti = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gcoti.place(x=25, y=99, width=140, height=20)

    # fecha
    canvas_coti.create_text(180, 76, text="Fecha", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 180, 94, 370, 124, radius=10, fill="white", outline="#959595")

    input_gfecha = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gfecha.place(x=185, y=99, width=180, height=20)

    # empresa
    canvas_coti.create_text(380, 76, text="Empresa", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 380, 94, 530, 124, radius=10, fill="white", outline="#959595")

    input_gpersona = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gpersona.place(x=385, y=99, width=140, height=20)

    # area
    canvas_coti.create_text(540, 76, text="Área", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_area = ttk.Combobox(canvas_coti, values=["Escoja una Opción", "Ejemplo1"], state="readonly", font=("Raleway", 10))
    cbo_area.place(x=540, y=94, width=140, height=31)
    cbo_area.current(0)

    # persona
    canvas_coti.create_text(20, 134, text="Persona de Contacto", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 152, 200, 182, radius=10, fill="white", outline="#959595")

    input_gempresa = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gempresa.place(x=25, y=157, width=170, height=20)

    # titulo
    canvas_coti.create_text(210, 134, text="Título del Servicio", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 210, 152, 680, 182, radius=10, fill="white", outline="#959595")

    input_gtitulo = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gtitulo.place(x=215, y=157, width=460, height=20)

    # tiempo
    canvas_coti.create_text(20, 192, text="Tiempo de Ejecución", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 210, 290, 240, radius=10, fill="white", outline="#959595")

    input_gtiempo = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gtiempo.place(x=25, y=215, width=260, height=20)

    # tipo pago
    canvas_coti.create_text(300, 192, text="Forma de Pago", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 300, 210, 490, 240, radius=10, fill="white", outline="#959595")

    input_gpago = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gpago.place(x=305, y=215, width=180, height=20)

    # igv
    canvas_coti.create_text(500, 192, text="IGV", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_igv = ttk.Combobox(canvas_coti, values=["SI", "NO"], state="readonly", font=("Raleway", 10))
    cbo_igv.place(x=500, y=210, width=50, height=31)
    cbo_igv.current(0)

    # moneda
    canvas_coti.create_text(560, 192, text="Tipo de Moneda", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_moneda = ttk.Combobox(canvas_coti, values=["PEN", "USD"], state="readonly", font=("Raleway", 10))
    cbo_moneda.place(x=560, y=210, width=120, height=31)
    cbo_moneda.current(0)

    # cuenta banc
    canvas_coti.create_text(20, 250, text="Tipo de Cuenta", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_cuenta = ttk.Combobox(canvas_coti, values=["Cuenta Soles", "Cuenta Dólares"], state="readonly", font=("Raleway", 10))
    cbo_cuenta.place(x=20, y=268, width=130, height=31)
    cbo_cuenta.current(0)

    # nro cuenta
    canvas_coti.create_text(160, 250, text="Nro de Cuenta", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 160, 268, 410, 298, radius=10, fill="white", outline="#959595")

    input_gcuenta = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gcuenta.place(x=165, y=273, width=240, height=20)

    # cuenta interbanc
    canvas_coti.create_text(420, 250, text="Cuenta Interbancaria", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 420, 268, 680, 298, radius=10, fill="white", outline="#959595")

    input_gcuenta = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gcuenta.place(x=425, y=273, width=250, height=20)


    # desc
    canvas_coti.create_text(20, 328, text="Descripción", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 346, 190, 376, radius=10, fill="white", outline="#959595")

    input_gdesc = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gdesc.place(x=25, y=351, width=160, height=20)

    # material
    canvas_coti.create_text(200, 328, text="Material(es)", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 200, 346, 370, 376, radius=10, fill="white", outline="#959595")

    input_gmaterial = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gmaterial.place(x=205, y=351, width=160, height=20)

    # unidades
    canvas_coti.create_text(380, 329, text="Unidad(es)", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_unidad = ttk.Combobox(canvas_coti, values=["JUEGO", "PIEZA"], state="readonly", font=("Raleway", 10))
    cbo_unidad.place(x=380, y=347, width=100, height=31)
    cbo_unidad.current(0)

    create_rounded_rectangle(canvas_coti, 490, 346, 545, 376, radius=10, fill="white", outline="#959595")

    input_gunidad = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gunidad.place(x=495, y=351, width=45, height=20)

    # precio unit
    canvas_coti.create_text(555, 328, text="Precio Unitario", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 555, 346, 680, 376, radius=10, fill="white", outline="#959595")

    input_gpreciou = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gpreciou.place(x=560, y=351, width=115, height=20)


    # subtotal
    canvas_coti.create_text(20, 606, text="Sub Total", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 624, 130, 654, radius=10, fill="white", outline="#959595")

    input_gsubtot = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gsubtot.place(x=25, y=629, width=100, height=20)

    # +igv
    canvas_coti.create_text(140, 606, text="IGV", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 140, 624, 250, 654, radius=10, fill="white", outline="#959595")

    input_gigv = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gigv.place(x=145, y=629, width=100, height=20)

    # total
    canvas_coti.create_text(260, 606, text="Total", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 260, 624, 370, 654, radius=10, fill="white", outline="#959595")

    input_gigv = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gigv.place(x=265, y=629, width=100, height=20)


    # Botones opcion
    btn_ag = tk.Button(crear_coti, text="Agregar", width=20, height=1, font=("Raleway", 9))
    btn_ag.place(x=10, y=396)
    
    btn_ed = tk.Button(crear_coti, text="Editar", width=20, height=1, font=("Raleway", 9))
    btn_ed.place(x=169, y=396)
    
    btn_del = tk.Button(crear_coti, text="Agregar", width=20, height=1, font=("Raleway", 9))
    btn_del.place(x=328, y=396)
        
    btn_gen = tk.Button(crear_coti, text="Generar", width=20, height=1, font=("Raleway", 9))
    btn_gen.place(x=10, y=674)

    btn_canc = tk.Button(crear_coti, text="Cancelar", width=20, height=1, font=("Raleway", 9))
    btn_canc.place(x=169, y=674)


# Crear la ventana principal
root = tk.Tk()
root.title("Inicio")
root.geometry("1400x700")
root.resizable(False, False)  # Evitar que la ventana se redimensione
root.configure(bg="#373737")  
root.protocol("WM_DELETE_WINDOW", cerrar_programa)

# Crear un Canvas
canvas = tk.Canvas(root, width=1400, height=700, bg="#373737", highlightthickness=0)
canvas.pack()

# Cuadro opción
create_rounded_rectangle(canvas, 10, 10, 300, 389, radius=10, fill="#959595", outline="#959595")
                                            # 690                                 
# Cuadro filtro
create_rounded_rectangle(canvas, 10, 400, 300, 689, radius=10, fill="#959595", outline="#959595")
                                            
# tabla canvas
create_rounded_rectangle(canvas, 310, 80, 1289, 651, radius=10, fill="#959595", outline="#959595")

canvas.create_text(20, 22, text="Opciones", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

canvas.create_text(20, 412, text="Filtro", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

canvas.create_text(395, 23, text="Soluciones Plasticas Metálicas SAC", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

# Botones opcion
btn_cli = tk.Button(root, text="Registrar Nuevo Cliente", width=37, height=1, font=("Raleway", 9))
btn_cli.place(x=20, y=80)

btn_cot = tk.Button(root, text="Generar Cotización", width=37, height=1, font=("Raleway", 9), command=crear_coti)
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
btn_prev.place(x=880, y=660)

# filtro oc
canvas.create_text(20, 466, text="Por Orden de Compra", anchor="nw", font=("Raleway", 10), fill="black")

cbo_oc = ttk.Combobox(canvas, values=["Todos los registros", "Trabajo No Iniciado", "En Proceso", "Completado Parcialmente", "Finalizado"], state="readonly", font=("Raleway", 10))
cbo_oc.place(x=20, y=484, width=269, height=30)
cbo_oc.current(0)   #484

# filtro fac
canvas.create_text(20, 520, text="Por Factura", anchor="nw", font=("Raleway", 10), fill="black")

cbo_fac = ttk.Combobox(canvas, values=["Todos los registros", "Cancelado", "Pendiente", "No Cancelado"], state="readonly", font=("Raleway", 10))
cbo_fac.place(x=20, y=538, width=269, height=30)
cbo_fac.current(0)



# Buscador
search_canvas = tk.Canvas(root, width=350, height=40, bg="#373737", highlightthickness=0)
search_canvas.place(x=940, y=20)

create_rounded_rectangle(search_canvas, 0, 0, 350, 40, radius=10, fill="white", outline="gray")

search_entry = tk.Entry(search_canvas, font=("Raleway", 13), width=40, bd=0, relief="flat", fg='grey')
search_entry.insert(0, "Buscar...")  # Insertar texto de placeholder
search_entry.bind("<FocusIn>", clear_placeholder)  # Limpiar cuando el usuario hace clic
search_entry.bind("<FocusOut>", placeholder_search)  # Volver a mostrar si está vacío
search_entry.place(x=6, y=7, width=337, height=27)






# Tabla del cuadro base
tree = ttk.Treeview(root, columns=("oc", "estado_oc", "cliente", "descripcion", "fac", "estado_fac", "fecha_fac"), show="headings")
tree.place(x=310, y=80, width=980, height=572)

# Configurar las columnas
tree.heading("oc", text="Orden de Compra")
tree.heading("estado_oc", text="Estado")
tree.heading("cliente", text="Cliente")
tree.heading("descripcion", text="Descripción")
tree.heading("fac", text="Factura")
tree.heading("estado_fac", text="Estado")
tree.heading("fecha_fac", text="Fecha")

# Ajustar el tamaño de las columnas
tree.column("oc", anchor="center", width=70)
tree.column("estado_oc", anchor="center", width=100)
tree.column("cliente", anchor="center", width=150)
tree.column("descripcion", anchor="center", width=280)
tree.column("fac", anchor="center", width=100)
tree.column("fecha_fac", anchor="center", width=50)




# Ejecutar la interfaz
root.mainloop()
