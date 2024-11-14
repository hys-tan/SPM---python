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
        utils.create_rounded_rectangle(canvas, 310, 80, 1390, 650, radius=10, fill="#959595", outline="#959595")

        canvas.create_text(20, 22, text="Opciones", anchor="nw", font=("Raleway", 20, "bold"), fill="White")

        # Botones opcion
        btn_gen_cot = tk.Button(root, text="Generar Cotización", width=37, height=1, font=("Raleway", 9), activebackground="#373737", activeforeground="white")
        btn_gen_cot.place(x=22, y=80)

        btn_reg_cli = tk.Button(root, text="Ver Registro de Clientes", width=37, height=1, font=("Raleway", 9), activebackground="#373737", activeforeground="white")
        btn_reg_cli.place(x=22, y=125)

        btn_reg_cot = tk.Button(root, text="Ver Registro de Cotización", width=37, height=1, font=("Raleway", 9), activebackground="#373737", activeforeground="white")
        btn_reg_cot.place(x=22, y=170)

        btn_reg_oc = tk.Button(root, text="Ver Registro de Orden de Compra", width=37, height=1, font=("Raleway", 9), activebackground="#373737", activeforeground="white")
        btn_reg_oc.place(x=22, y=215)

        btn_reg_fact = tk.Button(root, text="Registrar Factura", width=37, height=1, font=("Raleway", 9), activebackground="#373737", activeforeground="white")
        btn_reg_fact.place(x=22, y=260)

        btn_seg_fact = tk.Button(root, text="Seguimiento de Factura", width=37, height=1, font=("Raleway", 9), command=self.alerta.seleccionar_fila, activebackground="#373737", activeforeground="white")
        btn_seg_fact.place(x=22, y=305)

        btn_search = tk.Button(root, text="Buscar Documentos", width=37, height=1, font=("Raleway", 9), activebackground="#373737", activeforeground="white")
        btn_search.place(x=22, y=350)

        btn_act = tk.Button(root, text="Actualizar Registro", width=37, height=1, font=("Raleway", 9), activebackground="#373737", activeforeground="white")
        btn_act.place(x=22, y=395)

        # Usar el método cerrar_prog de alertas para el botón de salida
        btn_exit = tk.Button(root, text="Salir", width=37, height=1, font=("Raleway", 9), command=self.alerta.cerrar_prog, activebackground="#373737", activeforeground="white")
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
        
        cbo_page = ttk.Combobox(root, values=["1", "2", "3", "4", "5"], state="readonly", font=("Arial", 10))
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
        
        

        
if __name__ == "__main__":
    root = tk.Tk()
    app = ventana_inicio(root)
    root.mainloop()