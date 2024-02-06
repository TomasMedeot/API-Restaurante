def look_user(username:str):
    return f'SELECT * FROM USERS WHERE EMAIL = "{username}";'

def create_user(username:str, password:str, email: str):
    return f'INSERT INTO USERS (USERNAME, USER_PASSWORD, EMAIL) VALUES ("{username}", "{password}", "{email}");'

def add_menu(dish_name:str, price:float, description:str):
    return f"INSERT INTO MENU (DISH_NAME, PRICE, DESCRIPTION) VALUES ('{dish_name}', {price}, '{description}');"

def add_category(category_name:str):
    return f"INSERT INTO CATEGORY (CATEGORY_NAME) VALUES ('{category_name}');"

def add_association(category_id:int, menu_id:int):
    return f"INSERT INTO MENU_CATEGORY (MENU_ID, CATEGORY_ID) VALUES ({menu_id}, {category_id});"

def read_menu():
    return f"SELECT * FROM MENU;"

def read_dish(menu_id:int):
    return f"SELECT * FROM MENU WHERE MENU_ID = {menu_id};"

def read_category():
    return f"SELECT * FROM CATEGORY;"

def read_association(category_id:int):
    return f"SELECT M.* FROM MENU M JOIN MENU_CATEGORY MC ON M.MENU_ID = MC.MENU_ID JOIN CATEGORY C ON MC.CATEGORY_ID = C.CATEGORY_ID WHERE C.CATEGORY_ID = {category_id};"

def update_menu(menu_id:int, dish_name:str, price:float, description:str):
    return f"UPDATE MENU SET DISH_NAME = '{dish_name}', PRICE = {price}, DESCRIPTION = '{description}' WHERE MENU_ID = {menu_id};"

def update_category(category_id:int, category_name:str):
    return f"UPDATE CATEGORY SET CATEGORY_NAME = '{category_name}' WHERE CATEGORY_ID = {category_id};"

def delete_menu(menu_id:int):
    return f"DELETE FROM MENU WHERE MENU_ID = {menu_id};"

def delete_category(category_id:int):
    return [f"DELETE FROM MENU_CATEGORY WHERE CATEGORY_ID = {category_id};", f"DELETE FROM CATEGORY WHERE CATEGORY_ID = {category_id};"]

def delete_association(category_id:int, menu_id:int):
    return f"DELETE FROM MENU_CATEGORY WHERE MENU_ID = {menu_id} AND CATEGORY_ID = {category_id};"