import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from tkcalendar import DateEntry
import os
import shutil
from tkinter import PhotoImage
import utils


# NOTIFICACIONES - CONFIRMACIONES
class alertas:
    def __init__(self, parent):
        self.parent = parent
    
    # CERRAR EL PROGRAMA --
    def cerrar_prog(self):
        salida=tk.Toplevel(self.parent)
        salida.title("")
        salida.geometry("300x110")
        salida.resizable(False, False)
        salida.configure(bg="#FFFFFF")
        salida.grab_set()
        utils.centrar_ventana(salida)
        salida.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_salida = tk.Canvas(salida, width=300, height=110, bg="#FFFFFF", highlightthickness=0)
        canvas_salida.pack()
        
        # Cargar el icono
        icono_alert_ex = tk.PhotoImage(file="SPM---python/icons/question.png")
        canvas_salida.create_image(30, 17, anchor="nw", image=icono_alert_ex)
        canvas_salida.image = icono_alert_ex

        utils.create_rounded_rectangle(canvas_salida, 0, 66, 300, 110, radius=0, fill="#EEEEE4", outline="#EEEEE4")
        
        canvas_salida.create_text(79, 26, text="¿Está seguro de que desea salir?", anchor="nw", font=("Arial", 10), fill="Black")
        
        btn_si = tk.Button(salida, text="Si", width=9, height=1, font=("Raleway", 9), command=self.parent.destroy)
        btn_si.place(x=73, y=73)

        btn_no = tk.Button(salida, text="No", width=9, height=1, font=("Raleway", 9), command=salida.destroy)
        btn_no.place(x=158, y=73)

    # SELECCIONE UNA FILA
    def seleccionar_fila(self):
        sec_fila=tk.Toplevel(self.parent)
        sec_fila.title("")
        sec_fila.geometry("300x110")
        sec_fila.resizable(False, False)
        sec_fila.configure(bg="#FFFFFF")
        sec_fila.grab_set()
        utils.centrar_ventana(sec_fila)
        sec_fila.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_sec_fila = tk.Canvas(sec_fila, width=300, height=110, bg="#FFFFFF", highlightthickness=0)
        canvas_sec_fila.pack()
        
        # Cargar el icono
        icono_alert_sec = tk.PhotoImage(file="SPM---python/icons/alert.png")
        canvas_sec_fila.create_image(30, 17, anchor="nw", image=icono_alert_sec)
        canvas_sec_fila.image = icono_alert_sec

        utils.create_rounded_rectangle(canvas_sec_fila, 0, 66, 300, 110, radius=0, fill="#EEEEE4", outline="#EEEEE4")
        
        canvas_sec_fila.create_text(79, 26, text="Por favor, seleccione una fila", anchor="nw", font=("Arial", 10), fill="Black")
        
        btn_sec_ok = tk.Button(sec_fila, text="Aceptar", width=9, height=1, font=("Raleway", 9), command=sec_fila.destroy)
        btn_sec_ok.place(x=115, y=73)

    # DATO NO ENCONTRADO
    def no_datos(self):
        no_file=tk.Toplevel(self.parent)
        no_file.title("")
        no_file.geometry("300x110")
        no_file.resizable(False, False)
        no_file.configure(bg="#FFFFFF")
        no_file.grab_set()
        utils.centrar_ventana(no_file)
        no_file.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_no_file = tk.Canvas(no_file, width=300, height=110, bg="#FFFFFF", highlightthickness=0)
        canvas_no_file.pack()
        
        # Cargar el icono
        icono_alert_nf = tk.PhotoImage(file="SPM---python/icons/delete.png")
        canvas_no_file.create_image(30, 17, anchor="nw", image=icono_alert_nf)
        canvas_no_file.image = icono_alert_nf

        utils.create_rounded_rectangle(canvas_no_file, 0, 66, 300, 110, radius=0, fill="#EEEEE4", outline="#EEEEE4")
        
        canvas_no_file.create_text(94, 26, text="Datos no encontrados", anchor="nw", font=("Arial", 10), fill="Black")
        
        btn_nf_ok = tk.Button(no_file, text="Aceptar", width=9, height=1, font=("Raleway", 9), command=no_file.destroy)
        btn_nf_ok.place(x=115, y=73)


