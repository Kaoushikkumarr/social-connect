import os
from flask_migrate import Migrate
from flask_restful import Api
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config_manager.config_manager import FileConfigManager
from utils.request_controller import RequestsController

app = Flask(__name__)

CORS(app)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:p@192.168.43.141:5432/social_link_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Consul based Configurations
os.environ['CONSUL_HOST'] = 'localhost'
os.environ['CONSUL_PORT'] = '8500'
os.environ['CONSUL_PATH'] = 'integration/'
os.environ['CONSUL_HTTP_SCHEME'] = 'http'

if 'L2_CONFIG_PATH' in os.environ and os.environ['L2_CONFIG_PATH'] != 'None':
    configs = FileConfigManager(os.environ.get('L2_CONFIG_PATH'))
else:
    print('No Configuration Manager Found')


db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

from routes import social, social_link
from models.social_link_model import SocialLinkModel


# Collaboration API Signatures
api.add_resource(social.SocialSuiteAPI, '/this_is_test_api_for_collaborate')
api.add_resource(social_link.SocialLinkRead, '/social/<supply_id>')
api.add_resource(social_link.SocialLinkWrite, '/social')
api.add_resource(social_link.FetchSocialLinkAPI, '/<supply_id>/<provider>')
