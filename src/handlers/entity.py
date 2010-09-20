# Copyright (c) 2010 Pedro Matiello <pmatiello@gmail.com>

"""
Handlers.
"""

from models.entity import entity
from handlers import request_handler

class entities_handler(request_handler):
    
    def initialize(self, repository):
        self.repository = repository
    
    def get(self):
        self.render('entity/index.html', data=self.repository.list())
    
    def post(self):
        self.repository.save(entity(self.param('field1'), self.param('field2')))
        self.render('entity/index.html', data=self.repository.list())

class entity_handler(request_handler):
    
    def initialize(self, repository):
        self.repository = repository
    
    def put(self, id):
        msg = self.repository.load(id)
        msg.field1 = self.param('field1')
        msg.field2 = self.param('field2')
        self.repository.save(msg)
        self.render('entity/index.html', data=self.repository.list())
    
    def delete(self, id):
        self.repository.remove(self.repository.load(id))
        self.render('entity/index.html', data=self.repository.list())