from .. import db


class ProcessPayment(db.Model):
    """ Process Payment related details """
    __tablename__ = "ProcessPayment"

    id = db.Column(db.String(100), primary_key=True, nullable=False, autoincrement=True)
    creditcardnumber = db.Column(db.DECIMAL(16, 0), primary_key=True, nullable=False)
    cardholder = db.Column(db.String(100), primary_key=False, nullable=False)
    securitycode = db.Column(db.Integer,  nullable=False)    
    expirationdate = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'ProcessPayment {self.creditcardnumber}'
