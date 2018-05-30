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
