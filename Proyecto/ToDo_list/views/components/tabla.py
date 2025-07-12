import tkinter as tk
from ToDo_list.views.resources import PRIMARY_COLOR


def table_scrollable(w:tk.Tk, column, row, columnspan=0, padx=0, pady=0):
    contenedor =tk.Frame(w)
    contenedor.grid(sticky = "News",column=column, row=row, columnspan=columnspan, padx=padx, pady=pady)

    canvas =tk.Canvas(contenedor)
    scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set, background=PRIMARY_COLOR)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


    frame_scrollable = tk.Frame(canvas)
    canvas.create_window((0,0), window=frame_scrollable, anchor="nw")
    

    def on_configure():
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_scrollable.bind("<Configure>", on_configure)
    return frame_scrollable