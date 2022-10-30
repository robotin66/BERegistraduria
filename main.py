from flask import Flask, jsonify, request

from controllers.mesas import *
from models.mesas import Mesas

app = Flask(__name__)

control_mesa = ControladorMesa()


@app.route("/", methods=["GET"])
def ping():
    return jsonify({"Mensaje": "Servidor corriendo"}), 200


@app.route("/mesas", methods=["GET"])
def mesas():
    lista = []
    for i in control_mesa.trae_todas():
        lista.append(i.__dict__)
    return jsonify({
        "Mesas": lista,
        "Total": control_mesa.total()
    }), 200


@app.route("/mesas/<int:num_mesa>", methods=["GET"])
def traer_mesa_por_id(num_mesa):
    try:
        encontrada = control_mesa.trae_elemento(num_mesa)
    except MesaInexistente:
        return jsonify({"Error": "Mesa no encontrada"}), 404
    else:
        return jsonify(encontrada.__dict__), 200


@app.route("/mesas/", methods=["POST"])
def crea_mesa():
    creada = control_mesa.crea(request.get_json())
    return jsonify({
        "Mensaje": "Mesa creada exitosamente",
        "Mesa": creada.__dict__
    }), 201


@app.route("/mesas/<int:num_mesa>", methods=["PUT"])
def actualiza_mesa(num_mesa):
    try:
        actualizada = control_mesa.actualiza(num_mesa, request.get_json())
    except MesaInexistente:
        return jsonify({"Error": "Mesa a borrar no encontrada"}), 404
    else:
        return jsonify({
            "Mensaje": f"Mesa {num_mesa} actualizada exitosamente",
            "Mesa": actualizada.__dict__
        }), 200


@app.route("/mesas/<int:num_mesa>", methods=["DELETE"])
def borra_mesa(num_mesa):
    try:
        control_mesa.borra(num_mesa)
    except MesaInexistente:
        return jsonify({"Error": "Mesa a borrar no encontrada"}), 404
    else:
        return jsonify({
            "Mensaje": f"Mesa {num_mesa} borrada exitosamente",
        }), 200


app.run(host="127.0.0.1", port=5001, debug=True)
