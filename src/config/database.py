from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_database_path = '../data/engine.sqlite'
engine = create_engine('sqlite:///' + _database_path, echo=True)
session_factory = sessionmaker(bind=engine)