import tkinter as tk
from tkinter import messagebox as mb
from ToDo_list.views.resources import PRIMARY_COLOR, SECONDARY_COLOR, THIRD_COLOR, FOURTH_COLOR, TITLE,TEXT, LOGO, SUBTITLE
from PIL import Image, ImageTk
from ToDo_list.db.operations import get_all_activities, delete_activities
from ToDo_list.views.components.tabla import table_scrollable
from ToDo_list.views.users.alta_actividad import show_alta_actividad
import datetime

def mostrar_home(w:tk.Tk):

    def eliminar_actividades(name, user_id):
        res = mb.askyesno("Advertencia", f"Seguro de eliminar la actividad : {name}")
        if res:
            delete_activities(user_id)
            usuarios = get_all_activities()
            #funcion para actualizar tabla
            show_table(usuarios)


    #eliminar widgets anteriores
    for widget in w.winfo_children():
        widget.destroy()
    
    #contruccion de vusta home
    #columnas y filas
    for i in range(7):
        w.columnconfigure(i, weight=1)
        w.rowconfigure(i, weight=1)


    #LOGO
    image_pil = Image.open(LOGO)
    
    photo = ImageTk.PhotoImage(image_pil)
    w.photo = photo
    tk.Label(w, image=photo, bg=PRIMARY_COLOR). grid(row=0,  column=0, columnspan=7, sticky='n')
    #Menu de navegacion (navbar)

    #columna inical
    w.columnconfigure(0, weight=1)
    w.columnconfigure(6, weight=1)

    #columna final
    w.columnconfigure(6, weight=1)
    buttons_labels = ["Actividades", "Actividades hechas", "Actividades proximas"]
    index = 1
    for label in buttons_labels:
        tk.Button(w, text=label, relief='flat', background=PRIMARY_COLOR, fg=SECONDARY_COLOR, font=TEXT).grid(column=index, row=1, sticky='we')
        index+=1

        

    #Subtitulo y boton para crear usuarios
    tk.Label(w, text='Actividades', font=SUBTITLE, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR).grid(column=0, row=2, columnspan=6, sticky='n')

    tk.Button(w, text='Crear actividad', font=TEXT,command=lambda:show_alta_actividad(w), bg=THIRD_COLOR, fg=PRIMARY_COLOR).grid(column=5, row=2, sticky='n')

    #Tablita 
    print(get_all_activities())
    usuarios = get_all_activities()
    


       
    def show_table(users):
        view_scrollable = table_scrollable(w,1,3, columnspan=5, padx=10, pady=10)

        columns = [" Actividad ", "    descripcion    ", " fecha "," Opciones "]
        for indice, column in enumerate(columns):
         tk.Label(view_scrollable,text=column, relief='solid', font=TEXT, bg=PRIMARY_COLOR, fg=FOURTH_COLOR). grid(sticky='we', column=indice, row=0)
        for indice, user in enumerate(users, 1):
            #muestra el nombre
                tk.Label(view_scrollable, text=user  [1], relief='solid', font=TEXT, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR). grid(sticky='news', column=0, row=indice)
                tk.Label(view_scrollable, text=user [2], relief='solid', font=TEXT, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR). grid(sticky='news', column=1, row=indice)  
                tk.Label(view_scrollable, text=user [3], relief='solid', font=TEXT, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR). grid(sticky='news', column=2, row=indice) 
                tk.Button(view_scrollable, text="Eliminar",command=lambda: eliminar_actividades(user[1],user[0]), relief="ridge", font=TEXT, bg=PRIMARY_COLOR, fg=FOURTH_COLOR). grid(column=3, row=indice, sticky="e")
    show_table(usuarios)