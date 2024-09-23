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


# Función para crear las carpetas si no existen
def crear_carpetas_adjuntar():
    # Carpeta principal
    carpeta_principal = "documentos_adjuntar"
    
    # Subcarpetas para cada tipo de documento
    carpetas_sub = ["cotizacion", "orden_compra", "guia_remision"]
    
    # Crear la carpeta principal si no existe
    if not os.path.exists(carpeta_principal):
        os.makedirs(carpeta_principal)
    
    # Crear las subcarpetas si no existen
    for carpeta in carpetas_sub:
        ruta_carpeta = os.path.join(carpeta_principal, carpeta)
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)

# Crear las carpetas al inicio
crear_carpetas_adjuntar()

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
    #Ajusta el texto para que no exceda la longitud máxima y agrega '...' al final si es necesario.
    if len(texto) > max_length:
        return texto[:max_length - 3] + '...'
    return texto

def adjuntar_archivo(label, tipo_doc):
    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    if archivo:
        nombre_archivo = os.path.basename(archivo)
        texto_ajustado = ajustar_texto(nombre_archivo)
        label.config(text=texto_ajustado)

        # Determinar la subcarpeta según el tipo de documento
        subcarpeta = tipo_doc
        carpeta_destino = os.path.join("documentos_adjuntar", subcarpeta)

        # Copiar el archivo seleccionado a la carpeta correspondiente
        destino = os.path.join(carpeta_destino, nombre_archivo)
        shutil.copy(archivo, destino)  # Copia el archivo al destino
        return destino  # Devuelve la nueva ruta del archivo copiado
    return None

def confirmar_cancelacion(new_reg):
    # Verificar si los campos están vacíos
    campos_vacios = not input_coti.get().strip() and not input_nom.get().strip() and not input_tipodoc.get().strip() and not input_desc.get().strip() and not input_temp.get().strip() and not input_costo.get().strip()

    # Si los campos están vacíos, omitir la advertencia y cerrar directamente
    if campos_vacios:
        new_reg.destroy()   # Cierra la ventana de registro
        root.deiconify()    # Muestra nuevamente la ventana principal
    else:
        # Mostrar mensaje de advertencia si hay datos ingresados
        respuesta = messagebox.askquestion("Confirmación", "¿Desea cancelar el registro?")
        if respuesta == 'yes':
            new_reg.destroy()   # Cierra la ventana de registro
            root.deiconify()    # Muestra nuevamente la ventana principal


def placeholder_search(event):
    if search_entry.get() == "":
        search_entry.insert(0, "Buscar...")
        search_entry.config(fg='grey')

def clear_placeholder(event):
    if search_entry.get() == "Buscar...":
        search_entry.delete(0, tk.END)
        search_entry.config(fg='black')

def actualizar_simbolo_costo(event):
    moneda_seleccionada = cbo_costo_type.get()
    if moneda_seleccionada == "PEN":
        label_costo.config(text="S/")
    elif moneda_seleccionada == "USD":
        label_costo.config(text="$")

