import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog
from tkcalendar import DateEntry
import os
import shutil
from tkinter import PhotoImage
import formulario

def placeholder_search(event, entry):
    if entry.get() == "":
        entry.insert(0, "Buscar...")
        entry.config(fg='grey')

def clear_placeholder(event, entry):
    if entry.get() == "Buscar...":
        entry.delete(0, tk.END)
        entry.config(fg='black')


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
    fade_color((240, 240, 240), (55, 55, 55), 10, 10, btn, is_background=True)  # Fade del fondo
    fade_color((0, 0, 0), (255, 255, 255), 10, 10, btn, is_background=False)  # Fade del texto

def on_leave(btn):
    # Restaura el color de fondo y texto al salir el mouse
    fade_color((55, 55, 55), (240, 240, 240), 10, 10, btn, is_background=True)  # Fade del fondo
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
