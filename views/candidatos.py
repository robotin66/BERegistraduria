from flask import jsonify, request, Blueprint

from controllers.candidatos import *
from models.candidatos import *

control_candidato = ControladorCandidatos()
candidatos_bp = Blueprint("candidatos_blue", __name__)


@candidatos_bp.route("/", methods=["GET"])
def candidatos():
    lista = []
    for i in control_candidato.trae_todo():
        lista.append(i.pasa_json())
    return jsonify({
        "Cantidad": control_candidato.total(),
        "Mesas": lista,
    }), 200


@candidatos_bp.route("/<string:_id>", methods=["GET"])
def traer_candidato_por_id(_id):
    try:
        encontrado = control_candidato.trae_elemento(_id)
    except CandidatoInexistente:
        return jsonify({"Error": "Candidato no encontrado"}), 404
    else:
        return jsonify(encontrado.pasa_json()), 200


@candidatos_bp.route("/", methods=["POST"])
def crea_candidato():
    try:
        creada = control_candidato.crea(request.get_json())
    except PartidoInexistente:
        return jsonify({"Error": "Partido no existe"}), 400
    else:
        return jsonify({
            "Mensaje": "Candidato creado exitosamente",
            "Candidato": creada.pasa_json()
        }), 201


@candidatos_bp.route("/<string:_id>", methods=["PUT"])
def actualiza_candidato(_id):
    try:
        actualizar = control_candidato.actualiza(_id, request.get_json())
    except CandidatoInexistente:
        return jsonify({"Error": "Candidato  no existente"}), 400
    except PartidoInexistente:
        return jsonify({"Error": "Partido  no existente"}), 400
    else:
        return jsonify({
            "Mensaje": "Candidato actualizado exitosamente",
            "Candidato": actualizar.pasa_json()
        }), 201


@candidatos_bp.route("/<string:_id>", methods=["DELETE"])
def borra_candidato(_id):
    try:
        resultado = control_candidato.borra(_id)
    except CandidatoInexistente:
        return jsonify({
            "Error": "Candidato no encontrado"
        }), 404
    else:
        return jsonify({
            "Mensaje": "Candidato borrado exitosamente"
        }), 200


@candidatos_bp.route("/<string:candidato>/partido/<string:partido>", methods=["PUT"])
def asigna_partido(candidato, partido):
    try:
        resul_candi = control_candidato.asigna_partido(candidato, partido)
    except CandidatoInexistente:
        return jsonify({"Error": "Candidato no existe"})
    except PartidoInexistente:
        return jsonify({"Error": "Partido no existe"})
    else:
        return jsonify({
            "Mensaje": "Candidato asignado a partido",
            "Candidato": resul_candi.pasa_json()
        })
