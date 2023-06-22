from flask import jsonify, request
from database.db import connectdb


def add_films():
    conn = connectdb()
    cur = conn.cursor()
    data = request.get_json()
    
    nombre = data['nombre']
    año = data['año']
    director = data['director']
    categoria = data['categoria']
    precio = data['precio']
    
    
    cur.execute('INSERT INTO peliculas (nombre, año, director, categoria, precio) VALUES (%s, %s, %s,%s, %s)',(nombre, año, director, categoria, precio))
    
    conn.commit()
    conn.close()
    print('films created')
    return "Films add"