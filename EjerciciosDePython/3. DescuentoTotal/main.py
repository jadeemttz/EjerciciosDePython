import tkinter as tk
from descuentoapp import DescuentoApp

def main():
    root = tk.Tk()
    root.title("Cálculo de Descuento")
    app = DescuentoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
