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
    """
        This function enables a user to signup byt entering their password which will be able 
    """
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
    # source: https://docs.python.org/2/howto/regex.html
    if not re.match(r"[^@.]+@[^@]+\.[^@]+", email):
        return jsonify({'message': 'Invalid email address'}), 406
    # source: https://docs.python.org/2/howto/regex.html
    if not re.match(r"[A-Za-z0-9@#]{6,}", createPassword):
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
    """
        This function enables a user to login using their credentials that are stored in the database
        and they receive a token which they use to access the various other routes whose permissions they have.
    """
    user_data = request.get_json()

    email = user_data.get('email')
    password = user_data.get('password')

    if not email:
        return jsonify({'message': 'Missing email'}), 400
    if not password:
        return jsonify({'message': 'Missing password!'}), 400
    if password == User.validate_user(email, password):

        token = create_access_token(identity=user_auth)

        return jsonify({'token': token}), 200

    return jsonify({'message': 'Wrong email or password!'}), 401


@app.route('/app/v1/users/requests', methods=['POST'])
@jwt_required
def create_request():
    """ 
        this function enables a user create a request 
        it captures the length of all_requests list
        and set it as the first _id then increment it by one for each request's id
    """
    request_data = request.get_json()

    requesttype = request_data.get('requesttype')
    category = request_data.get('category')
    details = request_data.get('details')

    if not requesttype and len(requesttype.strip(" ")) != 0:
        return jsonify({'message': 'Missing request type'}), 400
    if not category and len(category.strip(" ")) != 0:
        return jsonify({'message': 'Missing request category'}), 400
    if not details and len(details.strip(" ")) != 0:
        return jsonify({'message': 'Missing request details'}), 400

    new_req = Request.add_request(current_user_email)
    # append new request to the list
    all_requests.append(new_req)

    return jsonify({
        'request': new_req.__dict__,
        'message': 'Request created successfully'
    }), 201


@app.route('/app/v1/users/requests', methods=['GET'])
@jwt_required
def get_requests():
    """
    This function enables a user to get back all their requests from the database
    which are identified by the current_user_email paramater

    Params: current_user_email is passed in the function and it takes the email
    that the user logged in with, decoded from the token they received
    """
    request_data = request.get_json()

    requesttype = request_data.get('requesttype')
    category = request_data.get('category')
    details = request_data.get('details')

    number_of_requests = len(all_requests)

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
@jwt_required
def get_request_by_id(requestid):
    """
    This function enables a user to get back a single request from the database
    which is identified by the requestid paramater

    Params: requestid is passed in the function and it takes the reqest id of the request 
    that is stored in the database and if it is not in the database, an error message is returned 
    """

    req_id = int(requestid)

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
            'message': 'Request does not exist'
        }), 400
    except ValueError:
        return jsonify({
            'message': 'Request does not exist'
        }), 400
    except TypeError:
        return jsonify({'message': 'Please enter a number!'
        }), 400
