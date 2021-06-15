# Przykładowa aplikacji typu Rest API w Flasku
from flask import Flask, jsonify, Response, make_response, request
from datetime import datetime

app = Flask("MyApi")

# generyczna odpowiedź z API
def create_reponse(message, code):
    resp : Response = make_response(message, code)
    resp.mimetype = "application/json"
    return resp

@app.route("/alive", methods=["GET"])
def alive():
    res = jsonify({
        "status" : "OK",
        "ts" : datetime.utcnow()
    })
    return create_reponse(res, 200)

@app.route("/echo/<string:msg>")
def echo(msg):
    return f"Odpowiadam: {msg}"

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/get", methods=['GET'])
def get():
    """
    http://127.0.0.1:1234/get?p1=123&p2=abc
    """
    p1 = request.args.get("p1","empty p1")
    p2 = request.args.get("p2","empty p2")
    res = jsonify({
        "p1": p1,
        "p2": p2
    })
    return create_reponse(res, 200)

@app.route("/post", methods=['POST'])
def post():
    p1 = request.form.get("p1","empty p1")
    p2 = request.form.get("p2","empty p2")
    res = jsonify({
        "p1": p1,
        "p2": p2
    })
    return create_reponse(res, 200)

@app.route("/json", methods=['POST'])
def json():
    data = request.json
    res = jsonify({
        "imie": data.get("imie"),
        "nazwisko": data.get("nazwisko")
    })
    return create_reponse(res, 200)

@app.after_request
def add_headers(response : Response):
    response.headers["Server"] = "My API server"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    response.headers["App-Id"] = "Enzode"
    return response

app.run(port=1234, debug=True)