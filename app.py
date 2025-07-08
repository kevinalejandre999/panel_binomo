from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

# Página web que muestra datos
@app.route("/")
def index():
    if not os.path.exists(DATA_FILE):
        data = {}
    else:
        with open(DATA_FILE) as f:
            data = json.load(f)
    return render_template("index.html", data=data)

# API para recibir datos del bot (POST)
@app.route("/update", methods=["POST"])
def update_data():
    if request.is_json:
        content = request.get_json()
        with open(DATA_FILE, "w") as f:
            json.dump(content, f, indent=4)
        return jsonify({"message": "Datos actualizados correctamente"}), 200
    return jsonify({"error": "Formato inválido. Se esperaba JSON."}), 400

if __name__ == "__main__":
    app.run(debug=True)
