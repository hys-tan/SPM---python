import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from tkcalendar import DateEntry
import os
import shutil
import sqlite3
from PIL import Image, ImageTk
from tkinter import Toplevel, Label, Button, PhotoImage

id_persona_contacto = 1
id_area_trabajo = 1
id_direccion = 1

# Crear o conectar a la base de datos
conn = sqlite3.connect('clientes.db')
c = conn.cursor()

# Crear tabla Clientes
c.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        persona_contacto TEXT,
        area_trabajo TEXT,
        razon_social TEXT,
        ruc TEXT,
        direccion TEXT
    )
''')
conn.commit()







def centrar_ventana(ventana):
    ventana.update_idletasks()
    width = ventana.winfo_width()
    height = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana.winfo_screenheight() // 2) - (height // 2)
    ventana.geometry(f"{width}x{height}+{x}+{y}")


# Función para crear las carpetas si no existen
def crear_carpetas_adjuntar():
    # Carpeta principal
    carpeta_principal = "documentos_adjuntar"
    
    # Subcarpetas para cada tipo de documento
    carpetas_sub = ["cotizacion", "orden_compra", "guia_remision", "acta_conformidad", "informe_tecnico", "doc_planos", "doc_factura"]
    
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



def confirmar_cancelacion(reg_cliente):
    # Verificar si los campos están vacíos
    campos_vacios = not reg_persona.get().strip() and not reg_ar_tb.get().strip() and not reg_rs_cli.get().strip() and not reg_ruc_cli.get().strip() and not reg_direx.get().strip()

    # Si los campos están vacíos, omitir la advertencia y cerrar directamente
    if campos_vacios:
        reg_cliente.destroy()   # Cierra la ventana de registro
        root.deiconify()    # Muestra nuevamente la ventana principal
    else:
        # Mostrar mensaje de advertencia si hay datos ingresados
        respuesta = messagebox.askquestion("Confirmación", "¿Desea cancelar el registro?")
        if respuesta == 'yes':
            reg_cliente.destroy()   # Cierra la ventana de registro
            root.deiconify()    # Muestra nuevamente la ventana principal


def placeholder_search(event):
    if search_entry.get() == "":
        search_entry.insert(0, "Buscar...")
        search_entry.config(fg='grey')

def clear_placeholder(event):
    if search_entry.get() == "Buscar...":
        search_entry.delete(0, tk.END)
        search_entry.config(fg='black')



def ventana_advertencia(mensaje, accion_confirmar):
    advertencia = Toplevel(root)
    advertencia.title("Advertencia")
    advertencia.geometry("380x112")
    advertencia.resizable(False, False)
    advertencia.configure(bg="#ffffff")

    # Cargar el ícono de advertencia y ajustarlo al tamaño de 32x32
    icono_advertencia = PhotoImage(file="icons/alert.png").subsample(2, 2)  # Ajustar tamaño
    Label(advertencia, image=icono_advertencia, bg="#ffffff").place(x=20, y=20)
    
    # Mensaje de advertencia en la posición especificada
    Label(advertencia, text=mensaje, bg="#ffffff", font=("Arial", 10)).place(x=77, y=27)
    
    # Botones de Sí y No en las coordenadas especificadas
    Button(advertencia, text="Sí", command=lambda: [accion_confirmar(), advertencia.destroy()], font=("Arial", 10)).place(x=85, y=72)
    Button(advertencia, text="No", command=advertencia.destroy, font=("Arial", 10)).place(x=195, y=72)

    advertencia.transient(root)  # La mantiene sobre la ventana principal
    advertencia.grab_set()  # Bloquea la interacción con otras ventanas hasta que esta se cierre
    advertencia.mainloop()


def ventana_confirmacion(mensaje, accion_confirmar):
    confirmacion = Toplevel()
    confirmacion.title("Confirmación")
    confirmacion.geometry("300x150")
    confirmacion.resizable(False, False)
    confirmacion.configure(bg="#ffffff")

    # Cargar el ícono de confirmación
    icono_confirmacion = PhotoImage(file="iconos/confirmacion.png")
    Label(confirmacion, image=icono_confirmacion, bg="#ffffff").pack(pady=10)
    
    # Mensaje de confirmación
    Label(confirmacion, text=mensaje, bg="#ffffff", font=("Arial", 10)).pack(pady=5)
    
    # Botones de Sí y No
    Button(confirmacion, text="Sí", command=lambda: [accion_confirmar(), confirmacion.destroy()], font=("Arial", 10)).pack(side="left", padx=20, pady=10)
    Button(confirmacion, text="No", command=confirmacion.destroy, font=("Arial", 10)).pack(side="right", padx=20, pady=10)
    
    confirmacion.transient()  # La mantiene sobre la ventana principal
    confirmacion.grab_set()  # Bloquea la interacción con otras ventanas hasta que esta se cierre
    confirmacion.mainloop()


def cerrar_programa():
    ventana_confirmacion("¿Está seguro de que desea salir?", root.quit)

# Ejemplo de función para eliminar una fila con confirmación
def eliminar_columna():
    # Aquí va la lógica para eliminar la fila seleccionada de la tabla
    print("Columna eliminada")  # Este print es solo un ejemplo
    ventana_advertencia("Columna eliminada")

# Función para advertencia de selección de fila para editar
def verificar_seleccion_editar(tabla, mensaje):
    selected_item = tabla.selection()
    if not selected_item:
        ventana_advertencia(mensaje)
        return None
    item = tabla.item(selected_item)
    return item









    

     
# ventana crear cot
def crear_cotiz(): 
    
    global input_gcoti, input_gfecha, input_gpersona, cbo_area, input_gempresa
    global input_gtitulo, input_gtiempo, input_gpago, cbo_igv, cbo_moneda, cbo_cuenta
    global input_gcuenta, input_gcuentabanc, input_gdesc, input_gmaterial, cbo_unidad
    global input_gunidad, input_gpreciou, input_gsubtot, input_gigv, input_gtotal, tree_materiales
    
    # Ocultar la ventana principal
    root.withdraw()
    
    # Ventana registro
    crear_coti = tk.Toplevel(root)
    crear_coti.title("Crear Cotización")
    crear_coti.geometry("700x714")
    crear_coti.resizable(False, False)
    crear_coti.configure(bg="#373737")
    
    centrar_ventana(crear_coti) # centrar ventana


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
    tree_materiales.place(x=10, y=435, width=681, height=152)
                                # 436                    151

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

    input_gcoti = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gcoti.place(x=25, y=99, width=140, height=20)

    # fecha
    canvas_coti.create_text(180, 76, text="Fecha", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 180, 94, 370, 124, radius=10, fill="white", outline="#959595")

    input_gfecha = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gfecha.place(x=185, y=99, width=180, height=20)

    # empresa
    canvas_coti.create_text(380, 76, text="Empresa", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 380, 94, 530, 124, radius=10, fill="white", outline="#959595")

    input_gpersona = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gpersona.place(x=385, y=99, width=140, height=20)

    # area
    canvas_coti.create_text(540, 76, text="Área", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_area = ttk.Combobox(crear_coti, values=["Escoja una Opción", "Ejemplo1"], state="readonly", font=("Raleway", 10))
    cbo_area.place(x=540, y=94, width=140, height=31)
    cbo_area.current(0)

    # persona
    canvas_coti.create_text(20, 134, text="Persona de Contacto", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 152, 200, 182, radius=10, fill="white", outline="#959595")

    input_gempresa = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gempresa.place(x=25, y=157, width=170, height=20)

    # titulo
    canvas_coti.create_text(210, 134, text="Título del Servicio", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 210, 152, 680, 182, radius=10, fill="white", outline="#959595")

    input_gtitulo = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gtitulo.place(x=215, y=157, width=460, height=20)

    # tiempo
    canvas_coti.create_text(20, 192, text="Tiempo de Ejecución", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 210, 290, 240, radius=10, fill="white", outline="#959595")

    input_gtiempo = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gtiempo.place(x=25, y=215, width=260, height=20)

    # tipo pago
    canvas_coti.create_text(300, 192, text="Forma de Pago", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 300, 210, 490, 240, radius=10, fill="white", outline="#959595")

    input_gpago = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gpago.place(x=305, y=215, width=180, height=20)

    # igv
    canvas_coti.create_text(500, 192, text="IGV", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_igv = ttk.Combobox(crear_coti, values=["SI", "NO"], state="readonly", font=("Raleway", 10))
    cbo_igv.place(x=500, y=210, width=50, height=31)
    cbo_igv.current(0)

    # moneda
    canvas_coti.create_text(560, 192, text="Tipo de Moneda", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_moneda = ttk.Combobox(crear_coti, values=["PEN", "USD"], state="readonly", font=("Raleway", 10))
    cbo_moneda.place(x=560, y=210, width=120, height=31)
    cbo_moneda.current(0)

    # cuenta banc
    canvas_coti.create_text(20, 250, text="Tipo de Cuenta", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_cuenta = ttk.Combobox(crear_coti, values=["Cuenta Soles", "Cuenta Dólares"], state="readonly", font=("Raleway", 10))
    cbo_cuenta.place(x=20, y=268, width=130, height=31)
    cbo_cuenta.current(0)

    # nro cuenta
    canvas_coti.create_text(160, 250, text="Nro de Cuenta", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 160, 268, 410, 298, radius=10, fill="white", outline="#959595")

    input_gcuenta = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gcuenta.place(x=165, y=273, width=240, height=20)

    # cuenta interbanc
    canvas_coti.create_text(420, 250, text="Cuenta Interbancaria", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 420, 268, 680, 298, radius=10, fill="white", outline="#959595")

    input_gcuentabanc = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gcuentabanc.place(x=425, y=273, width=250, height=20)


    # desc
    canvas_coti.create_text(20, 328, text="Descripción", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 346, 190, 376, radius=10, fill="white", outline="#959595")

    input_gdesc = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gdesc.place(x=25, y=351, width=160, height=20)

    # material
    canvas_coti.create_text(200, 328, text="Material(es)", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 200, 346, 370, 376, radius=10, fill="white", outline="#959595")

    input_gmaterial = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gmaterial.place(x=205, y=351, width=160, height=20)

    # unidades
    canvas_coti.create_text(380, 329, text="Unidad(es)", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_unidad = ttk.Combobox(crear_coti, values=["JUEGO", "PIEZA"], state="readonly", font=("Raleway", 10))
    cbo_unidad.place(x=380, y=347, width=100, height=31)
    cbo_unidad.current(0)

    create_rounded_rectangle(canvas_coti, 490, 346, 545, 376, radius=10, fill="white", outline="#959595")

    input_gunidad = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gunidad.place(x=495, y=351, width=45, height=20)

    # precio unit
    canvas_coti.create_text(555, 328, text="Precio Unitario", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 555, 346, 680, 376, radius=10, fill="white", outline="#959595")

    input_gpreciou = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gpreciou.place(x=560, y=351, width=115, height=20)


    # subtotal
    canvas_coti.create_text(20, 606, text="Sub Total", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 20, 624, 130, 654, radius=10, fill="white", outline="#959595")

    input_gsubtot = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gsubtot.place(x=25, y=629, width=100, height=20)

    # +igv
    canvas_coti.create_text(140, 606, text="IGV", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 140, 624, 250, 654, radius=10, fill="white", outline="#959595")

    input_gigv = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gigv.place(x=145, y=629, width=100, height=20)

    # total
    canvas_coti.create_text(260, 606, text="Total", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_coti, 260, 624, 370, 654, radius=10, fill="white", outline="#959595")

    input_gtotal = tk.Entry(crear_coti, font=("Arial", 11), bd=0)
    input_gtotal.place(x=265, y=629, width=100, height=20)


    # Botones opcion
    btn_ag = tk.Button(crear_coti, text="Agregar", width=20, height=1, font=("Raleway", 9))
    btn_ag.place(x=10, y=396)
    
    btn_ed = tk.Button(crear_coti, text="Editar", width=20, height=1, font=("Raleway", 9), command=abrir_editar_material)
    btn_ed.place(x=169, y=396)
    
    btn_del = tk.Button(crear_coti, text="Eliminar", width=20, height=1, font=("Raleway", 9))
    btn_del.place(x=328, y=396)
        
    btn_canc = tk.Button(crear_coti, text="Cancelar", width=20, height=1, font=("Raleway", 9))
    btn_canc.place(x=10, y=675)

    btn_gen = tk.Button(crear_coti, text="Generar", width=20, height=1, font=("Raleway", 9))
    btn_gen.place(x=169, y=675)


def abrir_editar_material():
    
    global inpt_ed_desc, inpt_ed_mat, cbo_ed_unidad, inpt_ed_unidad, inpt_ed_precio, inpt_ed_total
    
    # Crear una nueva ventana para editar materiales
    editar_material = tk.Toplevel(root)
    editar_material.title("Editar Material")
    editar_material.geometry("600x186")
    editar_material.resizable(False, False)
    editar_material.configure(bg="#373737")
    
    centrar_ventana(editar_material)
    
    
    # Evitar que la ventana principal se edite mientras la subventana está activa
    editar_material.grab_set()  # Bloquea la ventana principal hasta que la subventana se cierre

    # Prevenir el cierre de la ventana principal con el botón de cerrar (X)
    editar_material.protocol("WM_DELETE_WINDOW", lambda: None)  # Deshabilita el botón cerrar de la subventana si no quieres que se cierre accidentalmente
    

    # Crear el canvas para la ventana de editar
    canvas_editar = tk.Canvas(editar_material, width=600, height=186, bg="#373737", highlightthickness=0)
    canvas_editar.pack()
    
    create_rounded_rectangle(canvas_editar, 10, 10, 590, 135, radius=10, fill="#959595", outline="#959595")


    # desc
    canvas_editar.create_text(20, 20, text="Descripción", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_editar, 20, 38, 300, 68, radius=10, fill="white", outline="#959595")

    inpt_ed_desc = tk.Entry(editar_material, font=("Arial", 11), bd=0)
    inpt_ed_desc.place(x=25, y=43, width=270, height=20)

    # material
    canvas_editar.create_text(310, 20, text="Material(es)", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_editar, 310, 38, 580, 68, radius=10, fill="white", outline="#959595")

    inpt_ed_mat = tk.Entry(editar_material, font=("Arial", 11), bd=0)
    inpt_ed_mat.place(x=315, y=43, width=260, height=20)

    # unidades
    canvas_editar.create_text(20, 78, text="Unidad(es)", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_ed_unidad = ttk.Combobox(editar_material, values=["JUEGO", "PIEZA"], state="readonly", font=("Raleway", 10))
    cbo_ed_unidad.place(x=20, y=96, width=90, height=31)
    cbo_ed_unidad.current(0)

    create_rounded_rectangle(canvas_editar, 120, 96, 190, 126, radius=10, fill="white", outline="#959595")

    inpt_ed_unidad = tk.Entry(editar_material, font=("Arial", 11), bd=0)
    inpt_ed_unidad.place(x=125, y=101, width=60, height=20)

    # precio unit
    canvas_editar.create_text(200, 78, text="Precio Unitario", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_editar, 200, 96, 330, 126, radius=10, fill="white", outline="#959595")

    inpt_ed_precio = tk.Entry(editar_material, font=("Arial", 11), bd=0)
    inpt_ed_precio.place(x=205, y=101, width=120, height=20)
    
    # subtotal
    canvas_editar.create_text(340, 78, text="Sub Total", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_editar, 340, 96, 470, 126, radius=10, fill="white", outline="#959595")

    inpt_ed_total = tk.Entry(editar_material, font=("Arial", 11), bd=0)
    inpt_ed_total.place(x=345, y=101, width=120, height=20)
    
    #btn editar material
    btn_ed_canc = tk.Button(editar_material, text="Cancelar", width=15, height=1, font=("Raleway", 9), command=editar_material.destroy)
    btn_ed_canc.place(x=10, y=146)

    btn_ed_save = tk.Button(editar_material, text="Guardar", width=15, height=1, font=("Raleway", 9))
    btn_ed_save.place(x=134, y=146)


def registro_clientes():
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def eliminar_fila(tabla, campo_actual):
        # Seleccionar la fila en la tabla
        selected_item = tabla.selection()
        if not selected_item:
            mostrar_advertencia()  # Muestra la advertencia usando messagebox
            return

        # Obtener el valor actual
        item = tabla.item(selected_item)
        valor_actual = item['values'][1]

        # Confirmación de eliminación usando messagebox
        respuesta = messagebox.askyesno("Confirmación", f"¿Desea eliminar la columna '{valor_actual}'?")
        if respuesta:  # Si el usuario selecciona "Sí"
            # Eliminar la fila seleccionada de la tabla
            tabla.delete(selected_item)
            
            # Confirmación de eliminación exitosa
            messagebox.showinfo("Confirmación", "Columna eliminada")  # Modal de confirmación

    def mostrar_advertencia():
        # Esta función bloqueará la interfaz hasta que el usuario cierre la advertencia
        messagebox.showwarning("Advertencia", "Seleccione una fila para editar.")
    

    
    
    
    # Ocultar la ventana principal
    root.withdraw()
    
    global reg_persona, reg_ar_tb, reg_rs_cli, reg_ruc_cli, reg_direx
    global tabla_per_cont, tabla_ar_trab, tabla_direx
    
    reg_cliente = tk.Toplevel(root)
    reg_cliente.title("Registro de Clientes")
    reg_cliente.geometry("710x562")
    reg_cliente.resizable(False, False)
    reg_cliente.configure(bg="#373737")
    
    centrar_ventana(reg_cliente)

    
    # BD ------------------------------------------------

    def agregar_persona_contacto():
        global id_persona_contacto
        # Obtener el texto ingresado en el campo de persona de contacto
        persona_contacto = reg_persona.get()
        
        # Insertar el texto en la tabla correspondiente sin guardarlo en la BD
        if persona_contacto:
            tabla_per_cont.insert("", tk.END, values=(id_persona_contacto, persona_contacto))
            reg_persona.delete(0, tk.END)  # Limpiar el campo después de agregar
            id_persona_contacto += 1  # Incrementa el contador

    def agregar_area_trabajo():
        global id_area_trabajo
        area_trabajo = reg_ar_tb.get()
        
        if area_trabajo:
            tabla_ar_trab.insert("", tk.END, values=(id_area_trabajo, area_trabajo))
            reg_ar_tb.delete(0, tk.END)
            id_area_trabajo += 1

    def agregar_direccion():
        global id_direccion
        direccion = reg_direx.get()
        
        if direccion:
            tabla_direx.insert("", tk.END, values=(id_direccion, direccion))
            reg_direx.delete(0, tk.END)
            id_direccion += 1


    def guardar_cliente():
        # Obtener datos de los campos de entrada
        persona_contacto = reg_persona.get()
        area_trabajo = reg_ar_tb.get()
        razon_social = reg_rs_cli.get()
        ruc = reg_ruc_cli.get()
        direccion = reg_direx.get()

        # Insertar datos en la base de datos
        c.execute('''
            INSERT INTO Clientes (persona_contacto, area_trabajo, razon_social, ruc, direccion)
            VALUES (?, ?, ?, ?, ?)
        ''', (persona_contacto, area_trabajo, razon_social, ruc, direccion))
        conn.commit()

        # Limpiar campos después de guardar
        reg_persona.delete(0, tk.END)
        reg_ar_tb.delete(0, tk.END)
        reg_rs_cli.delete(0, tk.END)
        reg_ruc_cli.delete(0, tk.END)
        reg_direx.delete(0, tk.END)

        messagebox.showinfo("Éxito", "Cliente registrado exitosamente")

    # BD ------------------------------------------------


    # Asignar la acción para la 'X' (cerrar) y validar campos llenos o vacíos
    reg_cliente.protocol("WM_DELETE_WINDOW", lambda: confirmar_cancelacion(reg_cliente))
    
    # Crear el canvas para la ventana de reg clientes
    canvas_reg_cliente = tk.Canvas(reg_cliente, width=710, height=562, bg="#373737", highlightthickness=0)
    canvas_reg_cliente.pack()
    
    canvas_reg_cliente.create_text(178, 0, text="Registro de Clientes", anchor="nw", font=("Raleway", 30, "bold"), fill="White")
    
    # cuadro 1 left
    create_rounded_rectangle(canvas_reg_cliente, 10, 66, 350, 174, radius=10, fill="#959595", outline="#959595")
    
        # persona contacto
    canvas_reg_cliente.create_text(20, 76, text="Persona de Contacto", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_reg_cliente, 20, 94, 340, 124, radius=10, fill="white", outline="#959595")

    reg_persona = tk.Entry(reg_cliente, font=("Arial", 11), bd=0)
    reg_persona.place(x=25, y=99, width=310, height=20)
    
        # botones
    btn_ag_persona = tk.Button(reg_cliente, text="Agregar", width=13, height=1, font=("Raleway", 9), command=agregar_persona_contacto)
    btn_ag_persona.place(x=20, y=134)
    
    btn_ed_persona = tk.Button(reg_cliente, text="Editar", width=13, height=1, font=("Raleway", 9), command=edit_persona_cont)
    btn_ed_persona.place(x=130, y=134)
    
    btn_del_persona = tk.Button(reg_cliente, text="Eliminar", width=13, height=1, font=("Raleway", 9))
    btn_del_persona.config(command=lambda: eliminar_fila(tabla_per_cont, "persona_contacto_actual"))
    btn_del_persona.place(x=240, y=134)
    
        # tabla
    create_rounded_rectangle(canvas_reg_cliente, 10, 184, 350, 304, radius=10, fill="#959595", outline="#959595")
    
    tabla_per_cont = ttk.Treeview(reg_cliente, columns=("id_per","per_cont"), show="headings")
    tabla_per_cont.place(x=10, y=184, width=341, height=121)

    # Configurar las columnas
    tabla_per_cont.heading("id_per", text="ID")
    tabla_per_cont.heading("per_cont", text="Persona de Contacto")


    # Ajustar el tamaño de las columnas
    tabla_per_cont.column("id_per", anchor="center", width=41)
    tabla_per_cont.column("per_cont", anchor="center", width=298)
    
    
    
    # cuadro 2 left
    create_rounded_rectangle(canvas_reg_cliente, 10, 314, 350, 422, radius=10, fill="#959595", outline="#959595")
    
        # area trabajo
    canvas_reg_cliente.create_text(20, 324, text="Área de Trabajo", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_reg_cliente, 20, 342, 340, 372, radius=10, fill="white", outline="#959595")

    reg_ar_tb = tk.Entry(reg_cliente, font=("Arial", 11), bd=0)
    reg_ar_tb.place(x=25, y=347, width=310, height=20)
    
        # botones
    btn_ag_trabajo = tk.Button(reg_cliente, text="Agregar", width=13, height=1, font=("Raleway", 9), command=agregar_area_trabajo)
    btn_ag_trabajo.place(x=20, y=382)
    
    btn_ed_trabajo = tk.Button(reg_cliente, text="Editar", width=13, height=1, font=("Raleway", 9), command=edit_area_trabajo)
    btn_ed_trabajo.place(x=130, y=382)
    
    btn_del_trabajo = tk.Button(reg_cliente, text="Eliminar", width=13, height=1, font=("Raleway", 9))
    btn_del_trabajo.config(command=lambda: eliminar_fila(tabla_ar_trab, "area_trabajo_actual"))
    btn_del_trabajo.place(x=240, y=382)
    
        # tabla
    create_rounded_rectangle(canvas_reg_cliente, 10, 432, 350, 552, radius=10, fill="#959595", outline="#959595")
    
    tabla_ar_trab = ttk.Treeview(reg_cliente, columns=("id_trab", "trab_ar"), show="headings")
    tabla_ar_trab.place(x=10, y=432, width=341, height=121)

    # Configurar las columnas
    tabla_ar_trab.heading("id_trab", text="ID")
    tabla_ar_trab.heading("trab_ar", text="Área de Trabajo")

    # Ajustar el tamaño de las columnas
    tabla_ar_trab.column("id_trab", anchor="center", width=41)
    tabla_ar_trab.column("trab_ar", anchor="center", width=298)
    
    

    # cuadro 3 right
    create_rounded_rectangle(canvas_reg_cliente, 360, 66, 700, 192, radius=10, fill="#959595", outline="#959595")
    
        # razon social
    canvas_reg_cliente.create_text(370, 76, text="Razón Social/Cliente", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_reg_cliente, 370, 94, 690, 124, radius=10, fill="white", outline="#959595")

    reg_rs_cli = tk.Entry(reg_cliente, font=("Arial", 11), bd=0)
    reg_rs_cli.place(x=375, y=99, width=310, height=20)
    
        # ruc
    canvas_reg_cliente.create_text(370, 134, text="RUC", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_reg_cliente, 370, 152, 690, 182, radius=10, fill="white", outline="#959595")

    reg_ruc_cli = tk.Entry(reg_cliente, font=("Arial", 11), bd=0)
    reg_ruc_cli.place(x=375, y=157, width=310, height=20)
    
    
    # cuadro 4 right
    create_rounded_rectangle(canvas_reg_cliente, 360, 202, 700, 310, radius=10, fill="#959595", outline="#959595")
    
        # direccion
    canvas_reg_cliente.create_text(370, 212, text="Dirección", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_reg_cliente, 370, 230, 690, 260, radius=10, fill="white", outline="#959595")

    reg_direx = tk.Entry(reg_cliente, font=("Arial", 11), bd=0)
    reg_direx.place(x=375, y=235, width=310, height=20)
    
        # botones
    btn_ag_direx = tk.Button(reg_cliente, text="Agregar", width=13, height=1, font=("Raleway", 9), command=agregar_direccion)
    btn_ag_direx.place(x=370, y=270)
    
    btn_ed_direx = tk.Button(reg_cliente, text="Editar", width=13, height=1, font=("Raleway", 9), command=edit_direx)
    btn_ed_direx.place(x=480, y=270)
    
    btn_del_direx = tk.Button(reg_cliente, text="Eliminar", width=13, height=1, font=("Raleway", 9))
    btn_del_direx.config(command=lambda: eliminar_fila(tabla_direx, "direccion_actual"))
    btn_del_direx.place(x=590, y=270)
    
        # tabla
    create_rounded_rectangle(canvas_reg_cliente, 360, 320, 700, 513, radius=10, fill="#959595", outline="#959595")

    tabla_direx = ttk.Treeview(reg_cliente, columns=("id_direx", "direx"), show="headings")
    tabla_direx.place(x=360, y=320, width=341, height=194)

    # Configurar las columnas
    tabla_direx.heading("id_direx", text="ID")
    tabla_direx.heading("direx", text="Dirección")

    # Ajustar el tamaño de las columnas
    tabla_direx.column("id_direx", anchor="center", width=41)
    tabla_direx.column("direx", anchor="center", width=298)
    
    

    btn_cli_canc = tk.Button(reg_cliente, text="Cancelar", width=13, height=1, font=("Raleway", 9), command=lambda: confirmar_cancelacion(reg_cliente))
    btn_cli_canc.place(x=425, y=523)
    
    btn_cli_reg = tk.Button(reg_cliente, text="Registrar", width=13, height=1, font=("Raleway", 9), command=guardar_cliente)
    btn_cli_reg.place(x=535, y=523)


def edit_persona_cont():
    
    selected_item = tabla_per_cont.selection()
    if not selected_item:
        mostrar_advertencia()  # Muestra la advertencia personalizada
        return

    # Continuar con la obtención del valor si se seleccionó una fila
    item = tabla_per_cont.item(selected_item)
    persona_contacto_actual = item['values'][1]
    
    
    global inpt_ed_pers_con
    
    ed_pers = tk.Toplevel(root)
    ed_pers.title("Editar Persona de Contacto")
    ed_pers.geometry("340x128")
    ed_pers.resizable(False, False)
    ed_pers.configure(bg="#373737")
    
    centrar_ventana(ed_pers)
    

    ed_pers.grab_set()

    ed_pers.protocol("WM_DELETE_WINDOW", lambda: None)

    canvas_ed_pers = tk.Canvas(ed_pers, width=340, height=128, bg="#373737", highlightthickness=0)
    canvas_ed_pers.pack()

    create_rounded_rectangle(canvas_ed_pers, 10, 10, 330, 78, radius=10, fill="#959595", outline="#959595")

    # persona
    canvas_ed_pers.create_text(20, 20, text="Persona de Contacto", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_ed_pers, 20, 38, 320, 68, radius=10, fill="white", outline="#959595")

    inpt_ed_pers_con = tk.Entry(ed_pers, font=("Arial", 11), bd=0)
    inpt_ed_pers_con.place(x=25, y=43, width=290, height=20)
    
    
    # Función para guardar el cambio
    def guardar_cambio_persona():
        nuevo_valor = inpt_ed_pers_con.get()
        tabla_per_cont.item(selected_item, values=(item['values'][0], nuevo_valor))
        ed_pers.destroy()
    
    
    btn_save_pers = tk.Button(ed_pers, text="Guardar", width=13, height=1, font=("Raleway", 9), command=guardar_cambio_persona)
    btn_save_pers.place(x=10, y=88)

    btn_canc_pers = tk.Button(ed_pers, text="Cancelar", width=13, height=1, font=("Raleway", 9), command=ed_pers.destroy)
    btn_canc_pers.place(x=120, y=88)


def edit_area_trabajo():
    
    selected_item = tabla_ar_trab.selection()
    if not selected_item:
        mostrar_advertencia()  # Muestra la advertencia personalizada
        return

    # Continuar con la obtención del valor si se seleccionó una fila
    item = tabla_ar_trab.item(selected_item)
    area_trabajo_actual = item['values'][1]

    global inpt_ed_ar_trab
    
    ed_ar_trabajo = tk.Toplevel(root)
    ed_ar_trabajo.title("Editar Área de Trabajo")
    ed_ar_trabajo.geometry("340x128")
    ed_ar_trabajo.resizable(False, False)
    ed_ar_trabajo.configure(bg="#373737")
    
    centrar_ventana(ed_ar_trabajo)
    

    ed_ar_trabajo.grab_set()

    ed_ar_trabajo.protocol("WM_DELETE_WINDOW", lambda: None)

    canvas_ed_ar_trab = tk.Canvas(ed_ar_trabajo, width=340, height=128, bg="#373737", highlightthickness=0)
    canvas_ed_ar_trab.pack()

    create_rounded_rectangle(canvas_ed_ar_trab, 10, 10, 330, 78, radius=10, fill="#959595", outline="#959595")

    # persona
    canvas_ed_ar_trab.create_text(20, 20, text="Área de Trabajo", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_ed_ar_trab, 20, 38, 320, 68, radius=10, fill="white", outline="#959595")

    inpt_ed_ar_trab = tk.Entry(ed_ar_trabajo, font=("Arial", 11), bd=0)
    inpt_ed_ar_trab.place(x=25, y=43, width=290, height=20)
    
    
    def guardar_cambio_area():
        nuevo_valor = inpt_ed_ar_trab.get()
        tabla_ar_trab.item(selected_item, values=(item['values'][0], nuevo_valor))
        ed_ar_trabajo.destroy()
    
    
    btn_save_ar_trab = tk.Button(ed_ar_trabajo, text="Guardar", width=13, height=1, font=("Raleway", 9), command=guardar_cambio_area)
    btn_save_ar_trab.place(x=10, y=88)

    btn_canc_ar_trab = tk.Button(ed_ar_trabajo, text="Cancelar", width=13, height=1, font=("Raleway", 9), command=ed_ar_trabajo.destroy)
    btn_canc_ar_trab.place(x=120, y=88)


def edit_direx():
    
    selected_item = tabla_direx.selection()
    if not selected_item:
        mostrar_advertencia()  # Muestra la advertencia personalizada
        return

    # Continuar con la obtención del valor si se seleccionó una fila
    item = tabla_direx.item(selected_item)
    direccion_actual = item['values'][1]
    
    global inpt_ed_direx
    
    ed_direccion = tk.Toplevel(root)
    ed_direccion.title("Editar Dirección")
    ed_direccion.geometry("340x128")
    ed_direccion.resizable(False, False)
    ed_direccion.configure(bg="#373737")
    
    centrar_ventana(ed_direccion)
    

    ed_direccion.grab_set()

    ed_direccion.protocol("WM_DELETE_WINDOW", lambda: None)

    canvas_ed_direccion = tk.Canvas(ed_direccion, width=340, height=128, bg="#373737", highlightthickness=0)
    canvas_ed_direccion.pack()

    create_rounded_rectangle(canvas_ed_direccion, 10, 10, 330, 78, radius=10, fill="#959595", outline="#959595")

    # persona
    canvas_ed_direccion.create_text(20, 20, text="Dirección", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_ed_direccion, 20, 38, 320, 68, radius=10, fill="white", outline="#959595")

    inpt_ed_direx = tk.Entry(ed_direccion, font=("Arial", 11), bd=0)
    inpt_ed_direx.place(x=25, y=43, width=290, height=20)
    
    
    def guardar_cambio_direccion():
        nuevo_valor = inpt_ed_direx.get()
        tabla_direx.item(selected_item, values=(item['values'][0], nuevo_valor))
        ed_direccion.destroy()
    
    
    btn_save_direx = tk.Button(ed_direccion, text="Guardar", width=13, height=1, font=("Raleway", 9), command=guardar_cambio_direccion)
    btn_save_direx.place(x=10, y=88)

    btn_canc_direx = tk.Button(ed_direccion, text="Cancelar", width=13, height=1, font=("Raleway", 9), command=ed_direccion.destroy)
    btn_canc_direx.place(x=120, y=88)



def mostrar_advertencia():
    # Esta función bloqueará la interfaz hasta que el usuario cierre la advertencia
    messagebox.showwarning("Advertencia", "Seleccione una fila para editar.")



def registro_orden_compra():
    
    global oc_nro_compra, reg_oc_cli, cbo_estado_oc, reg_oc_serv, reg_oc_tiempo, fecha_entry
    global archivo_coti, archivo_oc
    
    # Ocultar la ventana principal
    root.withdraw()
    
    # Inicialización de variables de archivos
    archivo_coti = None
    archivo_oc = None
    
    reg_oc = tk.Toplevel(root)
    reg_oc.title("Registro de Orden de Compra")
    reg_oc.geometry("530x358")
    reg_oc.resizable(False, False)
    reg_oc.configure(bg="#373737")
    
    centrar_ventana(reg_oc)
    

    # Crear un Canvas en la ventana de registro
    canvas_oc = tk.Canvas(reg_oc, width=530, height=358, bg="#373737", highlightthickness=0)
    canvas_oc.pack()
    
    canvas_oc.create_text(25, 0, text="Reg. de Orden de Compra", anchor="nw", font=("Raleway", 30, "bold"), fill="White")

    create_rounded_rectangle(canvas_oc, 10, 66, 260, 308, radius=10, fill="#959595", outline="#959595")

    create_rounded_rectangle(canvas_oc, 270, 66, 520, 308, radius=10, fill="#959595", outline="#959595")
    
    # n° de oc
    canvas_oc.create_text(20, 76, text="N° de Orden de Compra", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_oc, 20, 94, 250, 124, radius=10, fill="white", outline="#959595")

    oc_nro_compra = tk.Entry(reg_oc, font=("Arial", 11), bd=0)
    oc_nro_compra.place(x=25, y=99, width=220, height=20)
    
    # cliente / empresas
    canvas_oc.create_text(20, 134, text="Cliente / Empresa", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_oc, 20, 152, 250, 182, radius=10, fill="white", outline="#959595")

    reg_oc_cli = tk.Entry(reg_oc, font=("Arial", 11), bd=0)
    reg_oc_cli.place(x=25, y=157, width=220, height=20)
    
    # estado oc
    canvas_oc.create_text(20, 192, text="Estado", anchor="nw", font=("Raleway", 10), fill="black")

    cbo_estado_oc = ttk.Combobox(reg_oc, values=["Seleccione una Opción", "Trabajo No Iniciado", "En Proceso", "Completado Parcialmente", "Finalizado"], state="readonly", font=("Raleway", 10))
    cbo_estado_oc.place(x=20, y=210, width=230, height=31)
    cbo_estado_oc.current(0)
    
    # servicio
    canvas_oc.create_text(20, 250, text="Servicio", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_oc, 20, 268, 250, 298, radius=10, fill="white", outline="#959595")

    reg_oc_serv = tk.Entry(reg_oc, font=("Arial", 11), bd=0)
    reg_oc_serv.place(x=25, y=273, width=220, height=20)
    
    # tiempo ejec
    canvas_oc.create_text(280, 76, text="Tiempo de Ejecución", anchor="nw", font=("Raleway", 10), fill="black")

    create_rounded_rectangle(canvas_oc, 280, 94, 510, 124, radius=10, fill="white", outline="#959595")

    reg_oc_tiempo = tk.Entry(reg_oc, font=("Arial", 11), bd=0)
    reg_oc_tiempo.place(x=285, y=99, width=220, height=20)
    
    # fecha reg
    canvas_oc.create_text(280, 134, text="Fecha de Registro", anchor="nw", font=("Raleway", 10), fill="black")
    
    fecha_entry = DateEntry(reg_oc, font=("Raleway", 11),state="readonly" , width=17, background='darkblue', foreground='white', borderwidth=2)
    fecha_entry.place(x=280, y=152, width=230, height=30)
    
        # DOCUMENTOS
    
            # COTIZACION
    canvas_oc.create_text(280, 192, text="Cotización", anchor="nw", font=("Raleway", 10), fill="black")
    
    button_coti = tk.Button(reg_oc, text="Adjuntar doc.", command=lambda: adjuntar_archivo(label_coti, "cotizacion"))
    button_coti.place(x=280, y=210, width=93, height=30)
    
    # Etiqueta para mostrar el nombre del archivo seleccionado
    global label_coti
    label_coti = tk.Label(reg_oc, text="Cotización", font=("Raleway", 9), bg="#373737", fg="white")
    label_coti.place(x=380, y=210, width=130, height=30)
    
    
            # ORDEN DE COMPRA
    canvas_oc.create_text(280, 250, text="Orden de Compra", anchor="nw", font=("Raleway", 10), fill="black")
    
    button_oc = tk.Button(reg_oc, text="Adjuntar doc.", command=lambda: adjuntar_archivo(label_oc, "orden_compra"))
    button_oc.place(x=280, y=268, width=93, height=30)
    
    global label_oc
    label_oc = tk.Label(reg_oc, text="Orden de Compra", font=("Raleway", 9), bg="#373737", fg="white")
    label_oc.place(x=380, y=268, width=130, height=30)
    
    
    
    btn_canc_oc = tk.Button(reg_oc, text="Cancelar", width=13, height=1, font=("Raleway", 9), command=cerrar_programa)
    btn_canc_oc.place(x=160, y=319)

    btn_reg_oc = tk.Button(reg_oc, text="Registrar", width=13, height=1, font=("Raleway", 9))
    btn_reg_oc.place(x=270, y=319)


def busqueda():
    
    # Ocultar la ventana principal
    root.withdraw()
    
    vent_busq = tk.Toplevel(root)
    vent_busq.title("Búsqueda")
    vent_busq.geometry("430x396")
    vent_busq.resizable(False, False)
    vent_busq.configure(bg="#373737")
    
    centrar_ventana(vent_busq)
    

    canv_busq = tk.Canvas(vent_busq, width=430, height=396, bg="#373737", highlightthickness=0)
    canv_busq.pack()
    
    create_rounded_rectangle(canv_busq, 10, 10, 420, 386, radius=10, fill="#959595", outline="#959595")
    
    
    def vistap_busq(event):
        if busq_entry.get() == "":
            busq_entry.insert(0, "Buscar...")
            busq_entry.config(fg='grey')

    def limpiar_busq(event):
        if busq_entry.get() == "Buscar...":
            busq_entry.delete(0, tk.END)
            busq_entry.config(fg='black')
    
    
    busq_canv = tk.Canvas(vent_busq, width=350, height=40, bg="#373737", highlightthickness=0)
    busq_canv.place(x=40, y=20)

    create_rounded_rectangle(busq_canv, 0, 0, 350, 40, radius=10, fill="white", outline="gray")

    busq_entry = tk.Entry(busq_canv, font=("Raleway", 13), width=40, bd=0, relief="flat", fg='grey')
    busq_entry.insert(0, "Buscar...")  # Insertar texto de placeholder
    busq_entry.bind("<FocusIn>", limpiar_busq)  # Limpiar cuando el usuario hace clic
    busq_entry.bind("<FocusOut>", vistap_busq)  # Volver a mostrar si está vacío
    busq_entry.place(x=6, y=7, width=337, height=27)
    
    
    
    
    def volver_a_principal():
        vent_busq.destroy()
        root.deiconify()
    
    btn_atras = tk.Button(vent_busq, text="Atrás", width=13, height=1, font=("Raleway", 9), command=volver_a_principal)
    btn_atras.place(x=165, y=348)


def seguimiento_factura():
    
    # Ocultar la ventana principal
    root.withdraw()
    
    seg_fact = tk.Toplevel(root)
    seg_fact.title("Seguimiento de Factura")
    seg_fact.geometry("570x474")
    seg_fact.resizable(False, False)
    seg_fact.configure(bg="#373737")
    
    centrar_ventana(seg_fact)
    

    canvas_fact = tk.Canvas(seg_fact, width=570, height=474, bg="#373737", highlightthickness=0)
    canvas_fact.pack()
    
    canvas_fact.create_text(62, 0, text="Seguimiento de Factura", anchor="nw", font=("Raleway", 30, "bold"), fill="White")

    create_rounded_rectangle(canvas_fact, 10, 66, 280, 424, radius=10, fill="#959595", outline="#959595")

    create_rounded_rectangle(canvas_fact, 290, 66, 560, 424, radius=10, fill="#959595", outline="#959595")

        # DOCUMENTOS
        
            # COTIZACION
    canvas_fact.create_text(20, 76, text="Cotización", anchor="nw", font=("Raleway", 10), fill="black")
    
    
    
            # ORDEN DE COMRRA
    canvas_fact.create_text(20, 134, text="Orden de Compra", anchor="nw", font=("Raleway", 10), fill="black")
    
    
    
            # GUIA DE REMISION
    canvas_fact.create_text(20, 192, text="Guía de Remisión", anchor="nw", font=("Raleway", 10), fill="black")
    
    button_guia = tk.Button(seg_fact, text="Adjuntar doc.", command=lambda: adjuntar_archivo(label_guia, "guia_remision"))
    button_guia.place(x=20, y=210, width=100, height=30)
    
    global label_guia
    label_guia = tk.Label(seg_fact, text="Guía de Remisión", font=("Raleway", 9), bg="#373737", fg="white")
    label_guia.place(x=130, y=210, width=140, height=30)
    
    
            # ACTA DE CONFORMIDAD
    canvas_fact.create_text(20, 250, text="Acta de Conformidad", anchor="nw", font=("Raleway", 10), fill="black")
    
    button_acta = tk.Button(seg_fact, text="Adjuntar doc.", command=lambda: adjuntar_archivo(label_acta, "acta_conformidad"))
    button_acta.place(x=20, y=268, width=100, height=30)
    
    global label_acta
    label_acta = tk.Label(seg_fact, text="Acta de Conformidad", font=("Raleway", 9), bg="#373737", fg="white")
    label_acta.place(x=130, y=268, width=140, height=30)
    
    
            # INFORME TECNICO
    canvas_fact.create_text(20, 308, text="Informe Técnico", anchor="nw", font=("Raleway", 10), fill="black")
    
    button_informe = tk.Button(seg_fact, text="Adjuntar doc.", command=lambda: adjuntar_archivo(label_informe, "informe_tecnico"))
    button_informe.place(x=20, y=326, width=100, height=30)
    
    global label_informe
    label_informe = tk.Label(seg_fact, text="Informe Técnico", font=("Raleway", 9), bg="#373737", fg="white")
    label_informe.place(x=130, y=326, width=140, height=30)
    
    
            # PLANOS
    canvas_fact.create_text(20, 366, text="Planos", anchor="nw", font=("Raleway", 10), fill="black")
    
    button_planos = tk.Button(seg_fact, text="Adjuntar doc.", command=lambda: adjuntar_archivo(label_planos, "doc_planos"))
    button_planos.place(x=20, y=384, width=100, height=30)
    
    global label_planos
    label_planos = tk.Label(seg_fact, text="Planos", font=("Raleway", 9), bg="#373737", fg="white")
    label_planos.place(x=130, y=384, width=140, height=30)
    

            # FACTURA
    canvas_fact.create_text(300, 76, text="Factura", anchor="nw", font=("Raleway", 10), fill="black")
    
    button_fact = tk.Button(seg_fact, text="Adjuntar doc.", command=lambda: adjuntar_archivo(label_fact, "doc_factura"))
    button_fact.place(x=300, y=94, width=100, height=30)
    
    global label_fact
    label_fact = tk.Label(seg_fact, text="Factura", font=("Raleway", 9), bg="#373737", fg="white")
    label_fact.place(x=410, y=94, width=140, height=30)
    
    
    
    # nro de cotzcn
    canvas_fact.create_text(300, 134, text="Nro de Cotización", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_fact, 300, 152, 550, 182, radius=10, fill="white", outline="#959595")

    seg_fact_nro_ctzc = tk.Entry(seg_fact, font=("Arial", 11), bd=0)
    seg_fact_nro_ctzc.place(x=305, y=157, width=240, height=20)
    
    # nro de fact
    canvas_fact.create_text(300, 192, text="Nro de Factura", anchor="nw", font=("Raleway", 10), fill="black")
    
    create_rounded_rectangle(canvas_fact, 300, 210, 550, 240, radius=10, fill="white", outline="#959595")

    seg_fact_nro_fact = tk.Entry(seg_fact, font=("Arial", 11), bd=0)
    seg_fact_nro_fact.place(x=305, y=215, width=240, height=20)
    
    # fecha de facturacion
    canvas_fact.create_text(300, 250, text="Fecha de Facturación", anchor="nw", font=("Raleway", 10), fill="black")
    
    date_fact = DateEntry(seg_fact, font=("Raleway", 11),state="readonly" , width=17, background='darkblue', foreground='white', borderwidth=2)
    date_fact.place(x=300, y=268, width=250, height=30)
    
    # estado
    canvas_fact.create_text(300, 308, text="Estado", anchor="nw", font=("Raleway", 10), fill="black")
    
    cbo_estado_fact = ttk.Combobox(seg_fact, values=["Seleccione una Opción", "Cancelado", "Pendiente", "No Cancelado"], state="readonly", font=("Raleway", 10))
    cbo_estado_fact.place(x=300, y=326, width=250, height=31)
    cbo_estado_fact.current(0)
    
    # forma de pago
    canvas_fact.create_text(300, 366, text="Forma de Pago", anchor="nw", font=("Raleway", 10), fill="black")
    
    cbo_forma_pag = ttk.Combobox(seg_fact, values=["Seleccione una Opción", "30 días", "60 días", "90 días", "180 días", "Al contado"], state="readonly", font=("Raleway", 10))
    cbo_forma_pag.place(x=300, y=384, width=250, height=31)
    cbo_forma_pag.current(0)
    
    
    btn_canc_fact = tk.Button(seg_fact, text="Cancelar", width=13, height=1, font=("Raleway", 9), command=cerrar_programa)
    btn_canc_fact.place(x=180, y=435)
    
    btn_reg_fact = tk.Button(seg_fact, text="Registrar", width=13, height=1, font=("Raleway", 9))
    btn_reg_fact.place(x=290, y=435)


# Crear la ventana principal
root = tk.Tk()
root.title("Inicio")
root.geometry("1400x700")
root.resizable(False, False)  # Evitar que la ventana se redimensione
root.configure(bg="#373737")

centrar_ventana(root)

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

canvas.create_text(480, 23, text="Soluciones Plasticas Metálicas SAC", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

# Botones opcion
btn_cli = tk.Button(root, text="Registrar Nuevo Cliente", width=37, height=1, font=("Raleway", 9), command=registro_clientes)
btn_cli.place(x=20, y=80)

btn_cot = tk.Button(root, text="Generar Cotización", width=37, height=1, font=("Raleway", 9), command=crear_cotiz)
btn_cot.place(x=20, y=125)

btn_oc = tk.Button(root, text="Registrar Orden de Compra", width=37, height=1, font=("Raleway", 9), command=registro_orden_compra)
btn_oc.place(x=20, y=170)

btn_sef = tk.Button(root, text="Seguimiento de Factura", width=37, height=1, font=("Raleway", 9), command=seguimiento_factura)
btn_sef.place(x=20, y=215)

btn_bus = tk.Button(root, text="Búsqueda de Documentos", width=37, height=1, font=("Raleway", 9), command=busqueda)
btn_bus.place(x=20, y=260)

btn_act = tk.Button(root, text="Actualizar Registro", width=37, height=1, font=("Raleway", 9))
btn_act.place(x=20, y=305)

btn_ex = tk.Button(root, text="Salir del Programa", width=37, height=1, font=("Raleway", 9), command=cerrar_programa)
btn_ex.place(x=20, y=350)


btn_next = tk.Button(root, text="Siguiente", width=20, height=1, font=("Raleway", 9))
btn_next.place(x=1240, y=660)

btn_prev = tk.Button(root, text="Atrás", width=20, height=1, font=("Raleway", 9))
btn_prev.place(x=1082, y=660)

# filtro oc
canvas.create_text(20, 466, text="Por Orden de Compra", anchor="nw", font=("Raleway", 10), fill="black")

cbo_oc = ttk.Combobox(root, values=["Todos los registros", "Trabajo No Iniciado", "En Proceso", "Completado Parcialmente", "Finalizado"], state="readonly", font=("Raleway", 10))
cbo_oc.place(x=20, y=484, width=269, height=30)
cbo_oc.current(0)  # 484

# filtro fac
canvas.create_text(20, 520, text="Por Factura", anchor="nw", font=("Raleway", 10), fill="black")

cbo_fac = ttk.Combobox(root, values=["Todos los registros", "Cancelado", "Pendiente", "No Cancelado"], state="readonly", font=("Raleway", 10))
cbo_fac.place(x=20, y=538, width=269, height=30)
cbo_fac.current(0)



# Buscador
search_canvas = tk.Canvas(root, width=350, height=40, bg="#373737", highlightthickness=0)
search_canvas.place(x=1040, y=20)

create_rounded_rectangle(search_canvas, 0, 0, 350, 40, radius=10, fill="white", outline="gray")

search_entry = tk.Entry(search_canvas, font=("Raleway", 13), width=40, bd=0, relief="flat", fg='grey')
search_entry.insert(0, "Buscar...")  # Insertar texto de placeholder
search_entry.bind("<FocusIn>", clear_placeholder)  # Limpiar cuando el usuario hace clic
search_entry.bind("<FocusOut>", placeholder_search)  # Volver a mostrar si está vacío
search_entry.place(x=6, y=7, width=337, height=27)



# Tabla del cuadro base
tree = ttk.Treeview(root, columns=("oc", "estado_oc", "cliente", "descripcion", "fac", "estado_fac", "fecha_fac"), show="headings")
tree.place(x=310, y=80, width=1080, height=572)

# Configurar las columnas
tree.heading("oc", text="Orden de Compra")
tree.heading("estado_oc", text="Estado")
tree.heading("cliente", text="Cliente / Empresa")
tree.heading("descripcion", text="Descripción / Servicio")
tree.heading("fac", text="Factura")
tree.heading("estado_fac", text="Estado")
tree.heading("fecha_fac", text="Fecha Factura")

# Ajustar el tamaño de las columnas
tree.column("oc", anchor="center", width=100)
tree.column("estado_oc", anchor="center", width=110)
tree.column("cliente", anchor="center", width=200)
tree.column("descripcion", anchor="center", width=280)
tree.column("fac", anchor="center", width=100)
tree.column("estado_fac", anchor="center", width=110)
tree.column("fecha_fac", anchor="center", width=110)


# Ejecutar la interfaz
root.mainloop()
