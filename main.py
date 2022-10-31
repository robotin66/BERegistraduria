from flask import Flask, jsonify, request

from controllers.mesas import *
from models.mesas import Mesas, MesaInexistente

app = Flask(__name__)

control_mesa = ControladorMesas()


@app.route("/", methods=["GET"])
def ping():
    return jsonify({"Mensaje": "Servidor corriendo"}), 200


@app.route("/mesas", methods=["GET"])
def mesas():
    lista = []
    for i in control_mesa.trae_todo():
        lista.append(i.__dict__)
    return jsonify({
        "Cantidad": control_mesa.total(),
        "Mesas": lista,
    }), 200


@app.route("/mesas/<string:_id>", methods=["GET"])
def traer_mesa_por_id(_id):
    try:
        encontrada = control_mesa.trae_elemento(_id)
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


@app.route("/mesas/<string:_id>", methods=["PUT"])
def actualiza_mesa(_id):
    try:
        actualizada = control_mesa.actualiza(_id, request.get_json())
    except MesaInexistente:
        return jsonify({"Error": "Mesa a borrar no encontrada"}), 404
    else:
        return jsonify({
            "Mensaje": f"Mesa {actualizada.numero_mesa} actualizada exitosamente",
            "Mesa": actualizada.__dict__
        }), 200


@app.route("/mesas/<string:_id>", methods=["DELETE"])
def borra_mesa(_id):
    resultado = control_mesa.borra(_id)
    if resultado > 0:
        return jsonify({
            "Mensaje": "Mesa borrada exitosamente"
        }), 200
    else:
        return jsonify({
            "Error": "Mesa no encontrada"
        }), 404


app.run(host="127.0.0.1", port=5001, debug=True)
