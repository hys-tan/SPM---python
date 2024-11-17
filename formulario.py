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

    # PREGUNTA ELIMINAR FILA
    def quest_mat(self):
        q_material=tk.Toplevel(self.parent)
        q_material.title("")
        q_material.geometry("300x110")
        q_material.resizable(False, False)
        q_material.configure(bg="#FFFFFF")
        q_material.grab_set()
        utils.centrar_ventana(q_material)
        q_material.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_ques_mat = tk.Canvas(q_material, width=300, height=110, bg="#FFFFFF", highlightthickness=0)
        canvas_ques_mat.pack()

        icon_quest_mat = tk.PhotoImage(file="SPM---python/icons/alert.png")
        canvas_ques_mat.create_image(30, 17, anchor="nw", image=icon_quest_mat)
        canvas_ques_mat.image = icon_quest_mat

        utils.create_rounded_rectangle(canvas_ques_mat, 0, 66, 300, 110, radius=0, fill="#EEEEE4", outline="#EEEEE4")
        
        canvas_ques_mat.create_text(79, 19, text="¿Estás seguro de que deseas", anchor="nw", font=("Arial", 10), fill="Black")
        canvas_ques_mat.create_text(115, 33, text="eliminar esta fila?", anchor="nw", font=("Arial", 10), fill="Black")
        
        btn_qm_si = tk.Button(q_material, text="Si", width=9, height=1, font=("Raleway", 9))
        btn_qm_si.place(x=73, y=73)

        btn_qm_no = tk.Button(q_material, text="No", width=9, height=1, font=("Raleway", 9), command=q_material.destroy)
        btn_qm_no.place(x=158, y=73)

    # FILA ELIMINADA
    def material_delete(self):
        mat_delete=tk.Toplevel(self.parent)
        mat_delete.title("")
        mat_delete.geometry("300x110")
        mat_delete.resizable(False, False)
        mat_delete.configure(bg="#FFFFFF")
        mat_delete.grab_set()
        utils.centrar_ventana(mat_delete)
        mat_delete.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_mat_delete = tk.Canvas(mat_delete, width=300, height=110, bg="#FFFFFF", highlightthickness=0)
        canvas_mat_delete.pack()
        
        icon_confirm_del = tk.PhotoImage(file="SPM---python/icons/confirm.png")
        canvas_mat_delete.create_image(30, 17, anchor="nw", image=icon_confirm_del)
        canvas_mat_delete.image = icon_confirm_del
        
        utils.create_rounded_rectangle(canvas_mat_delete, 0, 66, 300, 110, radius=0, fill="#EEEEE4", outline="#EEEEE4")
        
        canvas_mat_delete.create_text(85, 26, text="Fila eliminada exitosamente", anchor="nw", font=("Arial", 10), fill="Black")
        
        btn_md_ok = tk.Button(mat_delete, text="Aceptar", width=9, height=1, font=("Raleway", 9), command=mat_delete.destroy)
        btn_md_ok.place(x=115, y=73)
    
    # GENERAR COTIZACION
    def generator_cotizacion(self):
        gener_coti=tk.Toplevel(self.parent)
        gener_coti.title("")
        gener_coti.geometry("300x110")
        gener_coti.resizable(False, False)
        gener_coti.configure(bg="#FFFFFF")
        gener_coti.grab_set()
        utils.centrar_ventana(gener_coti)
        gener_coti.protocol("WM_DELETE_WINDOW", lambda: None)
        
        can_gen_coti = tk.Canvas(gener_coti, width=300, height=110, bg="#FFFFFF", highlightthickness=0)
        can_gen_coti.pack()
        
        icon_gener_coti = tk.PhotoImage(file="SPM---python/icons/question.png")
        can_gen_coti.create_image(30, 17, anchor="nw", image=icon_gener_coti)
        can_gen_coti.image = icon_gener_coti
        
        utils.create_rounded_rectangle(can_gen_coti, 0, 66, 300, 110, radius=0, fill="#EEEEE4", outline="#EEEEE4")
        
        can_gen_coti.create_text(79, 26, text="¿Desea generar la cotización?", anchor="nw", font=("Arial", 10), fill="Black")
        
        btn_gc_si = tk.Button(gener_coti, text="Si", width=9, height=1, font=("Raleway", 9))
        btn_gc_si.place(x=73, y=73)

        btn_gc_no = tk.Button(gener_coti, text="No", width=9, height=1, font=("Raleway", 9), command=gener_coti.destroy)
        btn_gc_no.place(x=158, y=73)
    
    # CANCELAR COTIZACION
    def cancelar_cotizacion(self):
        cancel_coti=tk.Toplevel(self.parent)
        cancel_coti.title("")
        cancel_coti.geometry("300x110")
        cancel_coti.resizable(False, False)
        cancel_coti.configure(bg="#FFFFFF")
        cancel_coti.grab_set()
        utils.centrar_ventana(cancel_coti)
        cancel_coti.protocol("WM_DELETE_WINDOW", lambda: None)
        
        can_cancel_coti = tk.Canvas(cancel_coti, width=300, height=110, bg="#FFFFFF", highlightthickness=0)
        can_cancel_coti.pack()
        
        icon_cancel_coti = tk.PhotoImage(file="SPM---python/icons/alert.png")
        can_cancel_coti.create_image(30, 17, anchor="nw", image=icon_cancel_coti)
        can_cancel_coti.image = icon_cancel_coti
        
        utils.create_rounded_rectangle(can_cancel_coti, 0, 66, 300, 110, radius=0, fill="#EEEEE4", outline="#EEEEE4")
        
        can_cancel_coti.create_text(79, 26, text="¿Desea cancelar la cotización?", anchor="nw", font=("Arial", 10), fill="Black")
        
        btn_cc_si = tk.Button(cancel_coti, text="Si", width=9, height=1, font=("Raleway", 9))
        btn_cc_si.place(x=73, y=73)

        btn_cc_no = tk.Button(cancel_coti, text="No", width=9, height=1, font=("Raleway", 9), command=cancel_coti.destroy)
        btn_cc_no.place(x=158, y=73)
    
    # CAMBIOS REALIZADOS
    def cambios_realizados(self):
        cambios_confirm=tk.Toplevel(self.parent)
        cambios_confirm.title("")
        cambios_confirm.geometry("300x110")
        cambios_confirm.resizable(False, False)
        cambios_confirm.configure(bg="#FFFFFF")
        cambios_confirm.grab_set()
        utils.centrar_ventana(cambios_confirm)
        cambios_confirm.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_camb_confirm = tk.Canvas(cambios_confirm, width=300, height=110, bg="#FFFFFF", highlightthickness=0)
        canvas_camb_confirm.pack()
        
        icon_confirm_cambio = tk.PhotoImage(file="SPM---python/icons/confirm.png")
        canvas_camb_confirm.create_image(30, 17, anchor="nw", image=icon_confirm_cambio)
        canvas_camb_confirm.image = icon_confirm_cambio
        
        utils.create_rounded_rectangle(canvas_camb_confirm, 0, 66, 300, 110, radius=0, fill="#EEEEE4", outline="#EEEEE4")
        
        canvas_camb_confirm.create_text(80, 26, text="Cambios realizados con éxtio", anchor="nw", font=("Arial", 10), fill="Black")
        
        btn_cr_ok = tk.Button(cambios_confirm, text="Aceptar", width=9, height=1, font=("Raleway", 9), command=cambios_confirm.destroy)
        btn_cr_ok.place(x=115, y=73)

    # CONFIRMACION DE CONTIZACION GENERADA
    def confirmacion_cotizacion(self):
        coti_confirm=tk.Toplevel(self.parent)
        coti_confirm.title("")
        coti_confirm.geometry("300x110")
        coti_confirm.resizable(False, False)
        coti_confirm.configure(bg="#FFFFFF")
        coti_confirm.grab_set()
        utils.centrar_ventana(coti_confirm)
        coti_confirm.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_coti_confirm = tk.Canvas(coti_confirm, width=300, height=110, bg="#FFFFFF", highlightthickness=0)
        canvas_coti_confirm.pack()
        
        icon_confirm_coti = tk.PhotoImage(file="SPM---python/icons/confirm.png")
        canvas_coti_confirm.create_image(30, 17, anchor="nw", image=icon_confirm_coti)
        canvas_coti_confirm.image = icon_confirm_coti
        
        utils.create_rounded_rectangle(canvas_coti_confirm, 0, 66, 300, 110, radius=0, fill="#EEEEE4", outline="#EEEEE4")
        
        canvas_coti_confirm.create_text(93, 26, text="Cotización generada", anchor="nw", font=("Arial", 10), fill="Black")
        
        btn_coti_gen = tk.Button(coti_confirm, text="Aceptar", width=9, height=1, font=("Raleway", 9), command=coti_confirm.destroy)
        btn_coti_gen.place(x=115, y=73)

    # COMPLETE LOS DATOS
    def question_datos(self):
        quest_datos=tk.Toplevel(self.parent)
        quest_datos.title("")
        quest_datos.geometry("300x110")
        quest_datos.resizable(False, False)
        quest_datos.configure(bg="#FFFFFF")
        quest_datos.grab_set()
        utils.centrar_ventana(quest_datos)
        quest_datos.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_quest_datos = tk.Canvas(quest_datos, width=300, height=110, bg="#FFFFFF", highlightthickness=0)
        canvas_quest_datos.pack()
        
        icon_quest_datos = tk.PhotoImage(file="SPM---python/icons/alert.png")
        canvas_quest_datos.create_image(30, 17, anchor="nw", image=icon_quest_datos)
        canvas_quest_datos.image = icon_quest_datos
        
        utils.create_rounded_rectangle(canvas_quest_datos, 0, 66, 300, 110, radius=0, fill="#EEEEE4", outline="#EEEEE4")
        
        canvas_quest_datos.create_text(84, 19, text="Por favor, complete todos", anchor="nw", font=("Arial", 10), fill="Black")
        canvas_quest_datos.create_text(125, 33, text="los datos", anchor="nw", font=("Arial", 10), fill="Black")
        
        btn_qd_ok = tk.Button(quest_datos, text="Aceptar", width=9, height=1, font=("Raleway", 9), command=quest_datos.destroy)
        btn_qd_ok.place(x=115, y=73)

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
        
        
        canvas_coti.create_text(20, 20, text="Nro de Cotización", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 20, 38, 170, 68, radius=10, fill="white", outline="#959595")
        input_gcoti = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gcoti.place(x=25, y=43, width=140, height=20)
        
        canvas_coti.create_text(180, 20, text="Fecha", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 180, 38, 360, 68, radius=10, fill="white", outline="#959595")
        input_gfecha = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gfecha.place(x=185, y=43, width=170, height=20)
        
        canvas_coti.create_text(370, 20, text="Cliente / Empresa", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 370, 38, 570, 68, radius=10, fill="white", outline="#959595")
        input_gpersona = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gpersona.place(x=375, y=43, width=190, height=20)
        
        canvas_coti.create_text(580, 20, text="Área", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        cbo_area = ttk.Combobox(gen_cot, values=["Escoja una Opción", "Ejemplo1"], state="readonly", font=("Raleway", 10))
        cbo_area.place(x=580, y=38, width=150, height=31)
        cbo_area.current(0)
        
        
        canvas_coti.create_text(20, 78, text="Persona de Contacto", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        cbo_persona = ttk.Combobox(gen_cot, values=["Escoja una Opción", "Ejemplo1"], state="readonly", font=("Raleway", 10))
        cbo_persona.place(x=20, y=96, width=230, height=31)
        cbo_persona.current(0)
        
        canvas_coti.create_text(260, 78, text="Título del Servicio", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 260, 96, 730, 126, radius=10, fill="white", outline="#959595")
        input_gtitulo = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gtitulo.place(x=265, y=101, width=460, height=20)
        
        
        canvas_coti.create_text(20, 136, text="Tiempo de Ejecución", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 20, 154, 290, 184, radius=10, fill="white", outline="#959595")
        input_gtiempo = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gtiempo.place(x=25, y=159, width=260, height=20)
        
        canvas_coti.create_text(300, 136, text="Forma de Pago", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 300, 154, 540, 184, radius=10, fill="white", outline="#959595")
        input_gpago = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gpago.place(x=305, y=159, width=230, height=20)
        
        canvas_coti.create_text(550, 136, text="IGV", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        cbo_igv = ttk.Combobox(gen_cot, values=["SI", "NO"], state="readonly", font=("Raleway", 10))
        cbo_igv.place(x=550, y=154, width=50, height=31)
        cbo_igv.current(0)
        
        canvas_coti.create_text(610, 136, text="Tipo de Moneda", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        cbo_moneda = ttk.Combobox(gen_cot, values=["PEN", "USD"], state="readonly", font=("Raleway", 10))
        cbo_moneda.place(x=610, y=154, width=120, height=31)
        cbo_moneda.current(0)
        
        canvas_coti.create_text(20, 194, text="Tipo de Cuenta", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        cbo_cuenta = ttk.Combobox(gen_cot, values=["Cuenta Soles", "Cuenta Dólares"], state="readonly", font=("Raleway", 10))
        cbo_cuenta.place(x=20, y=212, width=145, height=31)
        cbo_cuenta.current(0)
        
        canvas_coti.create_text(176, 194, text="Nro de Cuenta", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 176, 212, 446, 242, radius=10, fill="white", outline="#959595")
        input_gcuenta = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gcuenta.place(x=181, y=217, width=260, height=20)
        
        canvas_coti.create_text(456, 194, text="Cuenta Interbancaria", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 456, 212, 730, 242, radius=10, fill="white", outline="#959595")
        input_gcuentabanc = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gcuentabanc.place(x=461, y=217, width=264, height=20)
        
        
        canvas_coti.create_text(20, 272, text="Descripción", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 20, 290, 730, 320, radius=10, fill="white", outline="#959595")
        input_gdesc = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gdesc.place(x=25, y=295, width=700, height=20)
        
        canvas_coti.create_text(20, 330, text="Material(es)", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 20, 348, 420, 378, radius=10, fill="white", outline="#959595")
        input_gmaterial = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gmaterial.place(x=25, y=353, width=390, height=20)
        
        canvas_coti.create_text(430, 330, text="Unidad(es)", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 430, 348, 485, 378, radius=10, fill="white", outline="#959595")
        input_gunidad = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gunidad.place(x=435, y=353, width=45, height=20)
        cbo_unidad = ttk.Combobox(gen_cot, values=["JUEGO", "PIEZA"], state="readonly", font=("Raleway", 10))
        cbo_unidad.place(x=495, y=348, width=100, height=31)
        cbo_unidad.current(0)
        
        canvas_coti.create_text(605, 330, text="Precio Unit.", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 605, 348, 730, 378, radius=10, fill="white", outline="#959595")
        input_gpreciou = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gpreciou.place(x=610, y=353, width=115, height=20)
        
        
        canvas_coti.create_text(20, 606, text="Dscto. (%)", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 20, 624, 130, 654, radius=10, fill="white", outline="#959595")
        input_gdescuento = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gdescuento.place(x=25, y=629, width=100, height=20)
        
        canvas_coti.create_text(260, 606, text="SubTotal", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 260, 624, 370, 654, radius=10, fill="white", outline="#959595")
        input_gsubtot = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gsubtot.place(x=265, y=629, width=100, height=20)
        
        canvas_coti.create_text(380, 606, text="IGV", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 380, 624, 490, 654, radius=10, fill="white", outline="#959595")
        input_gigv = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gigv.place(x=385, y=629, width=100, height=20)
        
        canvas_coti.create_text(500, 606, text="Dscto.", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 500, 624, 610, 654, radius=10, fill="white", outline="#959595")
        input_gdescto = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gdescto.place(x=505, y=629, width=100, height=20)
        
        canvas_coti.create_text(620, 606, text="Total", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_coti, 620, 624, 730, 654, radius=10, fill="white", outline="#959595")
        input_gtotal = tk.Entry(gen_cot, font=("Arial", 11), bd=0)
        input_gtotal.place(x=625, y=629, width=100, height=20)
        
        
        btn_ag = tk.Button(gen_cot, text="Agregar", width=13, height=1, font=("Raleway", 9))
        btn_ag.place(x=10, y=398)
        
        btn_ed = tk.Button(gen_cot, text="Editar", width=13, height=1, font=("Raleway", 9), command=self.editar_material)
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
        ed_material.grab_set()
        utils.centrar_ventana(ed_material)
        ed_material.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_mat = tk.Canvas(ed_material, width=600, height=186, bg="#373737", highlightthickness=0)
        canvas_mat.pack()
        
        utils.create_rounded_rectangle(canvas_mat, 10, 10, 590, 136, radius=10, fill="#959595", outline="#959595")
        
        canvas_mat.create_text(20, 20, text="Descripción", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_mat, 20, 38, 300, 68, radius=10, fill="white", outline="#959595")
        inpt_ed_desc = tk.Entry(ed_material, font=("Arial", 11), bd=0)
        inpt_ed_desc.place(x=25, y=43, width=270, height=20)
        
        canvas_mat.create_text(310, 20, text="Material", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_mat, 310, 38, 580, 68, radius=10, fill="white", outline="#959595")
        inpt_ed_mat = tk.Entry(ed_material, font=("Arial", 11), bd=0)
        inpt_ed_mat.place(x=315, y=43, width=260, height=20)
    
        canvas_mat.create_text(20, 78, text="Unidad(es)", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_mat, 20, 96, 90, 126, radius=10, fill="white", outline="#959595")
        inpt_ed_unidad = tk.Entry(ed_material, font=("Arial", 11), bd=0)
        inpt_ed_unidad.place(x=25, y=101, width=60, height=20)
        cbo_ed_unidad = ttk.Combobox(ed_material, values=["JUEGO", "PIEZA"], state="readonly", font=("Raleway", 10))
        cbo_ed_unidad.place(x=100, y=96, width=90, height=31)
        cbo_ed_unidad.current(0)
        
        canvas_mat.create_text(200, 78, text="Precio Unit.", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_mat, 200, 96, 330, 126, radius=10, fill="white", outline="#959595")
        inpt_ed_precio = tk.Entry(ed_material, font=("Arial", 11), bd=0)
        inpt_ed_precio.place(x=205, y=101, width=120, height=20)
        
        canvas_mat.create_text(340, 78, text="Sub Total", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_mat, 340, 96, 470, 126, radius=10, fill="white", outline="#959595")
        inpt_ed_total = tk.Entry(ed_material, font=("Arial", 11), bd=0)
        inpt_ed_total.place(x=345, y=101, width=120, height=20)
        
        btn_ed_canc = tk.Button(ed_material, text="Cancelar", width=15, height=1, font=("Raleway", 9), command=ed_material.destroy)
        btn_ed_canc.place(x=10, y=146)

        btn_ed_save = tk.Button(ed_material, text="Guardar", width=15, height=1, font=("Raleway", 9))
        btn_ed_save.place(x=134, y=146)

class clientes:
    def __init__(self, root, vent_clientes):
        
        self.root = root
        self.vent_clientes = vent_clientes
        self.root.withdraw()
        
        self.vent_clientes = vent_clientes
        self.vent_clientes.title("Registro de Clientes")
        self.vent_clientes.geometry("978x458")
        self.vent_clientes.resizable(False, False)
        self.vent_clientes.configure(bg="#373737")
        utils.centrar_ventana(self.vent_clientes)
        
        self.alerta = alertas(vent_clientes)

        self.vent_clientes.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_cliente = tk.Canvas(vent_clientes, width=978, height=458, bg="#373737", highlightthickness=0)
        canvas_cliente.pack()
        
        utils.create_rounded_rectangle(canvas_cliente, 10, 10, 300, 314, radius=10, fill="#959595", outline="#959595")
        utils.create_rounded_rectangle(canvas_cliente, 10, 324, 300, 448, radius=10, fill="#959595", outline="#959595")
        #utils.create_rounded_rectangle(canvas_cliente, 310, 80, 968, 408, radius=10, fill="#959595", outline="#959595")
        
        canvas_cliente.create_text(20, 22, text="Opciones", anchor="nw", font=("Raleway", 20, "bold"), fill="White")
        
        btn_reg_cli = tk.Button(vent_clientes, text="Registrar Cliente", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white", command=self.registrar_cliente)
        btn_reg_cli.place(x=22, y=80)
        
        btn_ed_cli = tk.Button(vent_clientes, text="Editar cliente", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_ed_cli.place(x=22, y=125)
        
        btn_menu = tk.Button(vent_clientes, text="Volver al inicio", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_menu.place(x=22, y=170)
        
        btn_sig_cli = tk.Button(vent_clientes, text="Siguiente", width=13, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_sig_cli.place(x=868, y=418)
        
        btn_atras_cli = tk.Button(vent_clientes, text="Anterior", width=13, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_atras_cli.place(x=758, y=418)
        
        canvas_cliente.create_text(20, 336, text="Filtros", anchor="nw", font=("Raleway", 20, "bold"), fill="White")
        
        canvas_cliente.create_text(20, 390, text="Por fecha", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        
        cbo_date = ttk.Combobox(vent_clientes, values=["Todos los registros", "Última semana", "Últimas 2 semanas", "Último mes", "Últimos 3 meses", "Últimos 6 meses", "Último año"], state="readonly", font=("Raleway", 10))
        cbo_date.place(x=20, y=408, width=250, height=30)
        cbo_date.current(0)
        
        canvas_cliente.create_text(385, 22, text="REGISTRO DE CLIENTES", anchor="nw", font=("Raleway", 20, "bold"), fill="White")
        
        search_canvas_cliente = tk.Canvas(vent_clientes, width=191, height=40, bg="#373737", highlightthickness=0)
        search_canvas_cliente.place(x=777, y=20)
                
        utils.create_rounded_rectangle(search_canvas_cliente, 0, 0, 191, 40, radius=10, fill="white", outline="gray")
        search_canvas_cliente.create_line(156, 7, 156, 34, fill="gray", width=2)
                
        search_icon_cliente = tk.PhotoImage(file="SPM---python/icons/loupe.png")
        search_icon_id_cliente = search_canvas_cliente.create_image(162, 8, anchor="nw", image=search_icon_cliente)
        search_canvas_cliente.image = search_icon_cliente
                
        search_canvas_cliente.tag_bind(search_icon_id_cliente, "<Button-1>", lambda e: self.alerta.no_datos())
                
        search_entry_cliente = tk.Entry(search_canvas_cliente, font=("Arial", 13), width=40, bd=0, relief="flat", fg='grey')
        search_entry_cliente.insert(0, "Buscar...")
        search_entry_cliente.bind("<FocusIn>", lambda event: utils.clear_placeholder(event, search_entry_cliente))
        search_entry_cliente.bind("<FocusOut>", lambda event: utils.placeholder_search(event, search_entry_cliente))
        search_entry_cliente.place(x=6, y=7, width=142, height=27)
        
        cbo_page_cliente = ttk.Combobox(vent_clientes, values=["1", "2"], state="readonly", font=("Arial", 10))
        cbo_page_cliente.place(x=310, y=418, width=70, height=30)
        cbo_page_cliente.current(0)

        t_cliente = ttk.Treeview(vent_clientes, columns=("id", "razon", "ruc", "fecha",), show="headings", style="Custom.Treeview")
        t_cliente.place(x=310, y=80, width=659, height=329)
        
        t_cliente.heading("id", text="ID")
        t_cliente.heading("razon", text="Razón Social / Cliente / Empresa")
        t_cliente.heading("ruc", text="RUC / DNI")
        t_cliente.heading("fecha", text="Fecha")
        
        t_cliente.column("id", anchor="center", width=50, stretch=False)
        t_cliente.column("razon", anchor="center", width=395, stretch=False)
        t_cliente.column("ruc", anchor="center", width=110, stretch=False)
        t_cliente.column("fecha", anchor="center", width=100, stretch=False)
        
        datos_clientes = [
            ("1", "Empresa ABC S.A.", "20123456789", "2023-11-01"),
            ("2", "Constructora XYZ", "10456789012", "2023-10-15"),
            ("3", "Servicios Industriales S.R.L.", "20345678901", "2023-09-22"),
            ("4", "Distribuidora Pérez", "10432109876", "2023-08-30"),
            ("5", "Inversiones López S.A.C.", "20567890123", "2023-07-19"),
            ("6", "Transportes Rojas", "10321098765", "2023-06-25"),
            ("7", "Tecnología Avanzada S.A.", "20198765432", "2023-05-14"),
            ("8", "Comercializadora García", "10456789023", "2023-04-07"),
            ("9", "Consultores Martínez S.A.", "20456789123", "2023-03-29"),
            ("10", "Agroindustria Chávez", "20543210987", "2023-02-18"),
            ("11", "Corporación Rivera", "10321987654", "2023-01-09"),
            ("12", "Soluciones Globales S.A.C.", "20345678901", "2022-12-11"),
            ("13", "Proyectos Vega", "10456789021", "2022-11-22"),
            ("14", "Servicios Integrales Torres", "20123456780", "2022-10-05"),
            ("15", "Constructora Lima S.A.C.", "20432109876", "2022-09-17"),
        ]

        ejemplos_clientes = datos_clientes[:10]
        
        for cliente in ejemplos_clientes:
            t_cliente.insert("", "end", values=cliente)
        
    def registrar_cliente(self):
        
        self.vent_clientes.withdraw()
        
        reg_cliente = tk.Toplevel(self.vent_clientes)
        reg_cliente.title("Registro de Cliente")
        reg_cliente.geometry("710x502")
        reg_cliente.resizable(False, False)
        reg_cliente.configure(bg="#373737")
        utils.centrar_ventana(reg_cliente)

        reg_cliente.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_reg_cli = tk.Canvas(reg_cliente, width=710, height=502, bg="#373737", highlightthickness=0)
        canvas_reg_cli.pack()
        
        utils.create_rounded_rectangle(canvas_reg_cli, 10, 10, 350, 136, radius=10, fill="#959595", outline="#959595")
        utils.create_rounded_rectangle(canvas_reg_cli, 10, 146, 350, 254, radius=10, fill="#959595", outline="#959595")
        #utils.create_rounded_rectangle(canvas_reg_cli, 10, 264, 350, 412, radius=10, fill="#959595", outline="#959595")
        utils.create_rounded_rectangle(canvas_reg_cli, 360, 10, 700, 118, radius=10, fill="#959595", outline="#959595")
        #utils.create_rounded_rectangle(canvas_reg_cli, 360, 128, 700, 246, radius=10, fill="#959595", outline="#959595")
        utils.create_rounded_rectangle(canvas_reg_cli, 360, 256, 700, 364, radius=10, fill="#959595", outline="#959595")
        #utils.create_rounded_rectangle(canvas_reg_cli, 360, 374, 700, 492, radius=10, fill="#959595", outline="#959595")
        
        canvas_reg_cli.create_text(20, 20, text="Razón Social / Empresa / Cliente", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_reg_cli, 20, 38, 340, 68, radius=10, fill="white", outline="#959595")
        reg_rs_cli = tk.Entry(reg_cliente, font=("Arial", 11), bd=0)
        reg_rs_cli.place(x=25, y=43, width=310, height=20)
        
        canvas_reg_cli.create_text(20, 78, text="RUC", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_reg_cli, 20, 96, 340, 126, radius=10, fill="white", outline="#959595")
        reg_ruc_cli = tk.Entry(reg_cliente, font=("Arial", 11), bd=0)
        reg_ruc_cli.place(x=25, y=101, width=310, height=20)
        
        canvas_reg_cli.create_text(20, 156, text="Persona de Contacto", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_reg_cli, 20, 174, 340, 204, radius=10, fill="white", outline="#959595")
        reg_persona = tk.Entry(reg_cliente, font=("Arial", 11), bd=0)
        reg_persona.place(x=25, y=179, width=310, height=20)
        
        canvas_reg_cli.create_text(370, 20, text="Área de Trabajo", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_reg_cli, 370, 38, 690, 68, radius=10, fill="white", outline="#959595")
        reg_ar_tb = tk.Entry(reg_cliente, font=("Arial", 11), bd=0)
        reg_ar_tb.place(x=375, y=43, width=310, height=20)

        canvas_reg_cli.create_text(370, 266, text="Dirección", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_reg_cli, 370, 284, 690, 314, radius=10, fill="white", outline="#959595")
        reg_direx = tk.Entry(reg_cliente, font=("Arial", 11), bd=0)
        reg_direx.place(x=375, y=289, width=310, height=20)
        
        btn_ag_persona = tk.Button(reg_cliente, text="Agregar", width=13, height=1, font=("Raleway", 9))
        btn_ag_persona.place(x=20, y=214)
        
        btn_ed_persona = tk.Button(reg_cliente, text="Editar", width=13, height=1, font=("Raleway", 9), command=self.edit_persona_cont)
        btn_ed_persona.place(x=130, y=214)
        
        btn_del_persona = tk.Button(reg_cliente, text="Eliminar", width=13, height=1, font=("Raleway", 9))
        btn_del_persona.place(x=240, y=214)
        
        
        btn_ag_trabajo = tk.Button(reg_cliente, text="Agregar", width=13, height=1, font=("Raleway", 9))
        btn_ag_trabajo.place(x=370, y=78)
        
        btn_ed_trabajo = tk.Button(reg_cliente, text="Editar", width=13, height=1, font=("Raleway", 9), command=self.edit_area_trabajo)
        btn_ed_trabajo.place(x=480, y=78)
        
        btn_del_trabajo = tk.Button(reg_cliente, text="Eliminar", width=13, height=1, font=("Raleway", 9))
        btn_del_trabajo.place(x=590, y=78)
        
        
        btn_ag_direx = tk.Button(reg_cliente, text="Agregar", width=13, height=1, font=("Raleway", 9))
        btn_ag_direx.place(x=370, y=324)
        
        btn_ed_direx = tk.Button(reg_cliente, text="Editar", width=13, height=1, font=("Raleway", 9), command=self.edit_direx)
        btn_ed_direx.place(x=480, y=324)
        
        btn_del_direx = tk.Button(reg_cliente, text="Eliminar", width=13, height=1, font=("Raleway", 9))
        btn_del_direx.place(x=590, y=324)
        
        
        btn_canc = tk.Button(reg_cliente, text="Cancelar", width=13, height=1, font=("Raleway", 9))
        btn_canc.place(x=75, y=462)

        btn_gen = tk.Button(reg_cliente, text="Registrar", width=13, height=1, font=("Raleway", 9))
        btn_gen.place(x=185, y=462)
        
        
        t_persona = ttk.Treeview(reg_cliente, columns=("id_p", "persona"), show="headings", style="Custom.Treeview")
        t_persona.place(x=10, y=264, width=341, height=149)
        
        t_persona.heading("id_p", text="ID")
        t_persona.heading("persona", text="Persona de contacto")
        t_persona.column("id_p", anchor="center", width=35, stretch=False)
        t_persona.column("persona", anchor="center", width=290, stretch=False)
        
        datos_t_persona = [
            ("1", "Carlos Rodríguez"),
            ("2", "María López"),
            ("3", "Javier Martínez"),
            ("4", "Ana Fernández"),
            ("5", "Luis Gómez"),
        ]

        for persona in datos_t_persona:
            t_persona.insert("", "end", values=persona)
        
        scrollbar_t_persona = ttk.Scrollbar(reg_cliente, orient="vertical", command=t_persona.yview)
        t_persona.configure(yscrollcommand=scrollbar_t_persona.set)
        scrollbar_t_persona.place(x=337, y=264, height=149)
        
        
        t_area = ttk.Treeview(reg_cliente, columns=("id_a", "area"), show="headings", style="Custom.Treeview")
        t_area.place(x=360, y=128, width=341, height=119)
        
        t_area.heading("id_a", text="ID")
        t_area.heading("area", text="Área de trabajo")
        t_area.column("id_a", anchor="center", width=35, stretch=False)
        t_area.column("area", anchor="center", width=290, stretch=False)
        
        datos_t_area = [
            ("1", "Recursos Humanos"),
            ("2", "Desarrollo de Software"),
            ("3", "Marketing"),
            ("4", "Finanzas"),
            ("5", "Logística")
        ]

        for dato in datos_t_area:
            t_area.insert("", "end", values=dato)
        
        scrollbar_t_area = ttk.Scrollbar(reg_cliente, orient="vertical", command=t_area.yview)
        t_area.configure(yscrollcommand=scrollbar_t_area.set)
        scrollbar_t_area.place(x=687, y=128, height=119)


        t_direx = ttk.Treeview(reg_cliente, columns=("id_d", "direx"), show="headings", style="Custom.Treeview")
        t_direx.place(x=360, y=374, width=341, height=119)
        
        t_direx.heading("id_d", text="ID")
        t_direx.heading("direx", text="Dirección")
        t_direx.column("id_d", anchor="center", width=35, stretch=False)
        t_direx.column("direx", anchor="center", width=290, stretch=False)
        
        datos_t_direx = [
            ("1", "Av. Los Olivos 123, Lima"),
            ("2", "Jr. San Martín 456, Arequipa"),
            ("3", "Calle Las Rosas 789, Cusco"),
            ("4", "Av. El Sol 321, Trujillo"),
            ("5", "Jr. Amazonas 654, Piura")
        ]
        
        for dato in datos_t_direx:
            t_direx.insert("", "end", values=dato)
        
        scrollbar_t_direx = ttk.Scrollbar(reg_cliente, orient="vertical", command=t_direx.yview)
        t_direx.configure(yscrollcommand=scrollbar_t_direx.set)
        scrollbar_t_direx.place(x=687, y=374, height=119)

    def edit_persona_cont(self):
        ed_pers = tk.Toplevel(self.vent_clientes)
        ed_pers.title("Editar Persona de Contacto")
        ed_pers.geometry("340x128")
        ed_pers.resizable(False, False)
        ed_pers.configure(bg="#373737")
        ed_pers.grab_set()
        utils.centrar_ventana(ed_pers)
        ed_pers.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_ed_pers = tk.Canvas(ed_pers, width=340, height=128, bg="#373737", highlightthickness=0)
        canvas_ed_pers.pack()
        
        utils.create_rounded_rectangle(canvas_ed_pers, 10, 10, 330, 78, radius=10, fill="#959595", outline="#959595")
        
        canvas_ed_pers.create_text(20, 20, text="Persona de Contacto", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_ed_pers, 20, 38, 320, 68, radius=10, fill="white", outline="#959595")
        inpt_ed_pers_con = tk.Entry(ed_pers, font=("Arial", 11), bd=0)
        inpt_ed_pers_con.place(x=25, y=43, width=290, height=20)
        
        btn_canc_pers = tk.Button(ed_pers, text="Cancelar", width=13, height=1, font=("Raleway", 9), command=ed_pers.destroy)
        btn_canc_pers.place(x=10, y=88)

        btn_save_pers = tk.Button(ed_pers, text="Guardar", width=13, height=1, font=("Raleway", 9))
        btn_save_pers.place(x=120, y=88)
        
    def edit_area_trabajo(self):
        ed_ar_trabajo = tk.Toplevel(self.vent_clientes)
        ed_ar_trabajo.title("Editar Área de Trabajo")
        ed_ar_trabajo.geometry("340x128")
        ed_ar_trabajo.resizable(False, False)
        ed_ar_trabajo.configure(bg="#373737")
        ed_ar_trabajo.grab_set()
        utils.centrar_ventana(ed_ar_trabajo)
        ed_ar_trabajo.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_ed_ar_trab = tk.Canvas(ed_ar_trabajo, width=340, height=128, bg="#373737", highlightthickness=0)
        canvas_ed_ar_trab.pack()

        utils.create_rounded_rectangle(canvas_ed_ar_trab, 10, 10, 330, 78, radius=10, fill="#959595", outline="#959595")
    
        canvas_ed_ar_trab.create_text(20, 20, text="Área de Trabajo", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_ed_ar_trab, 20, 38, 320, 68, radius=10, fill="white", outline="#959595")
        inpt_ed_ar_trab = tk.Entry(ed_ar_trabajo, font=("Arial", 11), bd=0)
        inpt_ed_ar_trab.place(x=25, y=43, width=290, height=20)
        
        btn_canc_ar_trab = tk.Button(ed_ar_trabajo, text="Cancelar", width=13, height=1, font=("Raleway", 9), command=ed_ar_trabajo.destroy)
        btn_canc_ar_trab.place(x=10, y=88)

        btn_save_ar_trab = tk.Button(ed_ar_trabajo, text="Guardar", width=13, height=1, font=("Raleway", 9))
        btn_save_ar_trab.place(x=120, y=88)
        
    def edit_direx(self):
        ed_direccion = tk.Toplevel(self.vent_clientes)
        ed_direccion.title("Editar Dirección")
        ed_direccion.geometry("340x128")
        ed_direccion.resizable(False, False)
        ed_direccion.configure(bg="#373737")
        ed_direccion.grab_set()
        utils.centrar_ventana(ed_direccion)
        ed_direccion.protocol("WM_DELETE_WINDOW", lambda: None)
        
        canvas_ed_direccion = tk.Canvas(ed_direccion, width=340, height=128, bg="#373737", highlightthickness=0)
        canvas_ed_direccion.pack()

        utils.create_rounded_rectangle(canvas_ed_direccion, 10, 10, 330, 78, radius=10, fill="#959595", outline="#959595")

        canvas_ed_direccion.create_text(20, 20, text="Dirección", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        utils.create_rounded_rectangle(canvas_ed_direccion, 20, 38, 320, 68, radius=10, fill="white", outline="#959595")
        inpt_ed_direx = tk.Entry(ed_direccion, font=("Arial", 11), bd=0)
        inpt_ed_direx.place(x=25, y=43, width=290, height=20)
    
        btn_canc_direx = tk.Button(ed_direccion, text="Cancelar", width=13, height=1, font=("Raleway", 9), command=ed_direccion.destroy)
        btn_canc_direx.place(x=10, y=88)

        btn_save_direx = tk.Button(ed_direccion, text="Guardar", width=13, height=1, font=("Raleway", 9))
        btn_save_direx.place(x=120, y=88)
    
    
    
        
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

        btn_reg_cli = tk.Button(root, text="Ver Registro de Clientes", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white", command=self.abrir_ventana_clientes)
        btn_reg_cli.place(x=22, y=125)

        btn_reg_cot = tk.Button(root, text="Ver Registro de Cotización", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_reg_cot.place(x=22, y=170)

        btn_reg_oc = tk.Button(root, text="Ver Registro de Orden de Compra", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_reg_oc.place(x=22, y=215)

        btn_reg_fact = tk.Button(root, text="Registrar Factura", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_reg_fact.place(x=22, y=260)

        btn_seg_fact = tk.Button(root, text="Seguimiento de Factura", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_seg_fact.place(x=22, y=305)

        btn_search = tk.Button(root, text="Buscar Documentos", width=37, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_search.place(x=22, y=350)

        btn_act = tk.Button(root, text="Actualizar Registro", width=37, height=1, font=("Raleway", 9), command=self.alerta.material_delete, activebackground="#7F7F7F", activeforeground="white")
        btn_act.place(x=22, y=395)

        btn_exit = tk.Button(self.root, text="Salir", width=37, height=1, font=("Raleway", 9), command=self.alerta.cerrar_prog, activebackground="#7F7F7F", activeforeground="white")
        btn_exit.place(x=22, y=440)
        
        btn_siguiente = tk.Button(root, text="Siguiente", width=13, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_siguiente.place(x=1290, y=660)
        
        btn_atras = tk.Button(root, text="Anterior", width=13, height=1, font=("Raleway", 9), activebackground="#7F7F7F", activeforeground="white")
        btn_atras.place(x=1180, y=660)

        # Vincular los eventos a cada botón
        for btn in [btn_gen_cot, btn_reg_cli, btn_reg_cot, btn_reg_oc, btn_reg_fact, btn_seg_fact, btn_search, btn_act, btn_exit, btn_siguiente, btn_atras]:
            btn.bind("<Enter>", lambda e, b=btn: utils.on_enter(b))
            btn.bind("<Leave>", lambda e, b=btn: utils.on_leave(b))

        canvas.create_text(20, 502, text="Filtros", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

        canvas.create_text(20, 560, text="Por Orden de Compra", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        
        cbo_oc = ttk.Combobox(root, values=["Todos los registros", "Trabajo No Iniciado", "En Proceso", "Completado Parcialmente", "Finalizado"], state="readonly", font=("Raleway", 10))
        cbo_oc.place(x=20, y=578, width=250, height=30)
        cbo_oc.current(0)

        canvas.create_text(20, 614, text="Por Factura", anchor="nw", font=("Raleway", 10, "bold"), fill="black")
        
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

    def abrir_ventana_clientes(self):
        vent_clientes = tk.Toplevel(root)
        clientes(root, vent_clientes)

if __name__ == "__main__":
    root = tk.Tk()
    app = ventana_inicio(root)
    root.mainloop()