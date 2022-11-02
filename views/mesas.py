from flask import jsonify, request, Blueprint

from controllers.mesas import *
from models.mesas import *

control_mesa = ControladorMesas()
mesas_bp = Blueprint("mesas_blue", __name__)


@mesas_bp.route("/", methods=["GET"])
def mesas():
    lista = []
    for i in control_mesa.trae_todo():
        lista.append(i.pasa_json())
    return jsonify({
        "Cantidad": control_mesa.total(),
        "Mesas": lista,
    }), 200


@mesas_bp.route("/<string:_id>", methods=["GET"])
def traer_mesa_por_id(_id):
    try:
        encontrada = control_mesa.trae_elemento(_id)
    except MesaInexistente:
        return jsonify({"Error": "Mesa no encontrada"}), 404
    else:
        return jsonify(encontrada.pasa_json()), 200


@mesas_bp.route("/", methods=["POST"])
def crea_mesa():
    creada = control_mesa.crea(request.get_json())
    return jsonify({
        "Mensaje": "Mesa creada exitosamente",
        "Mesa": creada.pasa_json()
    }), 201


@mesas_bp.route("/<string:_id>", methods=["PUT"])
def actualiza_mesa(_id):
    try:
        actualizada = control_mesa.actualiza(_id, request.get_json())
    except MesaInexistente:
        return jsonify({"Error": "Mesa a actualizar no encontrada"}), 404
    else:
        return jsonify({
            "Mensaje": f"Mesa {actualizada.numero_mesa} actualizada exitosamente",
            "Mesa": actualizada.pasa_json()
        }), 200


@mesas_bp.route("/<string:_id>", methods=["DELETE"])
def borra_mesa(_id):
    try:
        resultado = control_mesa.borra(_id)
    except MesaInexistente:
        return jsonify({
            "Error": "Mesa no encontrada"
        }), 404
    else:
        return jsonify({
            "Mensaje": "Mesa borrada exitosamente"
        }), 200

