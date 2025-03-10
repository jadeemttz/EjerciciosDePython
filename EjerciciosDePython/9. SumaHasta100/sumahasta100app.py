import tkinter as tk
from tkinter import messagebox
from sumahasta100 import SumaLimitada

class SumaLimitadaApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x250")
        self.root.configure(bg="#ADD8E6")  
        self.suma = SumaLimitada()
        
        self.label = tk.Label(root, text="Ingrese un número (Límite: 100)", bg="#ADD8E6", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack()
        
        self.button = tk.Button(root, text="Agregar", command=self.agregar, bg="#1E90FF", fg="white", font=("Arial", 12))
        self.button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="Suma total: 0", bg="#ADD8E6", font=("Arial", 12))
        self.result_label.pack()
    
    def agregar(self):
        try:
            numero = int(self.entry.get())
            total = self.suma.agregar_numero(numero)
            self.result_label.config(text=f"Suma total: {total}")
            
            if self.suma.ha_superado_limite():
                messagebox.showinfo("Resultado", f"Suma final: {total} (superó 100)")
                self.root.quit()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")
