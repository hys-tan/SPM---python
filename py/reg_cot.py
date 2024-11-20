import tkinter as tk
from tkinter import PhotoImage

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Mi Aplicación")
    root.geometry("400x300")  # Tamaño de la ventana

    # Cargar el icono
    icon_path = "SPM---python/icons/cancel.png"  # Cambia 'tu_icono.png' por el nombre de tu archivo de icono
    icon = PhotoImage(file=icon_path)

    # Agregar un label con el icono
    label = tk.Label(root, text="¡Hola, mundo!", font=("Arial", 16))
    label.pack(pady=20)

    # Agregar un label que contenga el icono
    icon_label = tk.Label(root, image=icon)
    icon_label.pack(pady=10)

    # Agregar un botón
    button = tk.Button(root, text="Cerrar", command=root.destroy)
    button.pack(pady=10)

    # Iniciar el bucle principal
    root.mainloop()

if __name__ == "__main__":
    main()