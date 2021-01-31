from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        # 'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class ProcessPaymentDto:
    api = Namespace('ProcessPayment', description='ProcessPayment')
    process = api.model('ProcessPayment', {
        'CreditCardNumber': fields.Integer(required=True, description='CreditCardNumber'),
        'CardHolder': fields.String(required=True, description='CardHolder'),
        'SecurityCode': fields.Integer(required=True, description='SecurityCode'),
        'ExpirationDate': fields.String(required=True, description='ExpirationDate'),
        'Amount': fields.Float(required=True, description='Amount'),
        'Status': fields.String(required=False, description='status')
    })
