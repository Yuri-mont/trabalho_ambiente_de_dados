import pandas as pd
import mysql.connector as sql
from sqlalchemy import create_engine
import csv

def main():
    try:

        engine = create_engine('mysql://root:12345678@localhost/hospital')

        # Connect to the database
        conn = engine.connect()
        connection = sql.connect(
            host='localhost',
            user='root',
            password='12345678',
            database='hospital'
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            cursor = connection.cursor()
            query = "SELECT * FROM pessoa"
            cursor.execute(query)
            rows = cursor.fetchall()
            query2 = "select a.id AS 'id do atendimento', p.nome AS 'Nome do Paciente',d.nome AS 'Nome do Medico' from Atendimento a JOIN pessoa p ON a.CPF JOIN Doutores d ON a.CRM = d.CRM;"
            cursor.execute(query2)
            rows2 = cursor.fetchall()
            csv_file = "arquivo_da_query_de_exemplo_.csv"
            csv_file2 = "arquivo_da_query_de_exemplo2_.csv"

            with open(csv_file, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([i[0] for i in cursor.description])  
                csv_writer.writerows(rows)
            print(f"Results exported to '{csv_file}'")

            with open(csv_file2, 'w', newline='') as file2:
                csv_writer = csv.writer(file2)
                csv_writer.writerow([i[0] for i in cursor.description])  
                csv_writer.writerows(rows2)
            print(f"Results exported to '{csv_file2}'")

            #df = pd.read_csv('C:/Users/yuric/OneDrive/Documentos/code/py/trabalho_ambiente_de_dados/tabela_inicial.csv',sep=';')
            #df.to_sql('pessoa',conn,if_exists='append',index=False)
            #print(df)

    except sql.Error as e:
        print(f"Error connecting to MySQL database: {e}")

    finally:
        # Closing the connection when done
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

    

if __name__ == '__main__':
    main()
    
