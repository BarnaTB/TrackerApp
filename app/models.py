from flask import Flask, request, jsonify
from app.db import Mydb, Userdb
import uuid

db = Mydb()

class Request:
    def __init__(self, requesttype, category, details):
        # self._id = _id
        self.requesttype = requesttype
        self.category = category
        self.details = details

    def get_Id(self):
        return self._id

    def get_requesttype(self):
        return self.requesttype

    def get_category(self):
        return self.category

    def get_details(self):
        return self.details
    
    def get_db():
        return self.db

    @staticmethod
    def add_request(current_user_email):

        db.crt_request(self.requesttype,self.category, self.details, self.current_user_email)

        # return Mydb.get_single_request()

    @staticmethod
    def fetch_all_requests():
        All_requests = []
        for _request in db.get_all_requests():
            All_requests.append(_request)
            
        return Allrequests

    @staticmethod
    def fetch_request_by_id(requestid):
        _request = db.get_single_request(requestid)
        req_dict = {}
        req_dict['id'] = _request[0][0]
        req_dict['requesttype'] = _request[0][1]
        req_dict['category'] = _request[0][2]
        req_dict['details'] = _request[0][3]

        return req_dict

    def change_request(self, requestid, requesttype, category, details):
        _request = {
            'id': requestid,
            'requesttype': requesttype,
            'category': category,
            'details': details
        }
        db.modify_request(_request['id'], _request['requesttype'], _request['category'], _request['details'])

        return db.get_single_request(_request['id'])

class User:
    def __init__(self, email, createPassword, confirmPassword):
        self.email = email
        self.createPassword = createPassword
        self.confirmPassword = confirmPassword
        # self.db = Userdb()
    
    def get_email(self):
        return self.email

    def get_createPassword(self):
        return self.createPassword
    
    def get_confirmPassword(self):
        return self.confirmPassword
    
    def get_db():
        return self.db
    
    def add_user_table(self):
        return db.create_user_table()

    def create_user(self, email, confirmPassword):
        # userid = uuid.uuid1()
        user = {
            'email': email,
            'password': confirmPassword 
        }
        try:
            return Userdb().add_user(email, confirmPassword)
        except:
            return {'message': 'User already exists'}
    @staticmethod
    def validate_user(email, password):
        """ return a user by email """
        get_user = Userdb()
        user = get_user.get_user_by_email(email, password)

        if user is None:
            return jsonify({'message': 'Oops! Wrong credentials!'})
        
        return user