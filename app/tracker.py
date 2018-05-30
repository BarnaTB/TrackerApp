from flask import Flask, request, jsonify
import json
import random
from models import User_request

app = Flask(__name__)

all_requests = []


@app.route('/app/v1/users/requests', methods=['POST'])
# this function enables a user create a request
def create_request():
    request_data = request.get_json()
    # return jsonify({'message': 'hello world'})
    
    #add the data into the json object
    requesttype = request_data.get('requesttype')
    category = request_data.get('category')
    details = request_data.get('details')
    
    _id = request_data.get('_id')
    _id = random.randint(1, 1000)

    #check if each required field is present in the data
    if not requesttype:
        return jsonify({'message': 'Missing request type'}), 400
    if not category:
        return jsonify({'message': 'Missing request category'}), 400
    if not details:
        return jsonify({'message': 'Missing request details'}), 400
    if not _id:
        return jsonify({'message': 'Missing request id'}), 400

    new_request = User_request(_id, requesttype, category, details)

    all_requests.append(new_request)

    return jsonify({
        'requesttype': new_request.requesttype,
        'category': new_request.category,
        'details': new_request.details,
        'status': 'OK',
        'message': 'Request created successfully'
    }), 201


@app.route('/app/v1/users/requests', methods=['GET'])
# this function enables a user to fetch their requests
def get_requests():
    # test which method is being used to return the data
    number_of_requests = len(all_requests)
    if request.method == 'GET' and number_of_requests != 0:
        return jsonify({
            'requesttype': all_requests[0].requesttype,
            'category': all_requests[0].category,
            'details': all_requests[0].details,
            'status': 'OK',
            'message': 'Requests fetched successfully'
        }), 200
    else:
        return jsonify({
            'status': 'OK',
            'message': 'Requests fetch unsuccessful!'
        }), 200


if __name__ == '__main__':
    app.run(debug='True')
