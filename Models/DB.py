# sqlalchemy imports
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DB:
    # connection utils
    driver = "mysql+mysqlconnector"
    user = "muga"
    password = "asphalt11"
    host = "localhost"
    database = "PyramidScheme"
    connection_url = f"{driver}://{user}:{password}@{host}/{database}"

    # session and engine utils
    engine = create_engine(connection_url)
    Session = sessionmaker(bind=engine)

    # create instance of Session class
    session = Session()
    Base = declarative_base()