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
# TODO: Error handling for duplicate DB entries
# TODO: Separate Model classes


class AppUser:

    @staticmethod
    def hello_world(request):
        return Response('Hello World!')

    @staticmethod
    def index(request):
        return Response("We start here...")

    @staticmethod
    def create(request):

        # create instance of mapped class
        user = User(id=1,
                    first_name='Chris',
                    last_name='Muga',
                    email_address="chrismuga94@gmail.com",
                    phone_number="0704313126")
        try:
            # save user to session
            DB.session.add(user)
            # commit session
            DB.session.commit()
        except DatabaseError as err:
            print("Yeah, something went wrong.")
            # create error dict
            error = err.__dict__["orig"].__dict__
            return error

        return Response(user)


