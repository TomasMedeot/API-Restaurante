import pymysql

class DataBase:
    def __init__(self,host: str, port:str ,user: str,password: str,db: str):
        '''This function need context whit the information for the conecction'''
        self.conn = pymysql.connect(host=str(host),user=user,password=password,db=db)
        self.cursor = self.conn.cursor()

    #Is the conection to the database for insert , update or delete
    def datainsert(self,accion:str):
        '''This function need the sql instruction, returns 'msj':'DB correctly'//'DB error' '''
        try:
            self.cursor.execute(accion)
            self.conn.commit()
            return {'msj':'DB correctly'}
        except:
            return {'msj':'DB error'}

    #Is the connection to the database for read information
    def datasearch(self,accion:str):
        '''This function need the sql instruction, returns 'msj':'DB correctly'//'DB error' '''
        try:
            self.cursor.execute(accion)
            self.dates = self.cursor.fetchall()
            return self.dates
        except:
            return {'msj':'DB error'}