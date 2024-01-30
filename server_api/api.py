from flask import Flask
import psycopg2

host = "0.0.0.0"
user = "admin"
password = "root"
db_name = "users"
port=5003

app = Flask(__name__)

connection = None

def update_users():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )
    
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM Users;')
        print(cursor.fetchall())
    connection.close()



@app.route("/")
def index():
    update_users()
    return {"users": [{"id": 1, "name": "Ivan", "surname": "Srgeev"},
                      {"id": 2, "name": "Sergey", "surname": "Ivanov"},
                      {"id": 3, "name": "Petr", "surname": "Mihailov"},
                      {"id": 4, "name": "Mari", "surname": "Dubrovsky"}]}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
