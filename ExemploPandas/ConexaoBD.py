import mysql.connector
from mysql.connector import errorcode

class ConexaoBancoDeDados():
    def conecta_banco(self):
        try:
            db_connection = mysql.connector.connect(host='localhost', user='root', password='1234', database='Apartamento')
            print("Conexão com o banco de Dados feita!")
            return db_connection  # Retorna a conexão
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database não existe")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuário ou senha incorretos!")
            else:
                print(error)

    def insert_banco(self, cod_ap, cidade, metros, quartos, banheiro, estacionamento, animais, aluguel, iptu, seguranca):
        try:
            bd = self.conecta_banco()  # Abre a conexão
            if bd is not None:  # Verifica se a conexão foi bem-sucedida
                cursor = bd.cursor()
                sql = "INSERT INTO apartamento (codigo_Apartamento, cidade, metros_quadrados, quartos, banheiro, estacionamento, animais, valor_aluguel, valor_iptu, valor_seguranca) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (cod_ap, cidade, metros, quartos, banheiro, estacionamento, animais, aluguel, iptu, seguranca))
                bd.commit()  # realiza as alterações
                print("Dados inseridos no banco!")
        except mysql.connector.Error as error:
            print("Não foi possível inserir os dados:", error)
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'bd' in locals():
                bd.close()  # Feche a conexão

    def consulta_banco(self,id):
        try:
            bd = self.conecta_banco()  # Abre a conexão
            if bd is not None:  # Verifica se a conexão foi bem-sucedida
                cursor = bd.cursor()
                sql = "SELECT CONCAT('Cidade: ', cidade, ', ', quartos, ' quartos e ', banheiro, ' banheiro(s)') AS descricao FROM apartamento WHERE codigo_Apartamento = %s"
                cursor.execute(sql, (id,))
                resultado = cursor.fetchall()  # Recupera os resultados da consulta
                print( resultado)
            
        except mysql.connector.Error as error:
            print("Não foi possível inserir os dados:", error)
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'bd' in locals():
                bd.close()  # Feche a conexão


            


