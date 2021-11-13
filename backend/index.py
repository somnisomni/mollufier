import os
from flask import Flask, request, jsonify
from mollufy import mollufy as mollufy_internal

server = Flask("mollufier")

@server.route("/mollufy", methods=["POST"])
def mollufy():
  print(request.get_json())

  if request.is_json:
    text = request.get_json()["sentence"]
    
    responseData = { "content": mollufy_internal(text) }
    return jsonify(responseData)

if __name__ == "__main__":
  port = 50000 if not os.environ["FLASK_PORT"] else int(os.environ["FLASK_PORT"])

  server.run(port=port)
