# Copyright (c) 2010 Pedro Matiello <pmatiello@gmail.com>

"""
Database configuration and schema definition.
"""

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper
from models.entity import entity

database_uri = 'sqlite:///../data/database.sqlite'

metadata = MetaData()

entity_table = Table('Entity', metadata,
    Column('id', Integer, primary_key=True),
    Column('field1', String),
    Column('field2', String)
)

mapper(entity, entity_table)