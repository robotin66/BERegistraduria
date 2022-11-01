from flask import jsonify, request, Blueprint

resultados_bp = Blueprint("resultados_blue", __name__)


@resultados_bp.route("/", methods=["GET"])
def resultados():
    ...