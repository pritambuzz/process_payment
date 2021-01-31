# test_hello_add.py

import pytest
import requests
import json

from app.settings import FLASK_RUN_HOST, FLASK_RUN_PORT

url = "http://{}:{}".format(FLASK_RUN_HOST, FLASK_RUN_PORT)


def test_endpoint_for_invalid_request_type():
    response = requests.get("{}/processpayment".format(url))
    assert response.status_code >= 400


def test_payment_no_data():
    card_data = {}
    response = requests.post("{}/processpayment".format(url), data=json.dumps(card_data),
                             headers={"Content-Type": "application/json"})
    assert response.status_code == 400


def test_payment_invalid_argument():
    # testing api when request body has invalid argument, as compared to argument which is required
    card_data = dict(CreditCardNumbers="1234123412341234", CardHoldewr="Pritam Patil", SecurityCode="777", ExpirationDate="2020/1/1", Amount=222.2)
    response = requests.post("{}/processpayment".format(url), data=json.dumps(card_data), headers={"Content-Type": "application/json"})
    assert response.status_code == 400


def test_payment_ext_invalid_credit_card_info():
    # testing for various cases when CreditCardNumber value is different, checking validity of credit
    # card numbers
    card_data_1 = {"CreditCardNumber": "er1236ijiojwqw45","CardHolder":"Pritam Patil","SecurityCode": "777",
"ExpirationDate": "2020/1/1","Amount": 999.9}
    card_data_2 = {"CreditCardNumber": "7890123456123456", "CardHolder": "Pritam Patil", "SecurityCode": "777",
                   "ExpirationDate": "2022/11/12", "Amount": 999.9}
    response_1 = requests.post("{}/processpayment".format(url), data=json.dumps(card_data_1), headers={"Content-Type":"application/json"})
    response_2 = requests.post("{}/processpayment".format(url), data=json.dumps(card_data_2), headers={"Content-Type": "application/json"})
    
    assert response_1.status_code == 400
    assert response_2.status_code == 200
    
    
def test_valid_input_data_for_various_amount():
    # testing the cases where for different amount input different external payment method invoke
    card_data_1 = {"CreditCardNumber": "7890123456123456", "CardHolder": "Pritam Patil", "SecurityCode": "777",
                   "ExpirationDate": "2022/11/12", "Amount": 19}
    card_data_2 = {"CreditCardNumber": "7890123456123456", "CardHolder": "Pritam Patil", "SecurityCode": "777",
                   "ExpirationDate": "2022/11/12", "Amount": 333}
    card_data_3 = {"CreditCardNumber": "7890123456123456", "CardHolder": "Pritam Patil", "SecurityCode": "777",
                   "ExpirationDate": "2022/11/12", "Amount": 666}
    
    response_1 = requests.post("{}/processpayment".format(url), data=json.dumps(card_data_1), headers={"Content-Type":"application/json"})
    response_2 = requests.post("{}/processpayment".format(url), data=json.dumps(card_data_2), headers={"Content-Type":"application/json"})
    response_3 = requests.post("{}/processpayment".format(url), data=json.dumps(card_data_3), headers={"Content-Type":"application/json"})
    
    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert response_3.status_code == 200


def test_payment_ext_exp_date():
    card_data_1 = {"CreditCardNumber": "er1236ijiojwqw45", "CardHolder": "Pritam Patil", "SecurityCode": "777",
                   "ExpirationDate": "2029/9/9", "Amount": 999.9}
    card_data_2 = {"CreditCardNumber": "7890123456123456", "CardHolder": "Pritam Patil", "SecurityCode": "777",
                   "ExpirationDate": "2019/11/12", "Amount": 999.9}
    
    response_1 = requests.post("{}/processpayment".format(url), data=json.dumps(card_data_1), headers={"Content-Type": "application/json"})
    response_2 = requests.post("{}/processpayment".format(url), data=json.dumps(card_data_2),
                               headers={"Content-Type": "application/json"})
    
    assert response_1.status_code == 200
    assert response_2.status_code == 400


def test_security_code():
    card_data_1 = {"CreditCardNumber": "er1236ijiojwqw45", "CardHolder": "Pritam Patil", "SecurityCode": "777",
                   "ExpirationDate": "2029/9/9", "Amount": 999.9}
    card_data_2 =  {"CreditCardNumber": "er1236ijiojwqw45", "CardHolder": "Pritam Patil", "ExpirationDate": "2029/9/9", "Amount": 999.9}
    card_data_3 = {"CreditCardNumber": "er1236ijiojwqw45", "CardHolder": "Pritam Patil", "SecurityCode": 444,
                   "ExpirationDate": "2029/9/9", "Amount": 999.9}

    response_1 = requests.post("{}/processpayment".format(url), data=json.dumps(card_data_1),
                               headers={"Content-Type": "application/json"})
    
    response_2 = requests.post("{}/processpayment".format(url), data=json.dumps(card_data_2),
                               headers={"Content-Type": "application/json"})
    response_3 = requests.post("{}/processpayment".format(url), data=json.dumps(card_data_3),
                               headers={"Content-Type": "application/json"})
    assert response_1.status_code == 200
    assert response_2.status_code == 200
    assert response_3.status_code == 400