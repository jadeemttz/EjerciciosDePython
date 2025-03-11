import tkinter as tk
from tkinter import messagebox
from sumahasta0 import Sumador

class SumadorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x250")
        self.root.configure(bg="#FFD700")  
        self.sumador = Sumador()
        
        self.label = tk.Label(root, text="Ingrese un número (0 para finalizar):", bg="#FFD700", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack()
        
        self.button = tk.Button(root, text="Agregar", command=self.agregar, bg="#FFA500", fg="white", font=("Arial", 12))
        self.button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="Suma total: 0", bg="#FFD700", font=("Arial", 12))
        self.result_label.pack()
    
    def agregar(self):
        try:
            numero = int(self.entry.get())
            if numero == 0:
                messagebox.showinfo("Resultado", f"Suma final: {self.sumador.suma_total}")
                self.root.quit()
            else:
                total = self.sumador.agregar_numero(numero)
                self.result_label.config(text=f"Suma total: {total}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")
