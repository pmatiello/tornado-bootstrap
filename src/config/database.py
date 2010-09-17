from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper
from models.message import message

database_uri = 'sqlite:///../data/database.sqlite'

metadata = MetaData()

messages_table = Table('Messages', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('message', String)
)

mapper(message, messages_table)