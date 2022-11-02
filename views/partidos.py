from flask import jsonify, request, Blueprint

from controllers.partidos import *
from models.partidos import *

control_partido = ControladorPartidos()
partidos_bp = Blueprint("partidos_blue", __name__)


@partidos_bp.route("/", methods=["GET"])
def partidos():
    lista = []
    for i in control_partido.trae_todo():
        lista.append(i.pasa_json())
    return jsonify({
        "Cantidad": control_partido.total(),
        "Partidos": lista,
    }), 200


@partidos_bp.route("/<string:_id>", methods=["GET"])
def traer_partido_por_id(_id):
    try:
        encontrada = control_partido.trae_elemento(_id)
    except PartidoInexistente:
        return jsonify({"Error": "Partido no encontrado"}), 404
    else:
        return jsonify(encontrada.pasa_json()), 200


@partidos_bp.route("/", methods=["POST"])
def crea_partido():
    creada = control_partido.crea(request.get_json())
    return jsonify({
        "Mensaje": "Partido creado exitosamente",
        "Partido": creada.pasa_json()
    }), 201


@partidos_bp.route("/<string:_id>", methods=["PUT"])
def actualiza_partido(_id):
    try:
        actualizada = control_partido.actualiza(_id, request.get_json())
    except PartidoInexistente:
        return jsonify({"Error": "Partido a actualizar no encontrado"}), 404
    else:
        return jsonify({
            "Mensaje": f"Partido {actualizada.nombre} actualizado exitosamente",
            "Partido": actualizada.pasa_json()
        }), 200


@partidos_bp.route("/<string:_id>", methods=["DELETE"])
def borra_partido(_id):
    try:
        resultado = control_partido.borra(_id)
    except PartidoInexistente:
        return jsonify({
            "Error": "Partido no encontrado"
        }), 404
    else:
        return jsonify({
            "Mensaje": "Partido borrado exitosamente"
        }), 200

