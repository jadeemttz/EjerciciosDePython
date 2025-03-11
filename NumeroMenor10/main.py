import tkinter as tk
from validacionapp import ValidacionApp

def main():
    root = tk.Tk()
    root.title("Validación de Número")
    app = ValidacionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
