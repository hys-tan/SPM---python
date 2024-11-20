import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from tkcalendar import DateEntry
import os
import shutil
from tkinter import PhotoImage

def placeholder_search(event, entry):
    if entry.get() == "":
        entry.insert(0, "Buscar...")
        entry.config(fg='grey')

def clear_placeholder(event, entry):
    if entry.get() == "Buscar...":
        entry.delete(0, tk.END)
        entry.config(fg='black')



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

def ajustar_texto(texto, max_length=45):
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



def fade_color(start_color, end_color, steps, step_duration, button, is_background=True):
    """Función para hacer un fade de color."""
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color

    for step in range(steps + 1):
        r = int(r1 + (r2 - r1) * (step / steps))
        g = int(g1 + (g2 - g1) * (step / steps))
        b = int(b1 + (b2 - b1) * (step / steps))
        color = f'#{r:02x}{g:02x}{b:02x}'
        
        # Usa after para aplicar el color en cada paso
        button.after(step * step_duration, lambda c=color, b=button, bg=is_background: fade_color_step(c, b, bg))

def fade_color_step(color, button, is_background):
    """Actualiza el color del botón en un paso."""
    if is_background:
        button['background'] = color
    else:
        button['foreground'] = color

def on_enter(btn):
    # Cambia el color de fondo y texto al pasar el mouse
    fade_color((240, 240, 240), (85, 85, 85), 10, 10, btn, is_background=True)  # Fade del fondo
    fade_color((0, 0, 0), (255, 255, 255), 10, 10, btn, is_background=False)  # Fade del texto

def on_leave(btn):
    # Restaura el color de fondo y texto al salir el mouse
    fade_color((85, 85, 85), (240, 240, 240), 10, 10, btn, is_background=True)  # Fade del fondo
    fade_color((255, 255, 255), (0, 0, 0), 10, 10, btn, is_background=False)  # Fade del texto


def centrar_ventana(ventana):
    ventana.update_idletasks()
    width = ventana.winfo_width()
    height = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (width // 2)
    y = (ventana.winfo_screenheight() // 2) - (height // 2)
    ventana.geometry(f"{width}x{height}+{x}+{y}")


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
