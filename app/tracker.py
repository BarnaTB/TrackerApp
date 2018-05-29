from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/app/users/requests', methods=['POST', 'GET'])
def fetch():
    pass

@app.route('/app/v1/users/requests', methods=['POST'])
def post():
    pass
