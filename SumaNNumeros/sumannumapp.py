import tkinter as tk
from tkinter import messagebox
from sumannum import Suma

class SumaApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x200")
        self.root.configure(bg="#87CEEB")  
        
        self.label = tk.Label(root, text="Ingrese un número entero positivo:", bg="#87CEEB", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack()
        
        self.button = tk.Button(root, text="Calcular Suma", command=self.calcular_suma, bg="#4682B4", fg="white", font=("Arial", 12))
        self.button.pack(pady=10)
    
    def calcular_suma(self):
        try:
            n = int(self.entry.get())
            if n > 0:
                resultado = Suma.calcular_suma(n)
                messagebox.showinfo("Resultado", f"La suma de los primeros {n} números es {resultado}.")
            else:
                messagebox.showwarning("Error", "Ingrese un número mayor a 0.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")
