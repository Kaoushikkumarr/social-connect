"""Social_Suite_Controller"""


class SocialSuite:
    """This is a class for Social Suite Test."""

    def get_response_for_api(self):
        """ GET method for Social Suite."""
        coll_1 = "I'm from Social"
        coll_2 = "Suite Controller Class"
        result = coll_1 + coll_2
        return {
            'response': result
        }
