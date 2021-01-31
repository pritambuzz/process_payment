from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.process_payment import api as process_payment_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Process Payment API',
          version='1.0',
          description='Process Payment API'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(process_payment_ns, path='/processpayment')
api.add_namespace(auth_ns)
