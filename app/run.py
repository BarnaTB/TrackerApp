from flask import Flask, request, jsonify
import json
import random
from models import User_request
# create and import the User_request class from the models file

app = Flask(__name__)

all_requests = []


@app.route('/app/v1/users/requests', methods=['POST'])
# this function enables a user create a request
def create_request():
    request_data = request.get_json()
    # return jsonify({'message': 'hello world'})

    # add the data into the json object
    requesttype = request_data.get('requesttype')
    category = request_data.get('category')
    details = request_data.get('details')

    """
        Capture the length of all_requests list
        and set it as the first _id
    """
    _id = request_data.get('_id')
    _id = len(all_requests)

    _id += 1  # increment by 1 since the initial length is 0

    # check if each required field is present in the data
    if not requesttype:
        return jsonify({'message': 'Missing request type'}), 204
    if not category:
        return jsonify({'message': 'Missing request category'}), 204
    if not details:
        return jsonify({'message': 'Missing request details'}), 204
    if not _id:
        return jsonify({'message': 'Missing request id'}), 204

    # create a new request as an instance of the User_request class
    new_request = User_request(_id, requesttype, category, details)

    all_requests.append(new_request)  # append new request to the list

    return jsonify({
        'request': new_request.__dict__,
        'message': 'Request created successfully'
    }), 201


@app.route('/app/v1/users/requests', methods=['GET'])
# this function enables a user to fetch their requests
def get_requests():
    # collect the length of the list in which all requests are
    number_of_requests = len(all_requests)

    # check that the number of requests is not 0
    if number_of_requests > 0:
        return jsonify({
            'requests': [a_request.__dict__ for a_request in all_requests],
            'message': 'Requests fetched successfully',
            'status': 'OK'
        }), 201
    return jsonify({
        'status': 'FAIL',
        'message': 'Requests fetch unsuccessful!'
    }), 400


@app.route('/app/v1/users/requests/<requestid>', methods=['GET'])
# this function enables a user get fetch a request by it's id
def get_request_by_id(requestid):

    req_id = int(requestid)  # convert the requestid into an interger

    try:
        if isinstance(req_id, int):
            return jsonify({
                'id': all_requests[req_id-1]._id,
                'requesttype': all_requests[req_id-1].requesttype,
                'category': all_requests[req_id-1].category,
                'details': all_requests[req_id-1].details,
                'message': 'Request fetched successfully!'
            }), 201

    # this returns an error message if the requested id doesn't exist
    except IndexError:
        return jsonify({
            'message': 'Request does not exist',
            'status': 'FAIL'
        }), 400
    except ValueError:
        return jsonify({
            'message': 'Request does not exist',
            'status': 'FAIL'
        }), 400


@app.route('/app/v1/users/requests/<int:requestid>', methods=['PUT'])
def modify_request(requestid):
    """
    this function tests enables a user modify their request
    """
    if len(all_requests) < 1:  # check for the number of requests
        return jsonify({
            'message': 'No requests to modify',
            'Status': 'FAIL'
        }), 400

    else:

        request_data = request.get_json()

        # enter the attributes into the json object
        req_type = request_data.get('requesttype')
        req_category = request_data.get('category')
        req_details = request_data.get('details')

        for a_request in all_requests:
            """
            loop through each request while checking if the passed id is equal
            to any request id

            """
            if a_request._id == requestid:
                a_request.requesttype = req_type
                a_request.requesttype = req_category
                a_request.details = req_details

                return jsonify({
                    'requesttype': a_request.requesttype,
                    'category': a_request.category,
                    'details': a_request.details,
                    'message': 'Editted successfully!',
                    'status': 'OK'
                }), 200


if __name__ == '__main__':
    app.run(debug='True')
