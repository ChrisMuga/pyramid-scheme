# sqlalchemy imports
from sqlalchemy import Column, Integer, String, UniqueConstraint

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
    UniqueConstraint(email_address)

    def __repr__(self):

        return f"<User(" \
                f"id={self.id}, " \
                f"first_name={self.first_name}, " \
                f"last_name={self.last_name}, " \
                f"email_address={self.email_address}, " \
                f"phone_number={self.phone_number}" \
                f")>"
