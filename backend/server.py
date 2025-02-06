from flask import Flask, request, jsonify
import json
import os
import hashlib

app = Flask(__name__)

USER_DB_FILE = "users.db"

def load_users():
    """Carica gli utenti dal database."""
    if not os.path.exists(USER_DB_FILE):
        return {}
    with open(USER_DB_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    """Salva gli utenti nel database."""
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    """Crea un hash SHA256 della password."""
    return hashlib.sha256(password.encode()).hexdigest()

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    users = load_users()

    if data["username"] in users:
        return jsonify({"message": "❌ Username già registrato!"}), 400

    role = "admin" if not users else "user"
    users[data["username"]] = {"password": hash_password(data["password"]), "role": role}
    save_users(users)

    return jsonify({"message": f"✅ Registrazione completata! Sei stato registrato come {role}."})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    users = load_users()

    if data["username"] not in users or users[data["username"]]["password"] != hash_password(data["password"]):
        return jsonify({"message": "❌ Autenticazione fallita!"}), 401

    return jsonify({"message": f"✅ Autenticazione riuscita! Ruolo: {users[data['username']]['role']}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
