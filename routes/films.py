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

def get_films():
    conn = connectdb()
    cur = conn.cursor()
    cur.execute('SELECT * FROM peliculas')
    datos_films = cur.fetchall()
    data = [{'id_pelicula': dato[0],'titulo':dato[1], 'año':dato[2], 'director':dato[3], 'categoria':dato[4], } for dato in datos_films]
    
    