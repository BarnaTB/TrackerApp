from flask import Flask, request, jsonify
class User_request:
    def __init__(self, _id, requesttype, category, details):
        self._id = _id
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


class User:
    def __init__(self, email, createPassword, confirmPassword):
        self.email = email
        self.createPassword = createPassword
        self.confirmPassword = confirmPassword
    
    def get_email(self):
        return self.email

    def get_createPassword(self):
        return self.createPassword
    
    def get_confirmPassword(self):
        return self.confirmPassword