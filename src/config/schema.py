from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine

from models.message import message

metadata = MetaData()

messages_table = Table('Messages', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('message', String)
)

mapper(message, messages_table)

if __name__ == "__main__":
    _database_path = '../../data/engine.sqlite'
    engine = create_engine('sqlite:///' + _database_path, echo=True)
    metadata.create_all(engine)