from tkinter import font
import tkinter as tk
Ventana=tk.Tk()
Ventana.title("Calculo de Raices metodo Secante")
Ventana.configure(bg="#424949")
Ventana.geometry('1000x800')

frmBotones = tk.Frame(Ventana,bg="#7F8C8D",height=100,width=100,padx=5,pady=5)
frmBotones.grid(row=1, column=1, columnspan=2)

frmGrafica = tk.Frame(Ventana,bg="#D6DBDF",height=500,width=500)
frmGrafica.grid(row=2, column=1)

frmTabla = tk.Frame(Ventana,bg="#4D5656",height=500,width=500)
frmTabla.grid(row=2, column=2)


# Estos botones van dentro del frame pero el frame se ajusta a los botones
# y quiero dejarlo de un tamaño fijo:

Helvfont = font.Font(family="Helvetica", size=12, weight="bold")
tk.Button(frmBotones,text="graficar",font=Helvfont,fg="blue").grid(row=1,column=3)
tk.Button(frmBotones,text="Hola",font=Helvfont,fg="blue").grid(row=1,column=2)

Ventana.mainloop()