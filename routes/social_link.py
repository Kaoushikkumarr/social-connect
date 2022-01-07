import requests
from flask_restful import Resource
from flask import request
from app import db
from models.social_link_model import SocialLinkModel


class SocialLinkWrite(Resource):

    def post(self):
        """ POST method for CommentWrite API. """
        if request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                data = SocialLinkModel(
                    supply_id=data['supply_id'],
                    provider=data['provider'],
                    social_link=data['social_link']
                )
                db.session.add(data)
                db.session.commit()
                return {
                    "message": f"Supply_id: {data.supply_id}, 'Provider': {data.provider} has been created successfully."}
            else:
                return {"error": "The request payload is not in JSON format"}


class SocialLinkRead(Resource):

    def get(self, supply_id):
        """GET method for CommentWrite API. """
        data = SocialLinkModel.query.get_or_404(supply_id)
        if request.method == 'GET':
            response = {
                'supply_id': data.supply_id,
                'provider': data.provider,
                'social_link': data.social_link,
            }
            return {'response': True, 'results': [response]}

    def put(self, supply_id):
        """PUT method for CommentWrite API. """
        results = SocialLinkModel.query.get_or_404(supply_id)
        if request.method == 'PUT':
            data = request.get_json()
            results.supply_id = data['supply_id']
            results.provider = data['provider']
            results.social_link = data['social_link']
            db.session.add(results)
            db.session.commit()
            return {"message": f"Supply_id: {results.supply_id} & Provider: {results.provider} has been updated "
                               f"successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    def delete(self, supply_id):
        """DELETE method for CommentWrite API. """
        results = SocialLinkModel.query.get_or_404(supply_id)
        if request.method == 'DELETE':
            db.session.delete(results)
            db.session.commit()
            return {"message": f"Supply_id: {results.supply_id} successfully deleted."}


class FetchSocialLinkAPI(Resource):

    def get(self, supply_id, provider):
        results = SocialLinkModel.query.get_or_404(
            supply_id, provider
        )
        if results:
            if provider == "stackoverflow":
                provider_user_id = results.social_link.split("/")[-2]
                url = "https://api.stackexchange.com/2.2/users/{}?&site=stackoverflow".format(provider_user_id)
            else:
                provider_user_id = results.social_link.split("/")[-1]
                url = "https://api.github.com/users/{}".format(provider_user_id)
            response = requests.get(url)
            results = response.json()
            return {'response': 'success', 'results': results}, 200
