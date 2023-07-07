# Subscription model
# read https://medium.com/@mishraranjeet122/integrate-stripe-payment-with-a-card-in-python-e90989d39bca
# https://stripe.com/docs/development/quickstart?lang=python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    stripe_customer_id = Column(String)
    plan_id = Column(String)
    status = Column(String)
    user = relationship('User', backref='subscription')
