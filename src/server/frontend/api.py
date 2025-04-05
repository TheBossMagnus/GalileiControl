from flask import Flask, jsonify
import json

app = Flask(__name__)


def carica_database():
    with open("database.json", "r") as file:
        return json.load(file)


@app.route("/api/dispositivi", methods=["GET"])
def ottieni_dispositivi():
    """Restituisce l'elenco di tutti i dispositivi"""
    database = carica_database()

    if "dispositivi" not in database:
        return jsonify({"errore": "Formato database non valido"}), 500

    return jsonify(database["dispositivi"])


@app.route("/api/dispositivi/<hostname>", methods=["GET"])
def ottieni_dispositivo(hostname):
    """Restituisce i dati di uno specifico dispositivo tramite hostname"""
    database = carica_database()

    if "dispositivi" not in database:
        return jsonify({"errore": "Formato database non valido"}), 500

    if hostname not in database["dispositivi"]:
        return jsonify({"errore": f"Dispositivo {hostname} non trovato"}), 404

    return jsonify(database["dispositivi"][hostname])


@app.route("/api/test", methods=["GET"])
def test():
    database = carica_database()
    if database is not None:
        return jsonify({"messaggio": "Api funzionante"}), 200
    else:
        return jsonify({"errore": "Errore nel caricamento del database"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
