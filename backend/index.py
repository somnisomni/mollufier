import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from mollufy import mollufy as mollufy_internal

server = Flask("mollufier")
CORS(server)

@server.route("/mollufy", methods=["POST"])
def mollufy():
  print(request.get_json())

  if request.is_json:
    text = request.get_json()["sentence"]
    
    responseData = { "content": mollufy_internal(text) }
    return jsonify(responseData)

if __name__ == "__main__":
  host = "127.0.0.1" if not os.environ["FLASK_HOST"] else os.environ["FLASK_HOST"]
  port = 50000 if not os.environ["FLASK_PORT"] else int(os.environ["FLASK_PORT"])

  server.run(host=host, port=port)
