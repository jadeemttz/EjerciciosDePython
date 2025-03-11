import tkinter as tk
from sumahasta100app import SumaLimitadaApp

def main():
    root = tk.Tk()
    root.title("Suma hasta 100")
    app = SumaLimitadaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
