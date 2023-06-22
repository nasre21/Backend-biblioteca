from flask import Flask
from routes.empleados import *
from routes.cliente import *
from routes.films import *

app = Flask(__name__)

# Rutas empleados
app.route('/empleado_add', methods=['POST'])(add_empleado)
app.route('/empleados', methods=['GET'])(get_empleados)
app.route('/empleado/<int:id_empleado>')(obtener_empleado_por_id)
app.route('/empleados_del/<int:id_empleado>', methods=['DELETE'])(del_empleado)
app.route("/empleado/<int:id_empleado>", methods=["PATCH"])(update_empleado)

# Roots cliente nueva
app.route('/cliente_add', methods=['POST'])(add_cliente)



# Path Movies
app.route('films_add', methods = ['POST'])(add_films)


if __name__ == '__main__':
    app.run(debug=True)
