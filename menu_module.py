import querys

def load_menu(type:str, filter:str, database:object):
    if type == 'category':
        if filter == None:
            list = []
            for category in database.datasearch(querys.read_category()):
                list.append({
                    'category_id':category[0],
                    'category_name': category[1]
                })
            return {'category':list}
        else:
            print(database.datasearch(querys.read_association(filter)))
            list = []
            for dish in database.datasearch(querys.read_association(filter)):
                list.append({
                    'menu_id': dish[0],
                    'dish_name': dish[1],
                    'price': dish[2],
                    'description': dish[3]
                })
            return {'category':list}
    elif type == 'menu':
        if filter == None:
            list = []
            for dish in database.datasearch(querys.read_menu()):
                list.append({
                    'menu_id': dish[0],
                    'dish_name': dish[1],
                    'price': dish[2],
                    'description': dish[3]
                })
            return {'menu':list}
        else:
            try:
                dish = database.datasearch(querys.read_dish(filter))[0]
                return {
                    'menu_id': dish[0],
                    'dish_name': dish[1],
                    'price': dish[2],
                    'description': dish[3]
                }
            except:
                return {
                    'menu_id': filter,
                    'dish_name': None,
                    'price': None,
                    'description': None
                }

def edit_menu(type:str, action:str, filter:str, data, database:object):
    if type == "menu":
        if action == "add":
            return database.datainsert(querys.add_menu(data['dish_name'],data['price'],data['description']))
        elif action == "update":
            return database.datainsert(querys.update_menu(filter,data['dish_name'],data['price'],data['description']))
        elif action == "delete":
            return database.datainsert(querys.delete_menu(filter))

    elif type == "category":
        if action == "add":
            return database.datainsert(querys.add_category(data['category_name']))
        elif action == "update":
            return database.datainsert(querys.update_category(filter,data['category_name']))
        elif action == "delete":
            for query in querys.delete_category(filter):
                if database.datainsert(query) != {'message':'DB correctly'}:
                    return {'message':'DB error'}           
            return {'message':'DB correctly'}
                

    elif type == "association":
        if action == "add":
            return database.datainsert(querys.add_association(data['category_id'], data['menu_id']))
        elif action == "delete":
            return database.datainsert(querys.delete_association(data['category_id'], data['menu_id']))