from flask import Flask, request, jsonify
import json
from app.models import Request, User
from app import app
from app.db import Mydb, Userdb
import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, decode_token
import re

all_requests = []
users = []


@app.route('/app/v1/auth/signup', methods=['POST'])
def register_user():
    # function to register a user
    user_data = request.get_json()

    hashed_password = generate_password_hash(user_data['confirmPassword'])

    email = user_data.get('email')
    createPassword = user_data.get('createPassword')
    confirmPassword = user_data.get('confirmPassword')

    if not email:
        return jsonify({'message': 'Please enter email!'}), 400
    if not createPassword:
        return jsonify({'message': 'Please enter password!'}), 400
    if not confirmPassword:
        return jsonify({'message': 'Please repeat password!'}), 400
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'message': 'Invalid email address'}), 406
    if not re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password):
        return jsonify({'message': 'Password not strong enough!'}), 406

    new_user = User(
        user_data['email'], user_data['createPassword'], hashed_password)

    if user_data['createPassword'] != user_data['confirmPassword']:
        return jsonify({
            'message': "Passwords don't match!"
        }), 406

    # new_user.add_user_table()
    data = new_user.create_user(user_data['email'], hashed_password)

    if not data:
        data = 'user created'
    return jsonify({
        'message': data
    }), 201


@app.route('/app/v1/auth/login', methods=['POST'])
def login():
    # function to login a user
    user_data = request.get_json()

    email = user_data.get('email')
    password = user_data.get('password')

    if not email:
        return jsonify({'message': 'Missing email'}), 400
    if not password:
        return jsonify({'message': 'Missing password!'}), 400

    user_auth = User.validate_user(email, password)

    token = create_access_token(identity=user_auth)

    return jsonify({'token': token})


@app.route('/app/v1/users/requests', methods=['POST'])
@jwt_required
def create_request():
    """ this function enables a user create a request """
    request_data = request.get_json()

    # add the data into the json object
    requesttype = request_data.get('requesttype')
    category = request_data.get('category')
    details = request_data.get('details')

    decoded = decode_token(token)

    """
        Capture the length of all_requests list
        and set it as the first _id then increment it by one for each request's id
    """

    if not requesttype and len(requesttype.strip(" ")) != 0:
        return jsonify({'message': 'Missing request type'}), 400
    if not category and len(category.strip(" ")) != 0:
        return jsonify({'message': 'Missing request category'}), 400
    if not details and len(details.strip(" ")) != 0:
        return jsonify({'message': 'Missing request details'}), 400

    # create a new request as an instance of the Request class
    new_req = Request(
        request_data['requesttype'], request_data['category'], request_data['details'])
    new_req.create_request(decoded)
    # append new request to the list
    all_requests.append(new_req)

    return jsonify({
        'request': new_req.__dict__,
        'message': 'Request created successfully'
    }), 201


@app.route('/app/v1/users/requests', methods=['GET'])
# this function enables a user to fetch their requests
@jwt_required
def get_requests():

    request_data = request.get_json()

    requesttype = request_data.get('requesttype')
    category = request_data.get('category')
    details = request_data.get('details')

    # collect the length of the list in which all requests are
    number_of_requests = len(all_requests)

    # check that the number of requests is not 0
    if number_of_requests > 0:
        get_them_all = Request
        get_them_all.fetch_all_requests()
        return jsonify({
            'requests': [a_request.__dict__ for a_request in all_requests],
            'message': 'Requests fetched successfully',
        }), 201
    return jsonify({
        'message': 'Requests fetch unsuccessful!'
    }), 400


@app.route('/app/v1/users/requests/<requestid>', methods=['GET'])
# this function enables a user get fetch a request by it's id
@jwt_required
def get_request_by_id(requestid):

    req_id = int(requestid)  # convert the requestid into an interger

    try:
        if isinstance(req_id, int):
            one_request = Request.fetch_request_by_id(requestid)
            return jsonify({
                'Request': one_request,
                'message': 'Request fetched successfully!'
            }), 201

    # this returns an error message if the requested id doesn't exist
    except IndexError:
        return jsonify({
            'message': 'Request does not exist',
        }), 400
    except ValueError:
        return jsonify({
            'message': 'Request does not exist',
        }), 400


@app.route('/app/v1/users/requests/<int:requestid>', methods=['PUT'])
@jwt_required
def modify_request(requestid):
    """
    # this function tests enables a user modify their request
    """
    number_of_requests = len(all_requests)

    if number_of_requests < 1:  # check for the number of requests
        return jsonify({
            'message': 'No requests to modify',
        }), 400

    else:

        request_data = request.get_json()

        # enter the attributes into the json object
        req_type = request_data.get('requesttype')
        req_category = request_data.get('category')
        req_details = request_data.get('details')

        for a_request in all_requests:
            """
            # loop through each request while checking if the passed id is equal
            # to any request id

            """
            if a_request._id == requestid:
                a_request.requesttype = req_type
                a_request.requesttype = req_category
                a_request.details = req_details

                return jsonify({
                    'request': a_request.__dict__,
                    'message': 'Editted successfully!',
                }), 200
