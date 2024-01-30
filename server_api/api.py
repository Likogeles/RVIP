from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return {"users": [{"id": 1, "name": "Ivan", "surname": "Srgeev"},
                      {"id": 2, "name": "Sergey", "surname": "Ivanov"},
                      {"id": 3, "name": "Petr", "surname": "Mihailov"},
                      {"id": 4, "name": "Mari", "surname": "Dubrovsky"}]}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
