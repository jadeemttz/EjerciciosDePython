import tkinter as tk
from salarioapp import SalarioApp

def main():
    root = tk.Tk()
    root.title("Cálculo de Salario")
    app = SalarioApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