class generator_cot:
    def __init__(self, root, gen_cot):
        
        self.root = root
        self.gen_cot = gen_cot
        self.root.withdraw()
        
        self.gen_cot = gen_cot
        self.gen_cot.title("Generar Cotización")
        self.gen_cot.geometry("750x714")
        self.gen_cot.resizable(False, False)
        self.gen_cot.configure(bg="#373737")
        utils.centrar_ventana(self.gen_cot)
        
        self.gen_cot.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_coti = tk.Canvas(gen_cot, width=750, height=714, bg="#373737", highlightthickness=0)
        canvas_coti.pack()
        
        utils.create_rounded_rectangle(canvas_coti, 10, 10, 740, 252, radius=10, fill="#959595", outline="#959595")
        utils.create_rounded_rectangle(canvas_coti, 10, 262, 740, 388, radius=10, fill="#959595", outline="#959595")
        utils.create_rounded_rectangle(canvas_coti, 10, 438, 740, 586, radius=10, fill="#959595", outline="#959595")
        utils.create_rounded_rectangle(canvas_coti, 10, 596, 740, 664, radius=10, fill="#959595", outline="#959595")
        
        
        canvas_coti.create_text(20, 20, text="Nro de Cotización", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 20, 38, 170, 68, radius=10, fill="white", outline="#959595")
        input_gcoti = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gcoti.place(x=25, y=43, width=140, height=20)
        
        canvas_coti.create_text(180, 20, text="Fecha", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 180, 38, 360, 68, radius=10, fill="white", outline="#959595")
        input_gfecha = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gfecha.place(x=185, y=43, width=170, height=20)
        
        canvas_coti.create_text(370, 20, text="Cliente / Empresa", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 370, 38, 570, 68, radius=10, fill="white", outline="#959595")
        input_gpersona = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gpersona.place(x=375, y=43, width=190, height=20)
        
        canvas_coti.create_text(580, 20, text="Área", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        cbo_area = ttk.Combobox(gen_cot, values=["Escoja una Opción", "Ejemplo1"], state="readonly", font=("Raleway", 10))
        cbo_area.place(x=580, y=38, width=150, height=31)
        cbo_area.current(0)
        
        
        canvas_coti.create_text(20, 78, text="Persona de Contacto", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        cbo_persona = ttk.Combobox(gen_cot, values=["Escoja una Opción", "Ejemplo1"], state="readonly", font=("Raleway", 10))
        cbo_persona.place(x=20, y=96, width=230, height=31)
        cbo_persona.current(0)
        
        canvas_coti.create_text(260, 78, text="Título del Servicio", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 260, 96, 730, 126, radius=10, fill="white", outline="#959595")
        input_gtitulo = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gtitulo.place(x=265, y=101, width=460, height=20)
        
        
        canvas_coti.create_text(20, 136, text="Tiempo de Ejecución", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 20, 154, 290, 184, radius=10, fill="white", outline="#959595")
        input_gtiempo = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gtiempo.place(x=25, y=159, width=260, height=20)
        
        canvas_coti.create_text(300, 136, text="Forma de Pago", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 300, 154, 540, 184, radius=10, fill="white", outline="#959595")
        input_gpago = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gpago.place(x=305, y=159, width=230, height=20)
        
        canvas_coti.create_text(550, 136, text="IGV", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        cbo_igv = ttk.Combobox(gen_cot, values=["SI", "NO"], state="readonly", font=("Raleway", 10))
        cbo_igv.place(x=550, y=154, width=50, height=31)
        cbo_igv.current(0)
        
        canvas_coti.create_text(610, 136, text="Tipo de Moneda", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        cbo_moneda = ttk.Combobox(gen_cot, values=["PEN", "USD"], state="readonly", font=("Raleway", 10))
        cbo_moneda.place(x=610, y=154, width=120, height=31)
        cbo_moneda.current(0)
        
        canvas_coti.create_text(20, 194, text="Tipo de Cuenta", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        cbo_cuenta = ttk.Combobox(gen_cot, values=["Cuenta Soles", "Cuenta Dólares"], state="readonly", font=("Raleway", 10))
        cbo_cuenta.place(x=20, y=212, width=145, height=31)
        cbo_cuenta.current(0)
        
        canvas_coti.create_text(176, 194, text="Nro de Cuenta", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 176, 212, 446, 242, radius=10, fill="white", outline="#959595")
        input_gcuenta = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gcuenta.place(x=181, y=217, width=260, height=20)
        
        canvas_coti.create_text(456, 194, text="Cuenta Interbancaria", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 456, 212, 730, 242, radius=10, fill="white", outline="#959595")
        input_gcuentabanc = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gcuentabanc.place(x=461, y=217, width=264, height=20)
        
        
        canvas_coti.create_text(20, 272, text="Descripción", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 20, 290, 730, 320, radius=10, fill="white", outline="#959595")
        input_gdesc = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gdesc.place(x=25, y=295, width=700, height=20)
        
        canvas_coti.create_text(20, 330, text="Material(es)", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 20, 348, 420, 378, radius=10, fill="white", outline="#959595")
        input_gmaterial = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gmaterial.place(x=25, y=353, width=390, height=20)
        
        canvas_coti.create_text(430, 330, text="Unidad(es)", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 430, 348, 485, 378, radius=10, fill="white", outline="#959595")
        input_gunidad = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gunidad.place(x=435, y=353, width=45, height=20)
        cbo_unidad = ttk.Combobox(gen_cot, values=["JUEGO", "PIEZA"], state="readonly", font=("Raleway", 10))
        cbo_unidad.place(x=495, y=348, width=100, height=31)
        cbo_unidad.current(0)
        
        canvas_coti.create_text(605, 330, text="Precio Unit.", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 605, 348, 730, 378, radius=10, fill="white", outline="#959595")
        input_gpreciou = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gpreciou.place(x=610, y=353, width=115, height=20)
        
        
        canvas_coti.create_text(20, 606, text="Dscto. (%)", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 20, 624, 130, 654, radius=10, fill="white", outline="#959595")
        input_gdescuento = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gdescuento.place(x=25, y=629, width=100, height=20)
        
        canvas_coti.create_text(260, 606, text="SubTotal", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 260, 624, 370, 654, radius=10, fill="white", outline="#959595")
        input_gsubtot = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gsubtot.place(x=265, y=629, width=100, height=20)
        
        canvas_coti.create_text(380, 606, text="IGV", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 380, 624, 490, 654, radius=10, fill="white", outline="#959595")
        input_gigv = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gigv.place(x=385, y=629, width=100, height=20)
        
        canvas_coti.create_text(500, 606, text="Dscto.", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 500, 624, 610, 654, radius=10, fill="white", outline="#959595")
        input_gdescto = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gdescto.place(x=505, y=629, width=100, height=20)
        
        canvas_coti.create_text(620, 606, text="Total", anchor="nw", font=("Raleway", 10, "bold"), fill="white")
        utils.create_rounded_rectangle(canvas_coti, 620, 624, 730, 654, radius=10, fill="white", outline="#959595")
        input_gtotal = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gtotal.place(x=625, y=629, width=100, height=20)
        
        
        btn_ag = tk.Button(gen_cot, text="Agregar", width=13, height=1, font=("Raleway", 9))
        btn_ag.place(x=10, y=398)
        
        btn_ed = tk.Button(gen_cot, text="Editar", width=13, height=1, font=("Raleway", 9))
        btn_ed.place(x=120, y=398)
        
        btn_del = tk.Button(gen_cot, text="Eliminar", width=13, height=1, font=("Raleway", 9))
        btn_del.place(x=230, y=398)
            
        btn_canc = tk.Button(gen_cot, text="Cancelar", width=13, height=1, font=("Raleway", 9))
        btn_canc.place(x=10, y=674)

        btn_gen = tk.Button(gen_cot, text="Generar", width=13, height=1, font=("Raleway", 9))
        btn_gen.place(x=120, y=674)
        
        
        t_material = ttk.Treeview(gen_cot, columns=("desc", "mat", "und", "p_unit", "s_total"), show="headings", style="Custom.Treeview")
        t_material.place(x=10, y=438, width=731, height=149)
                                                    # - 155
        
        t_material.heading("desc", text="Descripción")
        t_material.heading("mat", text="Material")
        t_material.heading("und", text="Unidad(es)")
        t_material.heading("p_unit", text="Precio Unit.")
        t_material.heading("s_total", text="SubTotal")
        
        t_material.column("desc", anchor="center", width=226, stretch=False)
        t_material.column("mat", anchor="center", width=192, stretch=False)
        t_material.column("und", anchor="center", width=99, stretch=False)
        t_material.column("p_unit", anchor="center", width=99, stretch=False)
        t_material.column("s_total", anchor="center", width=99, stretch=False)
        
        scrollbar_vertical = ttk.Scrollbar(gen_cot, orient="vertical", command=t_material.yview)
        t_material.configure(yscrollcommand=scrollbar_vertical.set)
        scrollbar_vertical.place(x=727, y=438, height=149)
        
        ejemplos_t_material = [
            ("Soporte metálico", "Acero Inoxidable", "5", "35.00", "175.00"),
            ("Cableado estructurado", "Cobre", "10", "25.00", "250.00"),
            ("Panel divisor", "Policarbonato", "8", "45.50", "364.00"),
            ("Tubos de conexión", "PVC", "12", "15.30", "183.60"),
            ("Láminas de aislamiento", "Aluminio", "20", "22.00", "440.00"),
            ("Juego de tornillos", "Acero galvanizado", "50", "0.80", "40.00"),
            ("Pintura resistente al calor", "Base Epóxica", "3", "120.00", "360.00"),
            ("Ruedas industriales", "Poliuretano", "4", "85.00", "340.00"),
            ("Cables de alimentación", "Aluminio blindado", "15", "18.00", "270.00"),
            ("Conectores rápidos", "Latón", "30", "2.50", "75.00"),
        ]
        
        for dato in ejemplos_t_material:
            t_material.insert("", "end", values=dato)
    
    
    def editar_material(self):
        ed_material = tk.Toplevel(self.gen_cot)
        ed_material.title("Editar Material")
        ed_material.geometry("600x186")
        ed_material.resizable(False, False)
        ed_material.configure(bg="#373737")
        utils.centrar_ventana(ed_material)
        
        canvas_mat = tk.Canvas(ed_material, width=600, height=186, bg="#373737", highlightthickness=0)
        canvas_mat.pack()
        
        
        
        
        
class ventana_inicio:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio")
        self.root.geometry("1400x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#373737")
        utils.centrar_ventana(root)
        
        self.alerta = alertas(root)
        
        # Usar el método cerrar_prog de alertas para el cierre de la ventana principal
        self.root.protocol("WM_DELETE_WINDOW", self.alerta.cerrar_prog)

        canvas = tk.Canvas(root, width=1400, height=700, bg="#373737", highlightthickness=0)
        canvas.pack()

        utils.create_rounded_rectangle(canvas, 10, 10, 300, 480, radius=10, fill="#959595", outline="#959595")
        utils.create_rounded_rectangle(canvas, 10, 490, 300, 688, radius=10, fill="#959595", outline="#959595")
        #utils.create_rounded_rectangle(canvas, 310, 80, 1390, 650, radius=10, fill="#959595", outline="#959595")

        canvas.create_text(20, 22, text="Opciones", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

        # Botones opcion
        btn_gen_cot = tk.Button(root, text="Generar Cotización", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white", command=self.abrir_ventana_cotizacion)
        btn_gen_cot.place(x=22, y=80)

        btn_reg_cli = tk.Button(root, text="Ver Registro de Clientes", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_reg_cli.place(x=22, y=125)

        btn_reg_cot = tk.Button(root, text="Ver Registro de Cotización", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_reg_cot.place(x=22, y=170)

        btn_reg_oc = tk.Button(root, text="Ver Registro de Orden de Compra", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_reg_oc.place(x=22, y=215)

        btn_reg_fact = tk.Button(root, text="Registrar Factura", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_reg_fact.place(x=22, y=260)

        btn_seg_fact = tk.Button(root, text="Seguimiento de Factura", width=37, height=1, font=("Raleway", 9), command=self.alerta.seleccionar_fila, activebackground="#7F7F7F", activeforeground="white")
        btn_seg_fact.place(x=22, y=305)

        btn_search = tk.Button(root, text="Buscar Documentos", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_search.place(x=22, y=350)

        btn_act = tk.Button(root, text="Actualizar Registro", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_act.place(x=22, y=395)

        btn_exit = tk.Button(self.root, text="Salir", width=37, height=1, font=("Raleway", 9), command=self.alerta.cerrar_prog, activebackground="#7F7F7F", activeforeground="white")
        btn_exit.place(x=22, y=440)

        # Vincular los eventos a cada botón
        for btn in [btn_gen_cot, btn_reg_cli, btn_reg_cot, btn_reg_oc, btn_reg_fact, btn_seg_fact, btn_search, btn_act, btn_exit]:
            btn.bind("<Enter>", lambda e, b=btn: utils.on_enter(b))
            btn.bind("<Leave>", lambda e, b=btn: utils.on_leave(b))

        canvas.create_text(20, 502, text="Filtros", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

        canvas.create_text(20, 560, text="Por Orden de Compra", anchor="nw", font=("Raleway", 10), fill="black")
        
        cbo_oc = ttk.Combobox(root, values=["Todos los registros", "Trabajo No Iniciado", "En Proceso", "Completado Parcialmente", "Finalizado"], state="readonly", font=("Raleway", 10))
        cbo_oc.place(x=20, y=578, width=250, height=30)
        cbo_oc.current(0)

        canvas.create_text(20, 614, text="Por Factura", anchor="nw", font=("Raleway", 10), fill="black")
        
        cbo_fact = ttk.Combobox(root, values=["Todos los registros", "Cancelado", "Pendiente", "No Cancelado"], state="readonly", font=("Raleway", 10))
        cbo_fact.place(x=20, y=632, width=250, height=30)
        cbo_fact.current(0)
        
        cbo_page = ttk.Combobox(root, values=["1", "2"], state="readonly", font=("Arial", 10))
        cbo_page.place(x=310, y=660, width=70, height=30)
        cbo_page.current(0)

        canvas.create_text(400, 23, text="SOLUCIONES PLÁSTICAS METÁLICAS SAC", anchor="nw", font=("Raleway", 21, "bold"), fill="White")
        
        search_canvas = tk.Canvas(root, width=350, height=40, bg="#373737", highlightthickness=0)
        search_canvas.place(x=1040, y=20)
        
        utils.create_rounded_rectangle(search_canvas, 0, 0, 350, 40, radius=10, fill="white", outline="gray")
        search_canvas.create_line(315, 7, 315, 34, fill="gray", width=2)
        
        search_icon = tk.PhotoImage(file="SPM---python/icons/loupe.png")
        search_icon_id = search_canvas.create_image(321, 8, anchor="nw", image=search_icon)
        search_canvas.image = search_icon
        
        search_canvas.tag_bind(search_icon_id, "<Button-1>", lambda e: self.alerta.no_datos())
        
        search_entry = tk.Entry(search_canvas, font=("Arial", 13), width=40, bd=0, relief="flat", fg='grey')
        search_entry.insert(0, "Buscar...")  # Insertar texto de placeholder
        search_entry.bind("<FocusIn>", lambda event: utils.clear_placeholder(event, search_entry))  # Limpiar cuando el usuario hace clic
        search_entry.bind("<FocusOut>", lambda event: utils.placeholder_search(event, search_entry))  # Volver a mostrar si está vacío
        search_entry.place(x=6, y=7, width=301, height=27)
        
        style = ttk.Style()
        style.theme_use("clam") 
        
        style.configure("Custom.Treeview.Heading", background="lightblue", foreground="black", font=("Arial", 9))
        style.configure("Custom.Treeview", background="white", foreground="black", rowheight=30)

        tree = ttk.Treeview(root, columns=("oc", "estado_oc", "cliente", "descripcion", "fac", "estado_fac", "fecha_fac"), show="headings", style="Custom.Treeview")
        tree.place(x=310, y=80, width=1081, height=569)

        tree.heading("oc", text="Orden de Compra")
        tree.heading("estado_oc", text="Estado")
        tree.heading("cliente", text="Cliente / Empresa")
        tree.heading("descripcion", text="Descripción / Servicio")
        tree.heading("fac", text="Factura")
        tree.heading("estado_fac", text="Estado")
        tree.heading("fecha_fac", text="Fecha Factura")

        tree.column("oc", anchor="center", width=120, stretch=False)
        tree.column("estado_oc", anchor="center", width=148, stretch=False)
        tree.column("cliente", anchor="center", width=200, stretch=False)
        tree.column("descripcion", anchor="center", width=284, stretch=False)
        tree.column("fac", anchor="center", width=100, stretch=False)
        tree.column("estado_fac", anchor="center", width=115, stretch=False)
        tree.column("fecha_fac", anchor="center", width=110, stretch=False)

        ejemplos = [
            ("OC001", "Trabajo No Iniciado", "Empresa A", "Servicio de mantenimiento", "FAC001", "Cancelado", "2023-10-01"),
            ("OC002", "En Proceso", "Empresa B", "Desarrollo de software", "FAC002", "Pendiente", "2023-09-15"),
            ("OC003", "Completado Parcialmente", "Empresa C", "Consultoría en TI", "FAC003", "No Cancelado", "2023-08-30"),
            ("OC004", "Finalizado", "Empresa D", "Instalación de redes", "FAC004", "No Pagado", "2023-07-20"),
            ("OC005", "Completado", "Empresa E", "Auditoría de sistemas", "FAC005", "Pagado", "2023-06-18"),
            ("OC006", "En Proceso", "Empresa F", "Migración de datos", "FAC006", "Pendiente", "2023-05-22"),
            ("OC007", "Pendiente", "Empresa G", "Optimización de procesos", "FAC007", "No Pagado", "2023-04-10"),
            ("OC008", "Completado", "Empresa H", "Soporte técnico", "FAC008", "Pagado", "2023-03-15"),
            ("OC009", "En Proceso", "Empresa I", "Desarrollo web", "FAC009", "Pendiente", "2023-02-25"),
            ("OC010", "Pendiente", "Empresa J", "Evaluación de seguridad", "FAC010", "No Pagado", "2023-01-30"),
            ("OC011", "Completado", "Empresa K", "Diseño gráfico", "FAC011", "Pagado", "2023-11-02"),
            ("OC012", "En Proceso", "Empresa L", "Análisis de datos", "FAC012", "Pendiente", "2023-10-18"),
            ("OC013", "Pendiente", "Empresa M", "Capacitación de personal", "FAC013", "No Pagado", "2023-09-05"),
            ("OC014", "Completado", "Empresa N", "Optimización de redes", "FAC014", "Pagado", "2023-08-12"),
            ("OC015", "Pendiente", "Empresa O", "Desarrollo de app móvil", "FAC015", "No Pagado", "2023-07-28"),
            ("OC016", "Completado", "Empresa P", "Soporte en ciberseguridad", "FAC016", "Pagado", "2023-07-14"),
            ("OC017", "En Proceso", "Empresa Q", "Automatización de procesos", "FAC017", "Pendiente", "2023-06-20"),
            ("OC018", "Pendiente", "Empresa R", "Asesoría en transformación digital", "FAC018", "No Pagado", "2023-06-05"),
            ("OC019", "Completado", "Empresa S", "Administración de sistemas", "FAC019", "Pagado", "2023-05-23"),
            ("OC020", "Pendiente", "Empresa T", "Desarrollo de contenido", "FAC020", "No Pagado", "2023-04-18"),
            ("OC021", "En Proceso", "Empresa U", "Consultoría en recursos humanos", "FAC021", "Pendiente", "2023-03-15"),
            ("OC022", "Completado", "Empresa V", "Servicios de marketing digital", "FAC022", "Pagado", "2023-02-25"),
            ("OC023", "Pendiente", "Empresa W", "Servicios de traducción", "FAC023", "No Pagado", "2023-02-10"),
            ("OC024", "Completado", "Empresa X", "Evaluación financiera", "FAC024", "Pagado", "2023-01-31"),
            ("OC025", "Pendiente", "Empresa Y", "Investigación de mercado", "FAC025", "No Pagado", "2023-01-20"),
        ]

        ejemplos_mostrados = ejemplos[:18]
        
        for dato in ejemplos_mostrados:
            tree.insert("", "end", values=dato)

    def abrir_ventana_cotizacion(self):
        gen_cot = tk.Toplevel(root)
        generator_cot(root, gen_cot)


if __name__ == "__main__":
    root = tk.Tk()
    app = ventana_inicio(root)
    root.mainloop()