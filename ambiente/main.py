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
            password='',
            database='hospital'
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            cursor = connection.cursor()
            query = "SELECT * FROM pessoa"
            cursor.execute(query)
            rows = cursor.fetchall()
            csv_file = "arquivo_da_query_de_exemplo_.csv"

            with open(csv_file, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([i[0] for i in cursor.description])  
                csv_writer.writerows(rows)
            print(f"Results exported to '{csv_file}'")

            df = pd.read_csv('/trabalho_ambiente_de_dados/tabela_inicial.csv',sep=';')
            df.to_sql('pessoa',conn,if_exists='append',index=False)
            print(df)

    except sql.Error as e:
        print(f"Error connecting to MySQL database: {e}")

    finally:
        # Closing the connection when done
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

    

if __name__ == '__main__':
    main()
    
