import uuid
import datetime
import json
from flask import jsonify, make_response
from app.main import db
from ..model.processpayment import ProcessPayment as Payment
from app.main.model.user import User


def save_payment_details(data):
    payment = Payment.query.filter_by(creditcardnumber=data['CreditCardNumber']).first()
    if not payment:
        new_payment = Payment(
            id=str(uuid.uuid4()),
            creditcardnumber=data['CreditCardNumber'],
            cardholder=data['CardHolder'],
            securitycode=data['SecurityCode'],
            expirationdate=data['ExpirationDate'],
            amount=data['Amount'],
            status="completed"
        )
        save_changes(new_payment)
        response_object = {
            'CreditCardNumber': data['CreditCardNumber'],
            'CardHolder': data['CardHolder'],
            'SecurityCode': data['SecurityCode'],
            'ExpirationDate': data['ExpirationDate'],
            'Amount': data['Amount'],
            'Status': 'completed'
        }
        return response_object
    else:
        response_object = {
            'CreditCardNumber': data['CreditCardNumber'],
            'CardHolder': data['CardHolder'],
            'SecurityCode': data['SecurityCode'],
            'ExpirationDate': data['ExpirationDate'],
            'Amount': data['Amount'],
            'Status': 'failed (Credit card number already exists.)',
            'message': 'Credit card number already exists.',
        }
        return response_object, 409


def save_changes(data):
    db.session.add(data)
    db.session.commit()
