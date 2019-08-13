# python imports
import random

# pyramid imports
from pyramid.response import Response

# sql-alchemy
from sqlalchemy.exc import DatabaseError, ProgrammingError


# Model imports

from Models.User import User
from Models.DB import DB

# TODO: Update Users Info
# TODO: Delete User(s)
# TODO: Separate container for views
# TODO: Delete user "Mboya"


class AppUser:

    @staticmethod
    def hello_world(request):
        return Response('Hello World!')

    @staticmethod
    def index(request):
        return Response("We start here...")

    @staticmethod
    def fetch_users(request):

        try:
            users = DB.session.query(User).all()
            users_array = []
            for user in users:
                new_user_ = {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email_address": user.email_address,
                    "phone_number": user.phone_number
                }
                users_array.append(new_user_)
            return users_array
        except DatabaseError as err:
            print(err)
            Response("Something went wrong.")
        except ProgrammingError as err:
            print("Something went wrong.")
            print(err)
            Response("Programming Error")


    @staticmethod
    def new_user(request):

        # fetch from request
        random_id = random.randint(1, 1e9)
        first_name = request.json_body["first_name"]
        last_name = request.json_body["last_name"]
        email_address = request.json_body["email_address"]
        phone_number = request.json_body["phone_number"]

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
            print(error)
            return error
        response = {
            "code": 1,
            "msg": "Success"
        }

        return response


