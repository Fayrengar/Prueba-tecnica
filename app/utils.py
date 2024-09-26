import matplotlib.pyplot as plt
import plotly.express as px
import base64
from io import BytesIO

def create_bar_chart(edades, salarios):
    fig, ax = plt.subplots()
    ax.bar(edades, salarios)
    ax.set_xlabel('Edad')
    ax.set_ylabel('Salario')
    ax.set_title('Relación Edad-Salario')
    
    # Convertir gráfico a imagen base64
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    
    return image_base64

def create_pie_chart(ciudades):
    fig = px.pie(names=ciudades, title='Distribución por Ciudad')
    return fig.to_html(full_html=False)
