from flask import Flask, jsonify, request

from models.mesas import Mesas

app = Flask(__name__)

mesa = [
    Mesas(
        _id=1,
        num_mesa=1,
        ced_inscritas=111,
    ),
    Mesas(
        _id=2,
        num_mesa=2,
        ced_inscritas=222,
    )

]


def encontrar_indice(lista, encontrado):
    


@app.route("/", methods=["GET"])
def ping():
    return jsonify({"Mensaje": "Servidor corriendo"}), 200


@app.route("/mesas", methods=["GET"])
def mesas():
    lista = []
    for i in mesa:
        lista.append(i.__dict__)
    return jsonify({
        "Mesas": lista,
        "Total": len(lista)
    }), 200


@app.route("/mesas/<int:num_mesa>", methods=["GET"])
def traer_mesa_por_id(num_mesa):
    for i in mesa:
        if i.numero_mesa == num_mesa:
            return jsonify(i.__dict__)
    return jsonify({"Error": "Mesa no encontrada"}), 404


@app.route("/mesas/", methods=["POST"])
def crea_mesa():
    body = request.get_json()
    creada = Mesas(
        _id=body["_id"],
        num_mesa=body["num_mesa"],
        ced_inscritas=body["ced_inscritas"],
    )
    mesa.append(creada)
    return jsonify({
        "Mensaje": f"Mesa {creada.numero_mesa} creada exitosamente",
        "Mesa": creada.__dict__
    }), 201


@app.route("/mesas/<int:num_mesa>", methods=["PUT"])
def actualiza_mesa(num_mesa):
    body = request.get_json(num_mesa)
    encontrada = None
    for i in mesa:
        if i.numero_mesa == num_mesa:
            encontrada = i
        if not i:
            return jsonify({"Error": "Mesa a actualizar no encontrada"}), 404
    encontrada._id = body["_id"]
    encontrada.numero_mesa = body["num_mesa"]
    encontrada.cedulas_inscritas = body["ced_inscritas"]
    return jsonify({
        "Mensaje": f"Mesa {encontrada.numero_mesa} actualizada exitosamente",
        "Mesa": encontrada.__dict__
    }), 200


@app.route("/mesas/<int:num_mesa>", methods=["DELETE"])
def borra_mesa(num_mesa):
    indice = 0
    encontrada = -1
    for i in mesa:
        if i.numero_mesa == num_mesa:
            encontrada = indice
        indice += 1
    if encontrada < 0 or encontrada > len(mesa):
        return jsonify({"Error": "Mesa a borrar no encontrada"}), 404
    mesa.pop(encontrada)
    return jsonify({
        "Mensaje": f"Mesa {num_mesa} borrada exitosamente",
    }), 200


app.run(host="127.0.0.1", port=5001, debug=True)
