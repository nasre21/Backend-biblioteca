from flask import Flask
from routes.empleados import *

app = Flask(__name__)

# Rutas empleados
app.route('/empleado', methods=['POST'])(add_empleado)
app.route('/', methods=['GET'])(get_empleados)
app.route('/empleado/<int:id_empleado>')(obtener_empleado_por_id)
app.route('/del/<int:id_empleado>', methods=['DELETE'])(del_empleado)
app.route("/empleado/<int:id_empleado>", methods=["PATCH"])(update_empleado)

if __name__ == '__main__':
    app.run(debug=True)
