from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse
import mysql.connector
import csv

app = FastAPI()

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@S7905342439v9",
    database="HINDALCO_1D"
)
cursor = conn.cursor()

@app.post("/upload-data")
async def upload_data(file: UploadFile):
    # Read data from the uploaded CSV file
    contents = await file.read()
    decoded_contents = contents.decode("utf-8").splitlines()

    # Iterate over each row and insert into the database
    for row in csv.reader(decoded_contents):
        ticker, date, open_price, high, low, close = row
        query = "INSERT INTO ticker_data (ticker, date, open, high, low, close) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (ticker, date, open_price, high, low, close)
        cursor.execute(query, values)

    # Commit the changes
    conn.commit()

    return JSONResponse(content={"message": "Data uploaded successfully"})

@app.get("/get-data")
def get_data():
    # Fetch data from the database
    query = "SELECT * FROM ticker_data"
    cursor.execute(query)
    data = cursor.fetchall()

    return JSONResponse(content={"data": data})

# Close the connection when the application stops
@app.on_event("shutdown")
def shutdown_event():
    cursor.close()
    conn.close()
