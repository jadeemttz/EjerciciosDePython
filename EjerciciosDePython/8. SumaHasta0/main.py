import tkinter as tk
from sumahasta0app import SumadorApp

def main():
    root = tk.Tk()
    root.title("Suma hasta 0")
    
    app = SumadorApp(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
