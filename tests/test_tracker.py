import unittest
from app import tracker
import json


class Requests(unittest.TestCase):
    def setUp(self):
        self.tester = tracker.app.test_client()

    def test_user_gets_requests(self):
        # this tests if the user can get the requests that have already been created
        request = dict(requesttype='requesttype',
                       category='category', details='details')

        expected_message = 'Request view succesful!'

        reply = self.tester.get('/app/v1/users/requests')

        self.assertEqual(reply.status_code, 201)
        #this tests if a user can create a request

    def test_user_create_requests(self):
        request = dict(requesttype='requesttype', category='category', details='details')
        reply = self.tester.post('/app/v1/users/requests', content_type='application/json', data=json.dumps(request))

        self.assertEqual(reply.status_code, 201)

    

if __name__ == '__main__':
    unittest.main()
