from flask import Blueprint, request, jsonify
from db import get_db_connection

auth = Blueprint('auth', __name__)

@auth.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    user_name = data['user_name']
    email = data['email']
    password = data['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
    existing = cursor.fetchone()

    if existing:
        return jsonify({"message": "Email já cadastrado."}), 409

    cursor.execute('''
        INSERT INTO users (user_name, email, password)
        VALUES (%s, %s, %s)
        RETURNING id, user_name, email
    ''', (user_name, email, password))

    user = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({
        "message": "Usuário registrado com sucesso.",
        "user": {
            "id": user[0],
            "user_name": user[1],
            "email": user[2]
        }
    }), 201

@auth.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, user_name, email, password FROM users WHERE email = %s', (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user and user[3] == password:
        return jsonify({
            "message": "Login realizado com sucesso.",
            "user": {
                "id": user[0],
                "user_name": user[1],
                "email": user[2]
            }
        }), 200
    else:
        return jsonify({"message": "Credenciais inválidas."}), 401

@auth.route('/api/esqueci-senha', methods=['POST'])
def esqueci_senha():
    data = request.get_json()
    email = data['email']

    # Simulação
    return jsonify({"message": f"Instruções enviadas para o e-mail {email}."})

@auth.route('/api/login-google', methods=['POST'])
def login_google():
    # Simulação de login com Google
    data = request.get_json()
    google_email = data['email']
    user_name = data.get('user_name', 'GoogleUser')

    return jsonify({
        "message": "Login com Google bem-sucedido.",
        "user": {
            "email": google_email,
            "user_name": user_name
        }
    })

@auth.route('/api/test-db', methods=['GET'])
def test_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT 1')  # Testa se o banco responde
        cursor.close()
        conn.close()
        return jsonify({"message": "Conexão com o banco bem-sucedida!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500