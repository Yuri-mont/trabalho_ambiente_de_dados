import pandas as pd
import mysql.connector as sql
import csv

def main():
    try:
        connection = sql.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='hospital'
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            cursor = connection.cursor()
            query = "SELECT * FROM your_table"
            cursor.execute(query)
            rows = cursor.fetchall()
            csv_file = "arquivo_da_query_de_exemplo_.csv"

            with open(csv_file, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([i[0] for i in cursor.description])  
                csv_writer.writerows(rows)
            print(f"Results exported to '{csv_file}'")

    except sql.Error as e:
        print(f"Error connecting to MySQL database: {e}")

    finally:
        # Closing the connection when done
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

    df = pd.read_csv('tabela inicial.csv',sep=';')
    df.to_sql('',connection,if_exists='append')
    print(df)

if __name__ == '__main__':
    main()