import tkinter as tk
from tkinter import messagebox

tareas = []

def agregar_tarea():
    tarea = entrada.get()
    if tarea != "":
        tareas.append(tarea)
        actualizar_lista()
        entrada.delete(0, tk.END)

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        tareas.pop(seleccion[0])
        actualizar_lista()

def completar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        index = seleccion[0]
        tareas[index] = "[Hecho] " + tareas[index]
        actualizar_lista()

def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea)

# Interfaz
ventana = tk.Tk()
ventana.title("Lista de Tareas")

entrada = tk.Entry(ventana, width=40)
entrada.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_tarea)
boton_agregar.pack()

boton_completar = tk.Button(ventana, text="Completar", command=completar_tarea)
boton_completar.pack()

boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_tarea)
boton_eliminar.pack()

lista_tareas = tk.Listbox(ventana, width=50)
lista_tareas.pack()

ventana.mainloop()
