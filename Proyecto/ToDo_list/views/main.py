import tkinter as tk
from ToDo_list.views.users.home import mostrar_home
from ToDo_list.views.resources import PRIMARY_COLOR, ICON
main_window =tk.Tk()
main_window.state("zoomed")
main_window.config(bg=PRIMARY_COLOR)
main_window.iconbitmap(ICON)


mostrar_home(main_window)