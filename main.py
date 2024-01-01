from flask import Flask , jsonify , request
import os
import token_module
import users
import database_module
import querys
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv("KEY")

database = database_module.DataBase(host=os.getenv("DB_HOST"),
                                    port=os.getenv("DB_PORT"),
                                    user=os.getenv("DB_USER"),
                                    password=os.getenv("DB_PASS"),
                                    db=os.getenv("DB_DB"))


@app.route('/user', methods=['GET'])
@token_module.token_required
def protected_route(current_user):
    return jsonify(logged_in_as=current_user), 200


@app.route('/login', methods=['GET'])
def login():
    email = request.authorization.username
    password = request.authorization.password

    if users.validate_email_address(email):
        data = database.datasearch(querys.look_user(email))[0]
        print(data)
        if users.verify_password(password, data[2]):
            token = token_module.generate_token(email)
            return jsonify({'token': token})

    return jsonify({'message': 'Authentication failed'}), 401


@app.route('/register', methods=['POST'])
def register():
    email = request.get_json()['email']
    password = request.get_json()['password']
    username = request.get_json()['username']


    if users.validate_email_address(email):
        hashed_password = users.hash_password(password)
        return jsonify(database.datainsert(querys.create_user(username,hashed_password,email)))
    else:
        return jsonify({'message': 'invalid email'})

if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))