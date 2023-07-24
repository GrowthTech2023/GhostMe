# Video model
# Get API to a video processor - mp4, webm
# example compress a high res and once reaady to upload , send the original video

from .models import db, User

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('videos', lazy=True))

    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    filename = db.Column(db.String(100), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    