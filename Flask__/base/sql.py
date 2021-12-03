import mysql.connector
# utilizando as seguintes configurações
# MODIFIQUE PARAMETROS LOCAIS AQUI(nas strings seguintes):
user = 'root'
password = ''
host = '127.0.0.1'

class banco:
    def __init__(self):
        self.cnx = mysql.connector.connect(user=user, password=password, host=host)

    def executar(self,comando, parametros):
        cs = self.cnx.cursor()
        cs.execute(comando, parametros)
        self.cnx.commit()
        cs.close()
        return True

class SQL:
    def __init__(self, esquema):
        self.cnx = mysql.connector.connect(user=user, password=password,
                                           host=host,
                                           database=esquema)

    def executar(self, comando, parametros):
        cursor = self.cnx.cursor()
        cursor.execute(comando, parametros)
        self.cnx.commit()
        cursor.close()
        return True

    def consultar(self, comando, parametros):
        cursor = self.cnx.cursor()
        cursor.execute(comando, parametros)
        return cursor

    def __del__(self):
        self.cnx.close()
