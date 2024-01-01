def look_user (username: str):
    return f'SELECT * FROM USERS WHERE EMAIL = "{username}";'

def create_user(username:str, password:str, email: str):
    return f'INSERT INTO USERS (USERNAME, USER_PASSWORD, EMAIL) VALUES ("{username}", "{password}", "{email}");'