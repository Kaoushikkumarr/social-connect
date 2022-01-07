from flask_restful import Resource
from controllers.SocialController import SocialSuite


class SocialSuiteAPI(Resource):

    def get(self):
        """GET method for work experience read"""
        social = SocialSuite()
        result = social.get_response_for_api()
        if result['response']:
            return result, 200
        elif result['status_code'] == 401:
            return result, 401
        return result, 202
