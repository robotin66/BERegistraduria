from flask import jsonify, request, Blueprint

from controllers.resultados import *
from models.resultados import *

control_resultado = ControladorResultados()
resultados_bp = Blueprint("resultados_blue", __name__)


@resultados_bp.route("/", methods=["GET"])
def resultados():
    lista = []
    for i in control_resultado.trae_todo():
        lista.append(i.pasa_json())
    return jsonify({
        "Cantidad": control_resultado.total(),
        "Resultados": lista,
    }), 200


@resultados_bp.route("/<string:_id>", methods=["GET"])
def traer_resultado_por_id(_id):
    try:
        encontrada = control_resultado.trae_elemento(_id)
    except ResultadoInexistente:
        return jsonify({"Error": "Resultado no encontrado"}), 404
    else:
        return jsonify(encontrada.pasa_json()), 200


@resultados_bp.route("/", methods=["POST"])
def crea_resultado():
    try:
        creado = control_resultado.crea(request.get_json())
    except MesaInexistente:
        return jsonify({"Error": "Mesa no existe"}), 400
    except CandidatoInexistente:
        return jsonify({"Error": "Candidato no existe"}), 400
    return jsonify({
        "Mensaje": "Resultado creado exitosamente",
        "Resultado": creado.pasa_json()
    }), 201


@resultados_bp.route("/<string:_id>", methods=["PUT"])
def actualiza_resultado(_id):
    try:
        actualizado = control_resultado.actualiza(_id, request.get_json())
    except ResultadoInexistente:
        return jsonify({"Error": "Resultado a actualizar no encontrado"}), 404
    except MesaInexistente:
        return jsonify({"Error": "Mesa a actualizar no encontrado"}), 404
    except CandidatoInexistente:
        return jsonify({"Error": "Candidato a actualizar no encontrado"}), 404
    else:
        return jsonify({
            "Mensaje": f"Partido {actualizado.nombre} actualizado exitosamente",
            "Partido": actualizado.pasa_json()
        }), 200


@resultados_bp.route("/<string:_id>", methods=["DELETE"])
def borra_resultado(_id):
    try:
        resultado = control_resultado.borra(_id)
    except ResultadoInexistente:
        return jsonify({"Error": "Resultado no encontrado"}), 404
    else:
        return jsonify({
            "Mensaje": "Partido borrado exitosamente"
        }), 200

