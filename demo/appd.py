from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = mysql.connector.connect(
            host='mysql',
            user='root',
            password='rootpass',
            database='testdb'
        )
        return "Connected to MySQL!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