def vent_registro():
    
    global input_coti, input_nom, input_tipodoc, input_desc, input_temp, input_costo, date_entry, cbo_cancelado, input_cm
    global archivo_coti, archivo_oc, archivo_gr, cbo_doc_type, cbo_costo_type, label_costo
    
    # Ocultar la ventana principal
    root.withdraw()
    
    # Inicialización de variables de archivos
    archivo_coti = None
    archivo_oc = None
    archivo_gr = None
    
    # Ventana registro
    new_reg = tk.Toplevel(root)
    new_reg.title("Registro de Cotizaciones")
    new_reg.geometry("624x600")
    new_reg.resizable(False, False)
    new_reg.configure(bg="#373737")
    new_reg.protocol("WM_DELETE_WINDOW", cerrar_programa)

    # Crear un Canvas en la ventana de registro
    canvas_reg = tk.Canvas(new_reg, width=624, height=600, bg="#373737", highlightthickness=0)
    canvas_reg.pack()

    # Nuevo registro
    canvas_reg.create_text(105, 8, text="Registro de Cotización", anchor="nw", font=("Raleway", 30, "bold"), fill="White")
    
    # Cuadro 1
    create_rounded_rectangle(canvas_reg, 10, 80, 307, 550, radius=10, fill="#959595", outline="#959595")

    # Cuadro 2
    create_rounded_rectangle(canvas_reg, 317, 80, 614, 550, radius=10, fill="#959595", outline="#959595")

    # coti--
    canvas_reg.create_text(20, 92, text="N° de Cotización", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_reg, 20, 110, 297, 140, radius=10, fill="white", outline="#959595")

    input_coti = tk.Entry(new_reg, font=("Arial", 11), bd=0) #Entry
    input_coti.place(x=25, y=115, width=267, height=20)
    
    # nombre--
    canvas_reg.create_text(20, 156, text="Cliente", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_reg, 20, 174, 297, 204, radius=10, fill="white", outline="#959595")
    
    input_nom = tk.Entry(new_reg, font=("Arial", 11), bd=0) #Entry
    input_nom.place(x=25, y=179, width=267, height=20)
    
    # Tipo de documento
    canvas_reg.create_text(20, 220, text="Tipo de Documento", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_reg, 98, 238, 297, 268, radius=10, fill="white", outline="#959595")
                                        #----238
    input_tipodoc = tk.Entry(new_reg, font=("Arial", 11), bd=0) #Entry
    input_tipodoc.place(x=103, y=243, width=189, height=20)
    
    cbo_doc_type = ttk.Combobox(new_reg, values=["DNI", "RUC"], state="readonly", font=("Raleway", 10))
    cbo_doc_type.place(x=20, y=238, width=68, height=31)
    cbo_doc_type.current(0)
    
    # descripcion--
    canvas_reg.create_text(20, 284, text="Descripción", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_reg, 20, 302, 297, 332, radius=10, fill="white", outline="#959595")
    
    input_desc = tk.Entry(new_reg, font=("Arial", 11), bd=0)
    input_desc.place(x=25, y=307, width=267, height=20)
    
    # tiempo de ejecucion
    canvas_reg.create_text(20, 344, text="Tiempo de Ejecución", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_reg, 20, 362, 297, 392, radius=10, fill="white", outline="#959595")
    
    input_temp = tk.Entry(new_reg, font=("Arial", 11), bd=0) #Entry
    input_temp.place(x=25, y=367, width=267, height=20)
    
    # costo
    canvas_reg.create_text(20, 408, text="Costo Estimado", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_reg, 98, 426, 297, 456, radius=10, fill="white", outline="#959595")
    
    label_costo = tk.Label(new_reg, text="S/", font=("Raleway", 11), bg="white")
    label_costo.place(x=105, y=427)

    input_costo = tk.Entry(new_reg, font=("Arial", 11), bd=0) #Entry
    input_costo.place(x=133, y=432, width=158, height=20)
                    #   50     431
    cbo_costo_type = ttk.Combobox(new_reg, values=["PEN", "USD"], state="readonly", font=("Raleway", 10))
    cbo_costo_type.place(x=20, y=426, width=68, height=31)
    cbo_costo_type.current(0)
    
    cbo_costo_type.bind("<<ComboboxSelected>>", actualizar_simbolo_costo)
    
    # fecha de coti
    canvas_reg.create_text(20, 472, text="Fecha de Cotización", anchor="nw", font=("Raleway", 10), fill="black")
    
    date_entry = DateEntry(new_reg, font=("Raleway", 11),state="readonly" , width=17, background='darkblue', foreground='white', borderwidth=2)
    date_entry.place(x=20, y=491, width=278, height=30)
    
        # DOCUMENTOS A ADJUNTAR
        
            # Cotizacion
    canvas_reg.create_text(327, 92, text="Cotización", anchor="nw", font=("Raleway", 10), fill="black")
    
    button_coti = tk.Button(new_reg, text="Seleccionar archivo", command=lambda: adjuntar_archivo(label_coti, "cotizacion"))
    button_coti.place(x=327, y=111, height=29)

    # Etiqueta para mostrar el nombre del archivo seleccionado
    global label_coti
    label_coti = tk.Label(new_reg, text="Ningún archivo seleccio...", font=("Raleway", 9), bg="#373737", fg="white")
    label_coti.place(x=450, y=111, width=155, height=29)
    
    
            # Orden de compra
    canvas_reg.create_text(327, 156, text="Orden de Compra", anchor="nw", font=("Raleway", 10), fill="black")
    
    button_oc = tk.Button(new_reg, text="Seleccionar archivo", command=lambda: adjuntar_archivo(label_oc, "orden_compra"))
    button_oc.place(x=327, y=175, height=29)
    
    global label_oc
    label_oc = tk.Label(new_reg, text="Ningún archivo seleccio...", font=("Raleway", 9), bg="#373737", fg="white")
    label_oc.place(x=450, y=175, width=155, height=29)
    
    
            # Guía de remisión
    canvas_reg.create_text(327, 220, text="Guía de Remisión", anchor="nw", font=("Raleway", 10), fill="black")
    
    button_gr = tk.Button(new_reg, text="Seleccionar archivo", command=lambda: adjuntar_archivo(label_gr, "guia_remision"))
    button_gr.place(x=327, y=239, height=29)
    
    global label_gr
    label_gr = tk.Label(new_reg, text="Ningún archivo seleccio...", font=("Raleway", 9), bg="#373737", fg="white")
    label_gr.place(x=450, y=239, width=155, height=29)
    
    
    # CBO CANCELADO
    canvas_reg.create_text(327, 284, text="Cancelado", anchor="nw", font=("Raleway", 10), fill="black")
    
    cbo_cancelado = ttk.Combobox(new_reg, values=["Seleccione una opción", "Si", "No"], state="readonly", font=("Raleway", 10))
    cbo_cancelado.place(x=326, y=302, width=279, height=30)
    cbo_cancelado.current(0)
    
    # COMENTARIOS
    canvas_reg.create_text(327, 344, text="Comentarios (opcional)", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_reg, 326, 362, 604, 520, radius=10, fill="white", outline="#959595")
    
    input_cm = tk.Text(new_reg, font=("Arial", 11), bd=0, wrap="word") #Entry
    input_cm.place(x=331, y=363, width=271, height=157)
    

    # botones
    button_save = tk.Button(new_reg, text="Guardar", width=13, height=1, font=("Raleway", 9))
    button_save.place(x=207, y=560)
    
    button_cancel = tk.Button(new_reg, text="Cancelar", width=13, height=1, font=("Raleway", 9), command=lambda: confirmar_cancelacion(new_reg))
    button_cancel.place(x=317, y=560)


