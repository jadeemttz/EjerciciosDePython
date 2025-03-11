import tkinter as tk
from tkinter import messagebox
from descuento import Descuento

class DescuentoApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.configure(bg="#FFD700")  

        self.label_mes = tk.Label(root, text="Ingrese el no. de mes:", bg="#FFD700", font=("Arial", 12))
        self.label_mes.pack(pady=5)

        self.entry_mes = tk.Entry(root, font=("Arial", 12))
        self.entry_mes.pack()

        self.label_importe = tk.Label(root, text="Ingrese el importe:", bg="#FFD700", font=("Arial", 12))
        self.label_importe.pack(pady=5)

        self.entry_importe = tk.Entry(root, font=("Arial", 12))
        self.entry_importe.pack()

        self.button = tk.Button(root, text="Calcular Total", command=self.calcular_descuento, bg="#8B0000", fg="white", font=("Arial", 12))
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="", bg="#FFD700", font=("Arial", 12))
        self.result_label.pack()

    def calcular_descuento(self):
        try:
            mes = self.entry_mes.get()
            importe = self.entry_importe.get()

            # Validar mes (debe ser un número entre 1 y 12)
            if not mes.isdigit() or int(mes) < 1 or int(mes) > 12:
                raise ValueError("Ingrese un mes válido (1-12).")

            # Validar importe (debe ser un número positivo)
            if not importe.replace('.', '', 1).isdigit() or float(importe) <= 0:
                raise ValueError("Ingrese un importe válido y positivo.")
            
            mes = int(mes)
            importe = float(importe)
            
            descuento = Descuento(mes, importe)
            total = descuento.calcular_total()
            
            self.result_label.config(text=f"Total a pagar: ${total:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", f"Error: {e}")
