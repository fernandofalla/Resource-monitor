import time
from src.ui.file_dialog import FileDialogComponent

class MenuApp:
    def __init__(self, servicio_datos):        
        self.servicio = servicio_datos       

    def mostrar_encabezado(self):
        print("\n                HPC - MENU APP")
        print("     ------------------------------------------")
        print("     |   Nombre: Luis Fernando Falla Guzmán   |")
        print("     |   Carné: 201700700                     |")
        print("     ------------------------------------------")
        print("1. Cargar archivo de recursos") 
        print("2. Mostrar recursos en tiempo real")
        print("0. Salir\n")

    def cargar_archivo(self):
        ruta = FileDialogComponent.seleccionar_csv()

        if not ruta:
            print("No se seleccionó ningún archivo.")
            return

        print(f"Cargando archivo de recursos desde: {ruta} ...")
        
        if self.servicio.cargar_csv(ruta):
            print("¡Archivo cargado con éxito en memoria!")
        else:
            print("No se pudo cargar el archivo.")
    
    def mostrar_recursos(self):
        df = self.servicio.obtener_metricas()
        
        if df is None:
            print("Primero debes cargar un archivo (Opción 1).")
            return

        print("\nIniciando monitoreo en tiempo real (Presiona Ctrl+C para detener)...")
        print("─" * 55)
        print(f"{'SERVIDOR':<18} | {'USO CPU (%)':<12} | {'USO RAM (%)':<12}")
        print("─" * 55)

        try:
            for indice, fila in df.iterrows():
                cpu = fila['avg_cpu'] * 100
                ram = fila['avg_mem'] * 100
                print(f"Servidor_HPC_{indice:<4} | {cpu:>10.2f}% | {ram:>10.2f}%")
                time.sleep(0.5) 
        except KeyboardInterrupt:
            print("\n\nMonitoreo detenido por el usuario.")

    def ejecutar(self):
        while True:
            self.mostrar_encabezado()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.cargar_archivo()
            elif opcion == "2":
                self.mostrar_recursos()
            elif opcion == "0":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")