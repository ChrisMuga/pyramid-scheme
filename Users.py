# python imports
import random
import json

# pyramid imports
from pyramid.response import Response

# sql-alchemy
from sqlalchemy.exc import DatabaseError

# Model imports

from Models.User import User
from Models.DB import DB


# TODO: Fetch Users = Read
# TODO: Update Users Info
# TODO: Delete User(s)
# TODO: Create new_user API


class AppUser:

    @staticmethod
    def hello_world(request):
        return Response('Hello World!')

    @staticmethod
    def index(request):
        return Response("We start here...")

    @staticmethod
    def create(request):
        # fetch from request
        random_id = random.randint(1, 1e9)
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email_address = request.POST["email_address"]
        phone_number = request.POST["phone_number"]

        # create instance of mapped class
        user = User(id=random_id,
                    first_name=first_name,
                    last_name=last_name,
                    email_address=email_address,
                    phone_number=phone_number)
        try:
            # save user to session
            DB.session.add(user)
            # commit session
            DB.session.commit()
        except DatabaseError as err:
            print("Yeah, something went wrong.")

            # you have to rollback on inconclusive transaction
            DB.session.rollback()
            print("Rolling back")

            # create error dict
            error = err.__dict__["orig"].__dict__

            return error
        response = {
            "code": 1,
            "msg": "Success"
        }
        return response


