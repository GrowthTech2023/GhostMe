# Subscription model
# read https://medium.com/@mishraranjeet122/integrate-stripe-payment-with-a-card-in-python-e90989d39bca
# https://stripe.com/docs/development/quickstart?lang=python

# subscription_model.py

import stripe
from .models import db, User

stripe.api_key = "sk_test_..." # Set secret API key

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('subscriptions', lazy=True))

    stripe_subscription_id = db.Column(db.String(255)) 
    stripe_price_id = db.Column(db.String(255))

    @classmethod
    def create(cls, user, price_id):
        subscription = stripe.Subscription.create(
            customer=user.stripe_customer_id,
            items=[{"price": price_id}]
        )

        return cls(
            user_id=user.id,
            stripe_subscription_id=subscription.id,
            stripe_price_id=price_id
        )

    def cancel(self):
        stripe.Subscription.delete(self.stripe_subscription_id)
        self.query.filter_by(id=self.id).delete()