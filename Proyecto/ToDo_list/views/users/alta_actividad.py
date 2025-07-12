import tkinter as tk
from tkinter import messagebox as mb
from ToDo_list.db.operations import alta_actividad
from ToDo_list.views.resources import PRIMARY_COLOR, SECONDARY_COLOR, THIRD_COLOR, FOURTH_COLOR, TITLE, TEXT

def show_alta_actividad(w:tk.Tk):
    for widget in w.winfo_children():
        widget.destroy()


    w.columnconfigure(0, weight=1)
    w.columnconfigure(1)
    w.columnconfigure(2, weight=1)
    for i in range(6):
        w.rowconfigure(i, pad=10)

#Titulo
    title = tk.Label(w, text="Vista para crear actividades", font=TITLE, fg=SECONDARY_COLOR, bg=PRIMARY_COLOR)
    title.grid(column=0, row=0, columnspan=3, sticky="n")

    tk.Label(w, text="titulo", font=TEXT, bg=PRIMARY_COLOR, fg=THIRD_COLOR).grid(column=0, row=1, sticky="en")
    entry_title = tk.Entry(w, font=TEXT)
    entry_title.grid(column=1, row=1)

    tk.Label(w, text="Descripcion", font=TEXT, bg=PRIMARY_COLOR, fg=THIRD_COLOR).grid(column=0, row=2, sticky="en")
    entry_description = tk.Entry(w, font=TEXT)
    entry_description.grid(column=1, row=2)

    tk.Label(w, text="fecha", font=TEXT, bg=PRIMARY_COLOR, fg=THIRD_COLOR).grid(column=0, row=3, sticky="en")
    entry_date = tk.Entry(w, font=TEXT)
    entry_date.grid(column=1, row=3)

    def enviar():
        data = {}
        data["titulo"] = entry_title.get()
        data["actividad"] = entry_description.get()
        data["fecha"] = entry_date.get()
        status, msg = alta_actividad(data)
        if not status:
            mb.showerror("Ocurrio un error", msg)
            return
        mb.showinfo("Usuario creado", msg)


    tk.Button(w, command=enviar, font=TEXT, text="Guardar", fg=FOURTH_COLOR, bg=SECONDARY_COLOR, relief="flat").grid(column=0, row=6, columnspan=3, sticky="n")

    w.mainloop()    