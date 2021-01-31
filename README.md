#### Coding exercise:

### Terminal commands
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all

Make sure to run the initial migration commands to update the database.
    
    > python manage.py db init

    > python manage.py db migrate --message 'initial database migration'

    > python manage.py db upgrade


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

    For testing authorization, url for getting all user requires an admin token while url for getting a single
    user by public_id requires just a regular authentication.


### Coding exercise:

    >Write a Flask Web API with only 1 method called “ProcessPayment” that receives a request
    >like this



    >CreditCardNumber (mandatory, string, it should be a valid credit card number)
    >CardHolder: (mandatory, string)
    >ExpirationDate (mandatory, DateTime, it cannot be in the past)
    >SecurityCode (optional, string, 3 digits)
    >Amount (mandatoy decimal, positive amount)
    >The response of this method should be 1 of the followings based on
   

    >Payment is processed: 200 OK
    >The request is invalid: 400 bad request
    >Any error: 500 internal server error
    >The payment could be processed using different payment providers (external services)
    >called:
    

    >PremiumPaymentGateway
    >ExpensivePaymentGateway
    >CheapPaymentGateway.
    >The payment gateway that should be used to process each payment follows the next set of
    >business rules:
    >a) If the amount to be paid is less than £20, use CheapPaymentGateway.
    >b) If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
    >Otherwise, retry only once with CheapPaymentGateway.
    >c) If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times
    >in case payment does not get processed.
    >Recommendations:
    
    >The classes should be written in such way that they are easy to test.
    
    >Write as many tests as you think is enough to be certain about your solution works -
    >Use SOLID principles.
    
    >Decouple the logic the prediction logic from the API as much as possible