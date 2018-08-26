from sqlalchemy import *
from sqlalchemy.orm import ( scoped_session, sessionmaker, relationship,backref)
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))
Base = declarative_base()

Base.query = db_session.query_property()

class Carbon(Base):
    __tablename__ = 'carbon'
    id = Column(Integer, primary_key=True)
    created_at = Column(String)
    updated_at = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    reading = Column(Float)
    device_identification = Column(String)