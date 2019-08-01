# sqlalchemy imports
from sqlalchemy import Column, Integer, String

# import DB details
from .DB import DB

# create table class


class User(DB.Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email_address = Column(String)
    phone_number = Column(String)

    def __repr__(self):

        return f"<User(name={self.id}, fullname={self.first_name}, nickname={self.last_name})>"