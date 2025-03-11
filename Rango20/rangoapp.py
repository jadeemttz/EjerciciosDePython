import tkinter as tk
from tkinter import messagebox
from rango import Rango 

class RangoApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x200")
        self.root.configure(bg="#FFB6C1")  
        
        self.label = tk.Label(root, text="Ingrese un número (0-20):", bg="#FFB6C1", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack()
        
        self.button = tk.Button(root, text="Validar", command=self.rango, bg="#FF69B4", fg="white", font=("Arial", 12))
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="", bg="#FFB6C1", font=("Arial", 12))
        self.result_label.pack()
    
    def rango(self):
        try:
            numero = int(self.entry.get())
            if Rango.validar_numero(numero):
                self.result_label.config(text=f"¡Número válido: {numero}!")
            else:
                messagebox.showwarning("Error", "Número fuera del rango. Intente nuevamente.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")
