from uuid import uuid4
from sqlalchemy_utils import URLType
from app import db


class SocialLinkModel(db.Model):
    id = db.Column(db.String, default=uuid4, primary_key=True, unique=True)
    supply_id = db.Column(db.String, index=False, unique=False)
    provider = db.Column(db.String(120), index=False, unique=False)
    social_link = db.Column(URLType)

    def __repr__(self):
        return '<SocialLink {} -> {}>'.format(self.provider, self.supply_id)
