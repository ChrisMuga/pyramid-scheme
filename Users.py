from pyramid.response import Response

# sql-alchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


class DB:
    driver = "mysql+mysqlconnector"
    user = "muga"
    password = "asphalt11"
    host = "localhost"
    database = "PyramidScheme"
    connection_url = f"{driver}://{user}:{password}@{host}/{database}"

# TODO: Fetch Users = Read
# TODO: Update Users Info
# TODO: Delete User(s)


class AppUser:

    @staticmethod
    def hello_world(request):
        return Response('Hello World!')

    @staticmethod
    def index(request):
        return Response("We start here...")

    @staticmethod
    def create(request):
        engine = create_engine(DB.connection_url)
        Session = sessionmaker(bind=engine)
        # create instance of Session class
        session = Session()
        Base = declarative_base()

        # create table class
        class User(Base):

            __tablename__ = 'users'

            id = Column(Integer, primary_key=True)
            first_name = Column(String)
            last_name = Column(String)
            email_address = Column(String)
            phone_number = Column(String)

            def __repr__(self):

                return f"<User(name={self.id}, fullname={self.first_name}, nickname={self.last_name})>"

        # create instance of mapped class
        user = User(id=1, first_name='Chris', last_name='Muga', email_address= "chrismuga94@gmail.com", phone_number= "0704313126")
        # save user to session
        session.add(user)
        # commit session
        session.commit()

        return Response(user.first_name)


