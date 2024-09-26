from app import db

# Define el modelo de empleado
class Empleado(db.Model):
    __tablename__ = 'empleados'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    ciudad = db.Column(db.String(100))
    salario = db.Column(db.Numeric(10, 2))
