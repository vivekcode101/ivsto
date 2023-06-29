import pandas as pd
import mysql.connector
from mysql.connector import Error

# Your database connection details
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@S7905342439v9",
    database="HINDALCO_1D"
)

# Read the Excel file into a DataFrame
excel_data = pd.read_excel("HINDALCO_1D.xlsx")

# Iterate over the rows and insert the data
for index, row in excel_data.iterrows():
    # Convert 'datetime' to a string in the format 'YYYY-MM-DD HH:MM:SS'
    datetime_value = row['datetime'].strftime('%Y-%m-%d %H:%M:%S')
    close_value = row['close']
    high_value = row['high']
    low_value = row['low']
    open_value = row['open']
    instrument_value = row['instrument']

    # Prepare the SQL query
    sql_query = "INSERT INTO intern (datetime, close, high, low, open, instrument) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (datetime_value, close_value, high_value, low_value, open_value, instrument_value)

    try:
        # Execute the query
        cursor = db_connection.cursor()
        cursor.execute(sql_query, values)
        db_connection.commit()
    except Error as e:
        print(f"Error occurred: {e}")

# Close the database connection
db_connection.close()
