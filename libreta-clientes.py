from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title('Proyecto: CRM')
root.geometry('500x500')

conn = sqlite3.connect('crm.db')

cursor = conn.cursor()

cursor.execute("""
                CREATE TABLE if not exists cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    telefono TEXT NOT NULL,
                    empresa TEXT NOT NULL
                );      
""")

def nuevo_cliente():
    pass

def eliminar_cliente():
    pass

button_cliente = Button(root, text='Nuevo Cliente', command=nuevo_cliente)
button_cliente.grid(column=0, row=0)

button_eliminar = Button(root, text='Eliminar Cliente', command=eliminar_cliente)
button_eliminar.grid(column=1, row=0)

tree = ttk.Treeview(root)
tree['columns'] = ('Nombre', 'Telefono', 'Empresa')
tree.column('#0', width=0, stretch=NO)
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Telefono')
tree.heading('Empresa', text='Empresa')
tree.grid(column=0, row=1, columnspan=2)

root.mainloop()