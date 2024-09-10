import mysql.connector
from mysql.connector import Error
from datetime import datetime

class CidadesDAO:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def _connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def listar_cidades(self):
        connection = self._connect()
        if connection:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM Cidades"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        return []

    def atualizar_temperatura(self, cidade, temperatura):
        connection = self._connect()
        if connection:
            cursor = connection.cursor()
            query = """
            UPDATE Cidades
            SET temperatura = %s, status_data = %s
            WHERE cidade = %s
            """
            data = (temperatura, datetime.now(), cidade)
            cursor.execute(query, data)
            connection.commit()
            cursor.close()
            connection.close()

    def adicionar_cidade(self, cidade, pais):
        connection = self._connect()
        if connection:
            cursor = connection.cursor()
            query = """
            INSERT INTO Cidades (cidade, pais, temperatura, status_data)
            VALUES (%s, %s, %s, %s)
            """
            data = (cidade, pais, None, datetime.now())
            cursor.execute(query, data)
            connection.commit()
            cursor.close()
            connection.close()
