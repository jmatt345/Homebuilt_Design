from tkinter import *
from tkinter import Menu
from tkinter import ttk

# Create a GUI window
window = Tk()
window.title("Homebuilt Aircraft Design")

# Create a menu bar a add menu items
menu = Menu(window)
new_item = Menu(menu, tearoff = 0)
new_item.add_command(label = 'New')
new_item.add_separator()
new_item.add_command(label = 'Edit')
menu.add_cascade(label = 'File', menu = new_item)
window.config(menu = menu)

# Create a tabs
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text = 'Power Loading')
tab_control.add(tab2, text = 'Wing Loading')
tab_control.add(tab3, text = 'Airplane Sizing')
tab_control.pack(expand = 1, fill = 'both')

window.mainloop()
