from flask import jsonify, request, Blueprint

from controllers.partidos import *
from models.partidos import PartidoInexistente

control_partido = ControladorPartidos()
partidos_bp = Blueprint("partidos_blue", __name__)


@partidos_bp.route("/", methods=["GET"])
def partidos():
    lista = []
    for i in control_partido.trae_todo():
        lista.append(i.__dict__)
    return jsonify({
        "Cantidad": control_partido.total(),
        "Partidos": lista,
    }), 200


@partidos_bp.route("/<string:_id>", methods=["GET"])
def traer_partido_por_id(_id):
    try:
        encontrada = control_partido.trae_elemento(_id)
    except PartidoInexistente:
        return jsonify({"Error": "Partido no encontrada"}), 404
    else:
        return jsonify(encontrada.__dict__), 200


@partidos_bp.route("/", methods=["POST"])
def crea_partido():
    creada = control_partido.crea(request.get_json())
    return jsonify({
        "Mensaje": "Partido creada exitosamente",
        "Partido": creada.__dict__
    }), 201


@partidos_bp.route("/<string:_id>", methods=["PUT"])
def actualiza_Partido(_id):
    try:
        actualizada = control_partido.actualiza(_id, request.get_json())
    except PartidoInexistente:
        return jsonify({"Error": "Partido a borrar no encontrada"}), 404
    else:
        return jsonify({
            "Mensaje": f"Partido {actualizada.nombre} actualizada exitosamente",
            "Partido": actualizada.__dict__
        }), 200


@partidos_bp.route("/<string:_id>", methods=["DELETE"])
def borra_Partido(_id):
    resultado = control_partido.borra(_id)
    if resultado > 0:
        return jsonify({
            "Mensaje": "Partido borrada exitosamente"
        }), 200
    else:
        return jsonify({
            "Error": "Partido no encontrada"
        }), 404
