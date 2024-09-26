# Flask Dashboard

Este es un dashboard sencillo utilizando Flask, MySQL y Matplotlib/Plotly para visualización de datos.

## Requisitos

- Python 3.x
- MySQL

## Instalación

1. Clonar el repositorio.
2. Crear la base de datos:

```bash
CREATE DATABASE flask_dashboard;
USE flask_dashboard;

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    ciudad VARCHAR(100),
    salario DECIMAL(10,2)
);

-- Inserción de registros de prueba
INSERT INTO empleados (nombre, edad, ciudad, salario) VALUES
('Carlos', 30, 'Lima', 3000.00),
('Ana', 25, 'Huacho', 3500.00),
('Pedro', 28, 'Lima', 2500.00),
('Maria', 22, 'Arequipa', 2700.00),
('Luis', 35, 'Huacho', 4000.00);

```

3. Crear un entorno virtual:

```bash
   python3 -m venv venv

   # Activar el entorno 

   venv\Scripts\activate

   # Instalar dependencias

   pip install -r requirements.txt
   
   # Ejecutar el programa

   flask run


```
