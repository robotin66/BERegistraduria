from flask import Flask, jsonify
from views.mesas import mesas_bp
from views.partidos import partidos_bp
from views.candidatos import candidatos_bp
from views.resultados import resultados_bp


app = Flask(__name__)


@app.route("/", methods=["GET"])
def ping():
    return jsonify({"Mensaje": "Servidor corriendo"}), 200


app.register_blueprint(mesas_bp, url_prefix="/mesas")
app.register_blueprint(partidos_bp, url_prefix="/partidos")
app.register_blueprint(candidatos_bp, url_prefix="/candidatos")
app.register_blueprint(resultados_bp, url_prefix="/resultados")

app.run(host="127.0.0.1", port=5001, debug=True)
