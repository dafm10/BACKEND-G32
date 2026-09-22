from dotenv import load_dotenv
load_dotenv()
# Importaciones específicas
from app import create_app
# Importaciones totales (toda la información del archivo)
# import app


app = create_app()

if __name__ == "__main__":
    app.run()