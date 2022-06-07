import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from mollufy import mollufy as mollufy_internal


server = Flask("mollufier")
CORS(server, origins=["*" if not "FE_DEPLOY_HOST" in os.environ else os.environ["FE_DEPLOY_HOST"]])

@server.route("/mollufy", methods=["POST"])
def mollufy():
  if request.is_json:
    requestContent = request.get_json()

    text = requestContent["sentence"]
    ignoreNounLengthLimit = False

    if "options" in requestContent:
      requestOptions = requestContent["options"]

      if "ignoreNounLengthLimit" in requestOptions: ignoreNounLengthLimit = requestOptions["ignoreNounLengthLimit"]
    
    responseData = { "content": mollufy_internal(text, ignoreNounLengthLimit) }
    return jsonify(responseData)

if __name__ == "__main__":
  host = "127.0.0.1" if not "FLASK_HOST" in os.environ else os.environ["FLASK_HOST"]
  port = 50000 if not "FLASK_PORT" in os.environ else int(os.environ["FLASK_PORT"])

  server.run(host=host, port=port)
