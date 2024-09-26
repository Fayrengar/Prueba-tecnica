from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost/flask_dashboard'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos con la app Flask
    db.init_app(app)

    # Importar rutas para registrar las rutas en la aplicación
    from app.routes import main
    app.register_blueprint(main)

    return app
