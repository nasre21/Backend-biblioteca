from flask import jsonify, request
from database.db import connectdb

def add_cliente():
    conn = connectdb()
    cur = conn.cursor()
    data = request.get_json()

    nombre = data['nombre']
    apellidos = data['apellidos']
    edad = data['edad']
    telefono = data['telefono']
    direccion = data['direccion']
    email = data['email']


    cur.execute('INSERT INTO clientes (nombre, apellidos, edad, telefono, direccion, email) VALUES (%s, %s, %s, %s, %s, %s)', (nombre, apellidos, edad, telefono, direccion, email))
    conn.commit()
    conn.close()
    print('Empleado creado')
    return "Empleado agregado"