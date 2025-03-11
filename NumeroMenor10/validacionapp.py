import tkinter as tk
from tkinter import messagebox
from validacion import ValidacionNumero

class ValidacionApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x250")
        self.root.configure(bg="#87CEEB") 

        self.label = tk.Label(root, text="Ingrese un número (< 10):", bg="#87CEEB", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack()

        self.button = tk.Button(root, text="Validar", command=self.validar_numero, bg="#000080", fg="white", font=("Arial", 12))
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="", bg="#87CEEB", font=("Arial", 12))
        self.result_label.pack()

    def validar_numero(self):
        try:
            numero = int(self.entry.get())
            validacion = ValidacionNumero(numero)
            
            if validacion.es_valido():
                self.result_label.config(text=f"¡Número válido: {numero}!")
            else:
                messagebox.showerror("Error", "El número debe ser menor que 10.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")
