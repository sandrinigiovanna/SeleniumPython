import pymysql
from datetime import datetime, timedelta

class DBConnection:
    def __init__(self):
        # Substitua pelos detalhes corretos de conexão
        self.connection = pymysql.connect(
            host='your_host',
            user='your_user',
            password='your_password',
            database='cpjwcs',
            cursorclass=pymysql.cursors.DictCursor
        )
    
    def open_connection(self):
        if not self.connection.open:
            self.connection.ping(reconnect=True)

    def close_connection(self):
        if self.connection.open:
            self.connection.close()

    def execute_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def execute_non_query(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()

class RoboStatusDAO:
    conn = DBConnection()

    @staticmethod
    def obter_data_do_email_enviado(nome_robo):
        RoboStatusDAO.conn.open_connection()
        
        sql = f"SELECT data_email_enviado FROM robo_status WHERE nome_robo = '{nome_robo}' AND status = 1"
        table = RoboStatusDAO.conn.execute_query(sql)
        
        RoboStatusDAO.conn.close_connection()

        if not table or not table[0]['data_email_enviado']:
            data_parametro = datetime.now() - timedelta(days=1)
        else:
            data_parametro = datetime.strptime(table[0]['data_email_enviado'], '%Y-%m-%d').replace(hour=0, minute=0, second=0)

        return data_parametro

    @staticmethod
    def atualizar_data_do_email_enviado(data, nome_robo):
        sql = f"UPDATE robo_status SET data_email_enviado = '{data}' WHERE nome_robo = '{nome_robo}'"
        RoboStatusDAO.conn.open_connection()
        RoboStatusDAO.conn.execute_non_query(sql)
        RoboStatusDAO.conn.close_connection()

    @staticmethod
    def indicar_erro_no_robo(nome_robo, mensagem_erro):
        sql = f"UPDATE robo_status SET status = 2, problema = '{mensagem_erro}' WHERE nome_robo = '{nome_robo}'"
        RoboStatusDAO.conn.open_connection()
        RoboStatusDAO.conn.execute_non_query(sql)
        RoboStatusDAO.conn.close_connection()

    @staticmethod
    def robo_iniciou(nome_robo):
        sql = f"UPDATE robo_status SET inicio = CURRENT_TIMESTAMP, fim = NULL WHERE nome_robo = '{nome_robo}'"
        RoboStatusDAO.conn.open_connection()
        RoboStatusDAO.conn.execute_non_query(sql)
        RoboStatusDAO.conn.close_connection()

    @staticmethod
    def robo_finalizou(nome_robo):
        sql = f"UPDATE robo_status SET fim = CURRENT_TIMESTAMP WHERE nome_robo = '{nome_robo}'"
        RoboStatusDAO.conn.open_connection()
        RoboStatusDAO.conn.execute_non_query(sql)
        RoboStatusDAO.conn.close_connection()

    @staticmethod
    def obter_status_do_robo(nome_robo):
        RoboStatusDAO.conn.open_connection()
        try:
            sql = f"SELECT nome_intranet, status, problema FROM robo_status WHERE nome_robo = '{nome_robo}'"
            table = RoboStatusDAO.conn.execute_query(sql)
            if not table:
                return None

            status = {
                "NomeRobo": nome_robo,
                "NomeRoboIntranet": table[0]["nome_intranet"],
                "Status": table[0]["status"],
                "Problema": table[0]["problema"]
            }
            return status
        except Exception as ex:
            raise ex
        finally:
            RoboStatusDAO.conn.close_connection()
