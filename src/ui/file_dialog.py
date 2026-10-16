import tkinter as tk
from tkinter.filedialog import askopenfilename

class FileDialogComponent:    
    @staticmethod
    def seleccionar_csv():        
        root = tk.Tk()
        root.withdraw()
        
        root.wm_attributes('-topmost', 1)

        ruta = askopenfilename(
            title="Selecciona el archivo de trazas HPC (CSV)",
            filetypes=[("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")]
        )

        root.destroy()
        return ruta if ruta else None