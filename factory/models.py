from factory import db

class Price(db.Model):

    __tablename__ = 'price'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)

    def __init__(self, value):
        self.value = value