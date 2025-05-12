import tkinter as tki

ventana = tki.Tk()
ventana.geometry("600x400")

etiqueta = tki.Label(ventana, text = "Londoño es tonto", bg = "blue")
etiqueta.pack(fill = tki.Y, expand = True)
ventana.mainloop()
