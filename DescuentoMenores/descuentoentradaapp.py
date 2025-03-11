import tkinter as tk
from tkinter import messagebox
from descuentoentrada import DescuentoEntrada

class DescuentoApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x250")
        self.root.configure(bg="#98FB98")  
        self.label = tk.Label(root, text="Ingrese la edad:", bg="#98FB98", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack()

        self.button = tk.Button(root, text="Calcular Pago", command=self.calcular_pago, bg="#006400", fg="white", font=("Arial", 12))
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="", bg="#98FB98", font=("Arial", 12))
        self.result_label.pack()

    def calcular_pago(self):
        try:
            edad = int(self.entry.get())
            descuento = DescuentoEntrada(edad)
            total = descuento.calcular_pago()

            self.result_label.config(text=f"Total a pagar: {total:.2f} soles")
        except ValueError:
            messagebox.showerror("Error", "Ingrese una edad válida.")