def crear_coti():
    
    global input_gcoti, input_gfecha, input_gpersona, input_gempresa, input_gservicio, input_gejecucion, input_gpago 
    global cbo_igv, cbo_moneda, input_gdesc, input_gmateriales, input_gunidad, cbo_unidad, input_gpunit, input_gcuenta
    global cbo_cuenta, input_gbanco, tree_materiales
    
    # Ocultar la ventana principal
    root.withdraw()
    
    # Ventana registro
    crear_coti = tk.Toplevel(root)
    crear_coti.title("Crear Cotización")
    crear_coti.geometry("605x756")
    crear_coti.resizable(False, False)
    crear_coti.configure(bg="#373737")
    crear_coti.protocol("WM_DELETE_WINDOW", cerrar_programa)
    
    # Crear un Canvas en la ventana de registro
    canvas_coti = tk.Canvas(crear_coti, width=605, height=772, bg="#373737", highlightthickness=0)
    canvas_coti.pack()
    
    # Nuevo registro
    canvas_coti.create_text(125, 0, text="Generar Cotización", anchor="nw", font=("Raleway", 30, "bold"), fill="White")
    
    # Cuadro arriba
    create_rounded_rectangle(canvas_coti, 10, 66, 595, 262, radius=10, fill="#959595", outline="#959595")

    # Cuadro centro
    create_rounded_rectangle(canvas_coti, 10, 272, 595, 468, radius=10, fill="#959595", outline="#959595")
    
    # Cuadro abajo
    create_rounded_rectangle(canvas_coti, 10, 518, 595, 706, radius=10, fill="#959595", outline="#959595")
                                            #-523

    # Definimos las columnas para la tabla de materiales
    columns = ("descripcion", "material", "unidad", "precio_unit")
    
    # Creamos la tabla
    tree_materiales = ttk.Treeview(crear_coti, columns=columns, show="headings")
    tree_materiales.place(x=10, y=518, width=586, height=189)
                                        #----586
    
    # Configuramos los encabezados de cada columna
    tree_materiales.heading("descripcion", text="Descripción")
    tree_materiales.heading("material", text="Material")
    tree_materiales.heading("unidad", text="Unidad(es)")
    tree_materiales.heading("precio_unit", text="Precio Unit.")
    
    # Configuramos el ancho de cada columna
    tree_materiales.column("descripcion", anchor="center", width=200)
    tree_materiales.column("material", anchor="center", width=120)
    tree_materiales.column("unidad", anchor="center", width=50)
    tree_materiales.column("precio_unit", anchor="center", width=100)
    

    # n° de cotizacion
    canvas_coti.create_text(20, 76, text="N° de Cotización", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 94, 200, 124, radius=10, fill="white", outline="#959595")

    input_gcoti = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gcoti.place(x=25, y=99, width=170, height=20)
    
    # fecha
    canvas_coti.create_text(210, 76, text="Fecha", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 210, 94, 405, 124, radius=10, fill="white", outline="#959595")

    input_gfecha = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gfecha.place(x=215, y=99, width=185, height=20)
    
    # persona
    canvas_coti.create_text(415, 76, text="Persona de Contacto", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 415, 94, 585, 124, radius=10, fill="white", outline="#959595")

    input_gpersona = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gpersona.place(x=420, y=99, width=160, height=20)
    
    # empresa
    canvas_coti.create_text(20, 140, text="Empresa", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 158, 200, 188, radius=10, fill="white", outline="#959595")

    input_gempresa = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gempresa.place(x=25, y=163, width=170, height=20)
    
    # servicio
    canvas_coti.create_text(210, 140, text="Servicio", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 210, 158, 585, 188, radius=10, fill="white", outline="#959595")

    input_gservicio = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gservicio.place(x=215, y=163, width=365, height=20)
    
    # tiempo de ejecucion
    canvas_coti.create_text(20, 204, text="Tiempo de Ejecución", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 222, 225, 252, radius=10, fill="white", outline="#959595")

    input_gejecucion = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gejecucion.place(x=25, y=227, width=195, height=20)
    
    # forma de pago
    canvas_coti.create_text(235, 204, text="Forma de Pago", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 235, 222, 355, 252, radius=10, fill="white", outline="#959595")

    input_gpago = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gpago.place(x=240, y=227, width=110, height=20)
    
    # igv
    canvas_coti.create_text(365, 204, text="IGV", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_igv = ttk.Combobox(canvas_coti, values=["SI", "NO"], state="readonly", font=("Raleway", 10))
    cbo_igv.place(x=365, y=222, width=70, height=31)
    cbo_igv.current(0)
    
    # tipo de moneda
    canvas_coti.create_text(445, 204, text="Tipo de Moneda", anchor="nw", font=("Raleway", 10), fill="black")
    
    cbo_moneda = ttk.Combobox(canvas_coti, values=["PEN", "USD"], state="readonly", font=("Raleway", 10))
    cbo_moneda.place(x=445, y=222, width=140, height=31)
    cbo_moneda.current(0)
    
    # descripcion
    canvas_coti.create_text(20, 282, text="Descripción", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 300, 585, 330, radius=10, fill="white", outline="#959595")

    input_gdesc = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gdesc.place(x=25, y=305, width=555, height=20)
    
    # materiales
    canvas_coti.create_text(20, 346, text="Materiales", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 364, 290, 394, radius=10, fill="white", outline="#959595")

    input_gmateriales = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gmateriales.place(x=25, y=369, width=260, height=20)
    
    # unidades
    canvas_coti.create_text(300, 346, text="Unidad(es)", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 300, 364, 350, 394, radius=10, fill="white", outline="#959595")

    input_gunidad = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gunidad.place(x=305, y=369, width=40, height=20)
    
    cbo_unidad = ttk.Combobox(canvas_coti, values=["PIEZA", "JUEGO", "UNIDAD"], state="readonly", font=("Raleway", 10))
    cbo_unidad.place(x=360, y=364, width=92, height=31)
    cbo_unidad.current(0)
    
    # precio unit
    canvas_coti.create_text(462, 346, text="Precio Unit.", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 462, 364, 585, 394, radius=10, fill="white", outline="#959595")
    
    input_gpunit = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gpunit.place(x=467, y=369, width=113, height=20)
    
    # nro de cuenta
    canvas_coti.create_text(20, 410, text="N° de Cuenta", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 428, 190, 458, radius=10, fill="white", outline="#959595")
    
    input_gcuenta = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gcuenta.place(x=25, y=433, width=160, height=20)
    
    cbo_cuenta = ttk.Combobox(canvas_coti, values=["SOLES", "DÓLARES"], state="readonly", font=("Raleway", 10))
    cbo_cuenta.place(x=200, y=428, width=90, height=31)
    cbo_cuenta.current(0)
    
    # tipo de banco
    canvas_coti.create_text(300, 410, text="Banco", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 300, 428, 585, 458, radius=10, fill="white", outline="#959595")
    
    input_gbanco = tk.Entry(canvas_coti, font=("Arial", 11), bd=0)
    input_gbanco.place(x=305, y=433, width=275, height=20)
    
    # botones
    button_am = tk.Button(canvas_coti, text="Agregar Material/es", width=27, height=1, font=("Raleway", 9))
    button_am.place(x=10, y=478)
    
    button_lc = tk.Button(canvas_coti, text="Limpiar Campos", width=27, height=1, font=("Raleway", 9))
    button_lc.place(x=220, y=478)
    
    button_gc = tk.Button(canvas_coti, text="Generar Cotización", width=27, height=1, font=("Raleway", 9))
    button_gc.place(x=10, y=717)
    
    button_gcancel = tk.Button(canvas_coti, text="Cancelar", width=27, height=1, font=("Raleway", 9))
    button_gcancel.place(x=220, y=717)


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
create_rounded_rectangle(canvas, 10, 10, 300, 690, radius=10, fill="#959595", outline="#959595")

# Cuadro base 690
create_rounded_rectangle(canvas, 312, 88, 1289, 651, radius=10, fill="#959595", outline="#959595")


canvas.create_text(22, 24, text="Opciones", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

canvas.create_text(435, 23, text="Soluciones Plasticas Metálicas SAC", anchor="nw", font=("Raleway", 20, "bold"), fill="White")
               #---435, 29


# Botones base 1210
button_sig = tk.Button(root, text="Siguiente", width=10, height=1, font=("Raleway", 9))
button_sig.place(x=1210, y=661)

button_ant = tk.Button(root, text="Anterior", width=10, height=1, font=("Raleway", 9))
button_ant.place(x=1118, y=661)


# Botones opcion
button_regcoti = tk.Button(root, text="Registrar Nueva Cotización", width=37, height=1, font=("Raleway", 9), command=vent_registro)
button_regcoti.place(x=22, y=88)

button_gencoti = tk.Button(root, text="Crear Cotización", width=37, height=1, font=("Raleway", 9), command=crear_coti)
button_gencoti.place(x=22, y=134)

button_verdet = tk.Button(root, text="Ver detalles", width=37, height=1, font=("Raleway", 9))
button_verdet.place(x=22, y=180)

button_actreg = tk.Button(root, text="Actualizar Registros", width=37, height=1, font=("Raleway", 9))
button_actreg.place(x=22, y=226)

button_busav = tk.Button(root, text="Búsqueda Avanzada", width=37, height=1, font=("Raleway", 9))
button_busav.place(x=22, y=272)

button_allcotireg = tk.Button(root, text="Ver todas las cotizaciones registradas", width=37, height=1, font=("Raleway", 9))
button_allcotireg.place(x=22, y=318)

button_exit = tk.Button(root, text="Salir", width=37, height=1, font=("Raleway", 9), command=root.destroy)
button_exit.place(x=22, y=364)


# Buscador
search_canvas = tk.Canvas(root, width=280, height=30, bg="#373737", highlightthickness=0)
search_canvas.place(x=1005, y=29)

create_rounded_rectangle(search_canvas, 0, 0, 280, 30, radius=10, fill="white", outline="gray")

search_entry = tk.Entry(search_canvas, font=("Raleway", 11), width=30, bd=0, relief="flat", fg='grey')
search_entry.insert(0, "Buscar...")  # Insertar texto de placeholder
search_entry.bind("<FocusIn>", clear_placeholder)  # Limpiar cuando el usuario hace clic
search_entry.bind("<FocusOut>", placeholder_search)  # Volver a mostrar si está vacío
search_entry.place(x=6, y=4)


# Tabla del cuadro base
tree = ttk.Treeview(root, columns=("cotizacion", "nombre", "ruc", "descripcion", "fecha", "cancelado"), show="headings")
tree.place(x=312, y=88, width=978, height=564)

# Configurar las columnas
tree.heading("cotizacion", text="N° de Cotización")
tree.heading("nombre", text="Empresa")
tree.heading("ruc", text="RUC/DNI")
tree.heading("descripcion", text="Descripción")
tree.heading("fecha", text="Fecha de Cotización")
tree.heading("cancelado", text="Cancelado")

# Ajustar el tamaño de las columnas
tree.column("cotizacion", anchor="center", width=70)
tree.column("nombre", anchor="center", width=100)
tree.column("ruc", anchor="center", width=150)
tree.column("descripcion", anchor="center", width=280)
tree.column("fecha", anchor="center", width=100)
tree.column("cancelado", anchor="center", width=50)

# Ejecutar la interfaz
root.mainloop()
