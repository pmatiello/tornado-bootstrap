# Copyright (c) 2010 Pedro Matiello <pmatiello@gmail.com>

"""
An example entity and its DAO.
"""

class entity(object):
    
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2


class entity_repository():
    
    def __init__(self, session):
        self.session = session
    
    def load(self, id):
        return self.session.query(entity).filter(entity.id == id).first()
    
    def save(self, instance):
        self.session.add(instance)
        self.session.commit()
    
    def remove(self, instance):
        self.session.delete(instance)
        self.session.commit()
    
    def list(self):
        return self.session.query(entity).all()