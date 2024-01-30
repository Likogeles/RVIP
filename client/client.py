from flask import Flask
import requests

app = Flask(__name__)

users = [{"id": 1, "name": "Ivan", "surname": "Srgeev"}]

print("123")

@app.route("/")
def index():
    response = requests.get("http://server-api")
    
    users = response.json()['users']
    
    # "http://server-api"

    table_text = """<table border='1px'><tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Surname</th>
                    </tr>"""
    for i in users:
        table_text += f"""<tr>
                        <td>{i['id']}</td>
                        <td>{i['name']}</td>
                        <td>{i['surname']}</td>
                        </tr>"""
    table_text += "</table>"

    return f"""<!DOCTYPE html>
            <html>
                <head>
                    <title>Пользователи</title>
                </head>
                <body>
                    <h1>Пользователи</h1>
                    {table_text}
                </body>
            </html>"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
