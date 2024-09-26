from flask import Blueprint, render_template
from app.models import Empleado
from app.utils import create_bar_chart, create_pie_chart

# Crea un blueprint para las rutas
main = Blueprint('main', __name__)

@main.route('/')
def index():
    empleados = Empleado.query.all()

    # Datos para los gráficos
    edades = [emp.edad for emp in empleados]
    salarios = [emp.salario for emp in empleados]
    ciudades = [emp.ciudad for emp in empleados]

    # Gráficos
    bar_chart = create_bar_chart(edades, salarios)
    pie_chart = create_pie_chart(ciudades)

    return render_template('dashboard.html', empleados=empleados, bar_chart=bar_chart, pie_chart=pie_chart)
