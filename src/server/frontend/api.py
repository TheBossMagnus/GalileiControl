import json

from flask import Flask, jsonify

app = Flask(__name__)


def carica_database():
    with open(
        r"/home/tbmag/code/telecomunicazioni/Raspberry/raspberry-pi-bluetooth-server/database.json",
    ) as file:
        return json.load(file)


@app.route("/api/dispositivi/nomi", methods=["GET"])
def ottieni_nomi_dispositivi():
    """Restituisce solo i nomi (hostname) di tutti i dispositivi"""
    database = carica_database()

    if "dispositivi" not in database:
        return jsonify({"errore": "Formato database non valido"}), 500

    nomi_dispositivi = list(database["dispositivi"].keys())
    return jsonify(nomi_dispositivi)


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
    return jsonify({"errore": "Errore nel caricamento del database"}), 500


@app.route("/api/status", methods=["GET"])
def stato():
    """Restituisce se un dispositivo è in situazione critica"""
    database = carica_database()
    for dispositivo in database["dispositivi"].items():
        if dispositivo.get("connessione_internet") is False:
            return jsonify({"stato": "true"}), 200
        return jsonify({"stato": "false"}), 200
    return None


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
