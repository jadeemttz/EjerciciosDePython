import tkinter as tk
from tkinter import messagebox
from Empleado import Empleado

class Salarioapp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Incremento de Salario")
        self.root.geometry("400x300")
        self.root.configure(bg="#D0F4D3")
        
        # Etiqueta de Nombre
        self.nombre_label = tk.Label(root, text="Nombre:", bg="#D0F4D3", font=("Arial", 12))
        self.nombre_label.pack(pady=10)
        
        # Campo de entrada para nombre
        self.nombre_entry = tk.Entry(root, font=("Arial", 12))
        self.nombre_entry.pack()
        
        # Etiqueta de Salario
        self.salario_label = tk.Label(root, text="Salario Base:", bg="#D0F4D3", font=("Arial", 12))
        self.salario_label.pack(pady=10)
        
        # Campo de entrada para salario
        self.salario_entry = tk.Entry(root, font=("Arial", 12))
        self.salario_entry.pack(pady=5)
        
        # Botón de Calcular incremento
        self.Calcular_button = tk.Button(
            root,
            text="Calcular Incremento",
            command=self.Calcular_incremento,
            bg="#82CFC2",  # Verde menta
            fg="white",
            font=("Arial", 12),
        )
        self.Calcular_button.pack(pady=20)
    
    def Calcular_incremento(self):
        try:
            nombre = self.nombre_entry.get()
            salario_base = float(self.salario_entry.get())
            if not nombre or salario_base <= 0:
                raise ValueError("Ingrese valores válidos.")
            empleado = Empleado(nombre, salario_base)
            incremento = empleado.calcular_salario()
            nuevo_salario = empleado.nuevo_salario()
            messagebox.showinfo("Incremento de Salario", f"Incremento: ${incremento:.2f}\nNuevo Salario: ${nuevo_salario:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", f"Error: {e}")
            
if __name__ == "__main__":
    root = tk.Tk()
    Salarioapp = Salarioapp(root)
    root.mainloop()
