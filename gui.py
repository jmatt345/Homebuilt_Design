from tkinter import *
from tkinter import Menu
from tkinter import ttk

# Create a GUI window
window = Tk()
window.title("Homebuilt Aircraft Design")
window.geometry('400x600')

# Create a menu bar and add menu items
menu = Menu(window)
new_item = Menu(menu, tearoff = 0)
new_item.add_command(label = 'New')
new_item.add_separator()
new_item.add_command(label = 'Save')
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

# Tab 1 functions
def PwrLd():
  vmax = txtVmax_input.get()
  desConfig = comboDesignConfig.get()
  

# Create tab 1 inputs
lblVmax_input = Label(tab1, text = "What is the desired Vmax in knots?", padx = 5, pady = 3)
lblVmax_input.grid(column = 0, row = 0)
txtVmax_input = Entry(tab1, width = 10, padx = 5, pady = 3)
txtVmax_input.grid(column = 0, row = 1)
txtVmax_input.focus()
lblDesignConfig = Label(tab1, text = "What is the intended aircraft configuration?", padx = 5, pady = 3)
lblDesignConfig.grid(column = 0, row = 2)
comboDesignConfig = Combobox(tab1, padx = 5, pady = 3)
comboDesignConfig['values'] = ('Fixed-Gear Normal Design', 'Retract-Gear Normal Design', 'Fixed-Gear Smooth Design', 'Rectract-Gear Smooth Design', 'Acrobatic', 'Rag Wings', 'Ultralights', 'Text')
comboDesignConfig.current(1)
comboDesignConfig.grid(column = 0, row = 3)
calcPowerLoad = Button(tab1, text = "Calculate Power Loading", command = PwrLd, padx = 5, pady = 5)
calcPowerLoad.grid(column = 1, row = 7)

window.mainloop()
