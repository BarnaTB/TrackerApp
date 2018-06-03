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


# class Request_data(User_request):
#     def create_request_data(self, _id, requesttype, category, details):
#         request_data = request.get_json()

#         req_type = request_data.get('requesttype')
#         req_category = request_data.get('category')
#         req_details = request_data.get('details')

#         return request_data
