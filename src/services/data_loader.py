import pandas as pd

class ResourceService:
    def __init__(self):
        self.datos = None

    def cargar_csv(self, ruta_csv):        
        try:
            columnas = ['avg_cpu', 'avg_mem', 'avg_assigned_mem']            
            self.datos = pd.read_csv(ruta_csv, usecols=columnas)
            return True
        except Exception as e:
            print(f"\n Error al cargar el archivo: {e}")
            return False

    def obtener_metricas(self):        
        return self.datos
