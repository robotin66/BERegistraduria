from flask import jsonify, request, Blueprint

candidatos_bp = Blueprint("candidatos_blue", __name__)


@partidos_bp.route("/", methods=["GET"])
def candidatos():
    ...
