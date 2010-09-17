# Copyright (c) 2010 Pedro Matiello <pmatiello@gmail.com>

"""
Database utils.
"""

from config.database import database_uri, metadata
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

_engine = create_engine(database_uri)
session_factory = sessionmaker(bind=_engine)

if __name__ == "__main__":
    metadata.create_all(_engine)