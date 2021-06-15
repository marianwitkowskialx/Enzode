# Przykładowa aplikacji typu Rest API w Flasku
from flask import Flask, jsonify, Response, make_response
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

@app.after_request
def add_headers(response : Response):
    response.headers["Server"] = "My API server"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    response.headers["App-Id"] = "Enzode"
    return response

app.run(port=1234, debug=True)