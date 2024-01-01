import bcrypt
from validate_email import validate_email

def hash_password(password: str):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def verify_password(password: str, hashed_password: str):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def validate_email_address(email: str):
    try:
        is_valid = validate_email(email)
        return is_valid
    except:
        is_valid =False
        return is_valid