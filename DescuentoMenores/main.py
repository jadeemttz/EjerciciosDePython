import tkinter as tk
from descuentoentradaapp import DescuentoApp

def main():
    root = tk.Tk()
    root.title("Descuento en el Parque")
    app = DescuentoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
