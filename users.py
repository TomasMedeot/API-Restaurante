import bcrypt
from validate_email import validate_email

def hash_password(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def validate_email_address(email: str):
    try:
        return validate_email(email)
    except:
        return False

def format(database_response: tuple):
    return {"USER_ID":database_response[0][0],
            "USERNAME":database_response[0][1],
            "HASHED PASSWORD":database_response[0][2],
            "EMAIL":database_response[0][3]}