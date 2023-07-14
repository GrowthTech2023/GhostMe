# Social media platform model

from .models import db, User

class SocialPlatform(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('social_platforms', lazy=True))
    
    platform = db.Column(db.String(20), nullable=False)
    access_token = db.Column(db.String(255))