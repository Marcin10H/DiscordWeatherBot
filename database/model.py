from sqlalchemy import Column, BigInteger, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class History(Base):
    __tablename__ = 'history'
    __table_args__ = {'extend_existing': True}
    id = Column('id', BigInteger, primary_key=True, autoincrement=True)
    city = Column('city', Text)
    temperature = Column('temperature', Text)
    windspeed = Column('windspeed', Text)
    timestamp = Column('timestamp', BigInteger)


def history_class(table_name):
    History.__tablename__ = table_name
    return History
