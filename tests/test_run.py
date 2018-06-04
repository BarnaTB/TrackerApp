import unittest
# from .. import app
from app import app
import json

class Requests(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_user_gets_requests(self):
        # this tests if the user can get the requests that have already been created
        a_request = dict(requesttype='requesttype',
                         category='category',
                         details='details')

        self.tester.post('/app/v1/users/requests',
                         content_type='application/json',
                         data=json.dumps(a_request))

        response = self.tester.get('/app/v1/users/requests')

        self.assertEqual(response.status_code, 201)
        #this tests if a user can create a request

    def test_user_create_requests(self):
        # this tests if a user can create a request
        # create the request data
        a_request = ({
            'requesttype': 'replace',
            'category': 'water',
            'details': 'The pipe to the sink is overflowing'
        })
        response = self.tester.post('/app/v1/users/requests',
                                content_type='application/json',
                                data=json.dumps(a_request))
        reply = json.loads(response.data.decode())

        self.assertEquals(reply['message'], 'Request created successfully')

    def test_user_modify_request(self):
        post_request = ({
            'requesttype': 'replace',
            'category': 'water',
            'details': 'my water meter is broken.'
        })

        # collect the data that is being passed
        put_request = ({
            'requesttype': 'repair',
            'category': 'electricity',
            'details': 'my power is unusually on and off'
        })

        self.tester.post('/app/v1/users/requests',
                         content_type='application/json',
                         data=json.dumps(dict(post_request)))

        post_response = self.tester.put('/app/v1/users/requests/1',
                                        content_type='application/json',
                                        data=json.dumps(dict(put_request)))

        post_reply = json.loads(post_response.data.decode())

        self.assertEquals(post_reply['message'], 'Editted successfully!')

    def test_user_gets_request_by_id(self):
        post_request = ({
            'requesttype': 'replace',
            'category': 'water',
            'details': 'my water meter is broken.'
        })

        # pass the collected data through the post method
        self.tester.post('/app/v1/users/requests',
                         content_type='application/json',
                         data=json.dumps(dict(post_request)))

        post_response = self.tester.get('/app/v1/users/requests/1',
                                        content_type='application/json',
                                        data=json.dumps(dict(post_request)))

        post_reply = json.loads(post_response.data.decode())

        self.assertEqual(post_reply['message'], 'Request fetched successfully!')

    

if __name__ == '__main__':
    unittest.main()
