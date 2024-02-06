from flask import Flask , jsonify , request
import os
import token_module
import menu_module
import users
import database_module
import querys
import extra_functions
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv("KEY")

database = database_module.DataBase(host=os.getenv("DB_HOST"),
                                    port=os.getenv("DB_PORT"),
                                    user=os.getenv("DB_USER"),
                                    password=os.getenv("DB_PASS"),
                                    db=os.getenv("DB_DB"))

@app.route('/menu/<type>/<filter>', methods=['GET'])
@app.route('/menu/<type>', methods=['GET'])
def menu(type: str, filter: int =None):
    return jsonify(menu_module.load_menu(type, filter, database)), 200

@app.route('/menu_edit/<type>/<action>/<filter>', methods=['POST'])
@app.route('/menu_edit/<type>/<action>', methods=['POST'])
@extra_functions.add_variables(database=database)
@token_module.token_required
def menu_edit(user, type:str, action:str, database:object, filter:int =None):
    return jsonify(menu_module.edit_menu(type, action, filter, request.get_json(), database)), 200

@app.route('/user', methods=['GET'])
@token_module.token_required
def user(current_user):
    return jsonify(logged_in_as=current_user), 200

@app.route('/login', methods=['GET'])
def login():
    email = request.authorization.username
    password = request.authorization.password

    if users.validate_email_address(email):
        data = database.datasearch(querys.look_user(email))
        if len(data) == 1:
            fdata = users.format(data)
            if users.verify_password(password, fdata['HASHED PASSWORD']):
                token = token_module.generate_token(email,fdata['USERNAME'])
                return jsonify({'token': token}), 200

    return jsonify({'message': 'Authentication failed'}), 401

@app.route('/register', methods=['POST'])
def register():
    email = request.get_json()['email']
    password = request.get_json()['password']
    username = request.get_json()['username']

    if users.validate_email_address(email):
        hashed_password = users.hash_password(password)
        print(hashed_password)
        database.datainsert(querys.create_user(username,hashed_password,email))
        return jsonify({'message': 'User registed'}), 200
    else:
        return jsonify({'message': 'invalid email'}), 401

if __name__ == "__main__":
    app.run(host=os.getenv("HOST") ,port=os.getenv("PORT") ,debug=os.getenv("DEBUG"))