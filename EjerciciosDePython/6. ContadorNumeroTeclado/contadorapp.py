import tkinter as tk
from tkinter import messagebox
from contador import Contador

class ContadorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x250")
        self.root.configure(bg="#98FB98") 
        self.intentos = 0
        
        self.label = tk.Label(root, text="Ingrese un número (1-19):", bg="#98FB98", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack()
        
        self.button = tk.Button(root, text="Validar", command=self.contador, bg="#2E8B57", fg="white", font=("Arial", 12))
        self.button.pack(pady=10)
        
        self.label_intentos = tk.Label(root, text="Intentos: 0", bg="#98FB98", font=("Arial", 12))
        self.label_intentos.pack()
    
    def contador(self):
        try:
            numero = int(self.entry.get())
            self.intentos += 1
            self.label_intentos.config(text=f"Intentos: {self.intentos}")
            
            if Validacion.validar_numero(numero):
                messagebox.showinfo("Éxito", f"El número {numero} es válido. Intentos: {self.intentos}")
            else:
                messagebox.showwarning("Error", "Número fuera del rango. Intente nuevamente.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")
