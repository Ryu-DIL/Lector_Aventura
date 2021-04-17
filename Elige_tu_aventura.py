import tkinter as tk
import time

# pylint: disable=maybe-no-member

class Pagina:
	def __init__(self, Inicio):
		self.Inicio = Inicio

		Inicio.title("Elige tu propia ventura")
		Inicio.geometry("500x500")	

		tk.Grid.rowconfigure(Inicio,0,weight=1)
		tk.Grid.rowconfigure(Inicio,1,weight=50)
		tk.Grid.rowconfigure(Inicio,2,weight=1)
		tk.Grid.columnconfigure(Inicio,0,weight=1)
		tk.Grid.columnconfigure(Inicio,1,weight=1)

		self.numero_de_pagina = 1

		self.Texto = tk.Text(Inicio)
		self.Texto.bind("<Button>", lambda e: "break")
		self.Texto.bind("<Motion>", lambda e: "break")
		self.Texto.bind("<ButtonRelease>", lambda e: "break")
		self.Texto.bind("<ButtonPress>", lambda e: "break")
		self.Texto.bind("<Key>", lambda e: "break")

		self.Barra = tk.Scrollbar(self.Texto, orient = "vertical", command = self.Texto.yview)
		self.Boton = tk.Button(Inicio, text = "Empezar historia", command = lambda : Pagina1(Inicio))
		self.Texto.configure(yscrollcommand=self.Barra.set)
		self.pagina_actual = tk.Label(Inicio, text = "Página"+str(self.numero_de_pagina))
		self.Boton_Salir   = tk.Button(Inicio, text = "Cerrar Libro", command = Inicio.destroy)

		self.Rutas()

		self.Barra.pack(side = "right", fill = "y")
		self.Boton_Salir.grid(row = 0, column = 1, sticky = "nsew")
		self.Boton.grid(row = 2, column = 0, columnspan = 2, sticky = "nsew")
		self.Texto.grid(row = 1, column = 0, columnspan = 2, sticky = "nsew")
		
	
	def Rutas(self):
		for i in range(2, 6):
			exec("self.Boton_Pagina" + str(i) + " = tk.Button(Inicio, command = lambda : Pagina" + str(i) + "(Inicio))")
		self.Boton_Revivir = tk.Button(Inicio, text = "Volver a leer la aventura?", command = lambda : Pagina1(Inicio))

def Morir(Inicio):
	Pantalla.Boton.grid_forget()
	
	Escribir_Linea(Inicio, "Fin.")
	Pantalla.Boton_Revivir.grid(row = 2, column = 0, columnspan = 2, sticky = "nsew")

def Escribir_Linea(Inicio, frase):
	Pantalla.Texto.insert(tk.INSERT, frase)
	Inicio.update()

def Borrar_Todo(Inicio):
	Pantalla.Texto.delete(1.0, tk.END)
	Inicio.update()

def Pagina1(Inicio):
	Pantalla.Texto.delete(1.0, tk.END)
	Pantalla.Boton_Revivir.grid_forget()
	Pantalla.Boton.grid_forget()

	for i in range(50):
		frase = str(f"{i+1}.- Siempre has sentido interés por la ciencia.\n")
		Escribir_Linea(Inicio, frase)
		time.sleep(0.1)
	Escribir_Linea(Inicio, "Camino 1: Ve a la Pagina 2.\n")
	Escribir_Linea(Inicio, "Camino 2: Ve a la Pagina 3.\n")
	
	Pantalla.Boton_Pagina2.configure(text = "Camino 1")
	Pantalla.Boton_Pagina3.configure(text = "Camino 2")
	Pantalla.Boton_Pagina2.grid(row = 2, column = 0, sticky = "nsew")
	Pantalla.Boton_Pagina3.grid(row = 2, column = 1, sticky = "nsew")

def Pagina2(Inicio):
	Borrar_Todo(Inicio)
	Pantalla.Boton_Pagina2.grid_forget()
	Pantalla.Boton_Pagina3.grid_forget()

	Escribir_Linea(Inicio, "Eliges el Camino 1.\n")
	Inicio.update()
	time.sleep(1)
	Escribir_Linea(Inicio, "MUERES!!!")
	time.sleep(5)
	Morir(Inicio)

def Pagina3(Inicio):
	Borrar_Todo(Inicio)
	Pantalla.Boton_Pagina2.grid_forget()
	Pantalla.Boton_Pagina3.grid_forget()

	Escribir_Linea(Inicio, "Eliges el Camino 2.\n")
	time.sleep(1)
	Escribir_Linea(Inicio, "VIVES!!!")
	Escribir_Linea(Inicio, "Camino 1: Un Avion.\n")
	Escribir_Linea(Inicio, "Camino 2: Un Barco.\n")
	
	Pantalla.Boton_Pagina4.configure(text = "Un avion")
	Pantalla.Boton_Pagina5.configure(text = "Un barco")
	Pantalla.Boton_Pagina4.grid(row = 2, column = 0, sticky = "nsew")
	Pantalla.Boton_Pagina5.grid(row = 2, column = 1, sticky = "nsew")

def Pagina4(Inicio):
	Borrar_Todo(Inicio)
	Pantalla.Boton_Pagina4.grid_forget()
	Pantalla.Boton_Pagina5.grid_forget()
	
	Escribir_Linea(Inicio, "Subes al avión.\n")
	time.sleep(1)
	Escribir_Linea(Inicio, "MUERES!!!")
	time.sleep(5)
	Morir(Inicio)

def Pagina5(Inicio):
	Borrar_Todo(Inicio)
	Pantalla.Boton_Pagina4.grid_forget()
	Pantalla.Boton_Pagina5.grid_forget()

	Escribir_Linea(Inicio, "Subes al barco.\n")
	time.sleep(1)
	Escribir_Linea(Inicio, "Te escapas!!!")
	time.sleep(5)
	Morir(Inicio)

if __name__ == "__main__":
	Inicio = tk.Tk()
	Pantalla = Pagina(Inicio)
	Pagina1(Inicio)
	Inicio.mainloop()