import unittest
from app import tracker
import json


class Requests(unittest.TestCase):
    def setUp(self):
        self.tester = tracker.app.test_client()

    def test_user_gets_requests(self):
        pass
    #     # this tests if the user can get the requests that have already been created
    #     request = dict(requesttype='requesttype',
    #                    category='category', details='details')

    #     reply = self.tester.get('/app/v1/users/requests')

    #     self.assertEqual(reply.status_code, 201)

    # def test_user_create_requests(self):
    #     # this tests if a user can create a request
    #     # create the request data
    #     user_request = ({
    #         'requesttype': 'replace',
    #         'category': 'water',
    #         'details': 'The pipe to the sink is overflowing'
    #     })
    #     response = self.tester.post(
    #         '/app/v1/users/requests', content_type='application/json', data=json.dumps(user_request))
    #     reply = json.loads(response.data.decode())

    #     self.assertEquals(reply['status'], 'OK')
    #     self.assertEquals(reply['message'], 'Request created successfully')
    #     self.assertEquals(reply.status_code, 201)

    # def test_user_modify_request(self):
    #     #this tests that a user can modify a request
    #     request = dict()


if __name__ == '__main__':
    unittest.main()
