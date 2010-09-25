# Copyright (c) 2010 Pedro Matiello <pmatiello@gmail.com>

"""
Database schema definition.
"""

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper
from models.entity import entity

def map_entities():
    mapper(entity, entity_table)
    return _metadata

_metadata = MetaData()

# Database Schema

entity_table = Table('Entity', _metadata,
    Column('id', Integer, primary_key=True),
    Column('field1', String),
    Column('field2', String)
)
