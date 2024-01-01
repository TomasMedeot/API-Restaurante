from flask import request , jsonify
import datetime
import jwt
from functools import wraps
import os
from dotenv import load_dotenv

load_dotenv()

def generate_token(email, username):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'sub': email,
        'username': username
    }
    token = jwt.encode(payload, os.getenv("KEY") , algorithm='HS256')
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, os.getenv("KEY") , algorithms=['HS256'])
        except jwt.ExpiredSignatureError as e:
            print(f"Error de firma expirada: {e}")
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError as e:
            print(f"Error de token inválido: {e}")
            return jsonify({'message': 'Invalid token'}), 401

        return f(data, *args, **kwargs)

    return decorated