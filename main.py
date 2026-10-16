from src.services.data_loader import ResourceService
from src.ui.console import MenuApp

def main():    
    servicio = ResourceService()
    app = MenuApp(servicio)
    app.ejecutar()

if __name__ == "__main__":
    main()