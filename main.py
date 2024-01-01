from flask import Flask , jsonify , request
import os
import token_module
import users
import database_module
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv("KEY")

database = database_module.DataBase(host=os.getenv("DB_HOST"),
                                    port=os.getenv("DB_PORT"),
                                    user=os.getenv("DB_USER"),
                                    password=os.getenv("DB_PASS"),
                                    db=os.getenv("DB_DB"))


# Ruta protegida que requiere un token válido
@app.route('/protected', methods=['GET'])
@token_module.token_required
def protected_route(current_user):
    return jsonify(logged_in_as=current_user), 200

# Ruta para obtener un token
@app.route('/get-token', methods=['GET'])
def get_token():
    username = request.authorization.username
    password = request.authorization.password

    # Verifica las credenciales (puedes reemplazar esto con tu propia lógica de autenticación)
    if username == 'usuario' and password == 'contraseña':
        token = token.generate_token(username)
        return jsonify({'token': token.decode('UTF-8')})

    return jsonify({'message': 'Authentication failed'}), 401

if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))