import re
import datetime
from decimal import Decimal


def validate_card(card):
    if not re.search(r"^[456]\d{3}(-?\d{4}){3}$", card) or re.search(r"(\d)\1{3}", re.sub("-", "", card)):
        return False
    return True


class BaseCardDetails:
    def __init__(self):
        self.CreditCardNumber = None
        self.CardHolder = None
        self.ExpirationDate = None
        self.SecurityCode = None
        self.Amount = None


class Card(BaseCardDetails):
    def __init__(self):
        super(Card, self).__init__()

    def verify_input(self, **kwargs):
        if len(str(kwargs['CreditCardNumber'])) < 16:
            print("invalid credit card number")
            response_object = {
                'message': 'invalid credit card number.',
            }
            return response_object, 400

        if len(str(kwargs['SecurityCode'])) < 3 or len(str(kwargs['SecurityCode'])) > 3:
            print("Invalid Security Code")
            response_object = {
                'message': 'Invalid Security Code.',
            }
            return response_object, 400

        print("input is verified.")
        self.__map_to_card(**kwargs)
        return True

    def __map_to_card(self, **kwargs):
        self.CreditCardNumber = kwargs.get('CreditCardNumber', None)
        self.Amount = kwargs.get('Amount', None)
        self.CardHolder = kwargs.get('CardHolder', None)

        self.SecurityCode = kwargs.get('SecurityCode', None)
        self.ExpirationDate = kwargs.get('ExpirationDate', None)

        print("mapping of user input is done sucessfully.")
        return True
