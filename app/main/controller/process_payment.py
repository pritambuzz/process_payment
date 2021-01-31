import json

from app.main.util.decorator import admin_token_required
from app.main.util.dto import ProcessPaymentDto
from flask import Blueprint, Flask, abort, jsonify, render_template, request
from flask_restx import Resource

from ..service.gateway import GatewayPayment
from ..service.payment import Card
from ..service.payment_service import save_payment_details

api = ProcessPaymentDto.api
_ProcessPayment = ProcessPaymentDto.process

@api.route('')
class processpayment(Resource):
    @api.expect(_ProcessPayment, validate=True)
    @api.response(201, 'ProcessPayment is successfull.')
    @api.doc('payment')
    @api.marshal_with(_ProcessPayment)
    @admin_token_required
    def post(self):
        """ProcessPayment"""
        data = request.get_data(as_text=True)
        if not data:
            abort(400)
        request_data = json.loads(data)

        card_data = Card()
        print("request data {}".format(request_data))
        try:
            # verifying all the request data 
            if not card_data.verify_input(**request_data):
                print("card data invalid")
                response_object = {
                    'message': 'Invalid card details.',
                }
                return response_object, 409
                abort(400)
        except Exception as e:
            print(e)
            abort(400)
        try:
            # payment begins
            print("payment status started")
            payment_status = GatewayPayment(card_data.Amount, card_data)
            print("payment process started")

            payment_sccessfull = payment_status.make_payment()
            if payment_sccessfull:
                return save_payment_details(data=json.loads(data))
            else:
                abort(400)
        except Exception as e:
            print(e)
            abort(500)

