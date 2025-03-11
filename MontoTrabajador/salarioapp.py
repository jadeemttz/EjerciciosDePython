import tkinter as tk
from tkinter import messagebox
from salario import Empleado

class SalarioApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("450x350")
        self.root.configure(bg="#FFB6C1")
        
        self.label_nombre = tk.Label(root, text="Nombre del empleado:", bg="#FFB6C1", font=("Arial", 12))
        self.label_nombre.pack(pady=5)
        self.entry_nombre = tk.Entry(root, font=("Arial", 12))
        self.entry_nombre.pack()
        
        self.label_horas_normales = tk.Label(root, text="Horas normales:", bg="#FFB6C1", font=("Arial", 12))
        self.label_horas_normales.pack(pady=5)
        self.entry_horas_normales = tk.Entry(root, font=("Arial", 12))
        self.entry_horas_normales.pack()
        
        self.label_horas_extras = tk.Label(root, text="Horas extras:", bg="#FFB6C1", font=("Arial", 12))
        self.label_horas_extras.pack(pady=5)
        self.entry_horas_extras = tk.Entry(root, font=("Arial", 12))
        self.entry_horas_extras.pack()
        
        self.label_hijos = tk.Label(root, text="Cantidad de hijos:", bg="#FFB6C1", font=("Arial", 12))
        self.label_hijos.pack(pady=5)
        self.entry_hijos = tk.Entry(root, font=("Arial", 12))
        self.entry_hijos.pack()
        
        self.label_tarifa = tk.Label(root, text="Tarifa por hora:", bg="#FFB6C1", font=("Arial", 12))
        self.label_tarifa.pack(pady=5)
        self.entry_tarifa = tk.Entry(root, font=("Arial", 12))
        self.entry_tarifa.pack()
        
        self.button_calcular = tk.Button(root, text="Calcular Salario", command=self.calcular_salario, bg="#FF69B4", fg="white", font=("Arial", 12))
        self.button_calcular.pack(pady=10)
    
    def calcular_salario(self):
        try:
            nombre = self.entry_nombre.get()
            horas_normales = self.entry_horas_normales.get()
            horas_extras = self.entry_horas_extras.get()
            hijos = self.entry_hijos.get()
            tarifa = self.entry_tarifa.get()
            
            if not nombre.isalpha():
                raise ValueError("El nombre debe contener solo letras.")
            
            if not horas_normales.isdigit() or int(horas_normales) <= 0:
                raise ValueError("Las horas normales deben ser un número entero positivo.")
            
            if not horas_extras.isdigit() or int(horas_extras) < 0:
                raise ValueError("Las horas extras deben ser un número entero positivo o cero.")
            
            if not hijos.isdigit() or int(hijos) < 0:
                raise ValueError("La cantidad de hijos debe ser un número entero positivo o cero.")
            
            try:
                tarifa = float(tarifa)
                if tarifa <= 0:
                    raise ValueError("La tarifa por hora debe ser un número decimal positivo.")
            except ValueError:
                raise ValueError("La tarifa por hora debe ser un número decimal válido.")
            
            empleado = Empleado(
                nombre,
                int(horas_normales),
                int(horas_extras),
                int(hijos),
                tarifa
            )
            total = empleado.calcular_pago_total()
            messagebox.showinfo("Salario Calculado", f"Pago total para {empleado.nombre}: {total:.2f}")
        
        except ValueError as e:
            messagebox.showerror("Error", str(e))
