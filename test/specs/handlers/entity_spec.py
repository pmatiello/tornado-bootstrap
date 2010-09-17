# Copyright (c) 2010 Pedro Matiello <pmatiello@gmail.com>

from mockito import any, mock, verify, when
from handlers.entity import entity_handler, entities_handler
from models.entity import entity

class entities_handler_spec():
    
    def setup(self):
        self.handler = object.__new__(entities_handler)
        self.repository = mock()
        self.handler.initialize(self.repository)
        self.entity_list = [1,2,3]
        when(self.repository).list().thenReturn(self.entity_list)
        when(self.handler).render().thenReturn(None)
    
    def should_list_all_instances(self):
        self.handler.get()
        verify(self.repository).list()
        verify(self.handler).render('index.html', data=self.entity_list)
    
    def should_create_new_instances(self):
        when(self.handler).param('field1').thenReturn("Field1 data")
        when(self.handler).param('field2').thenReturn("Field2 data")
        self.handler.post()
        verify(self.repository).save(any(entity))

class entity_handler_spec():
    
    def setup(self):
        self.handler = object.__new__(entity_handler)
        self.repository = mock()
        self.handler.initialize(self.repository)
        self.entity = entity("Field1 data", "Field2 data")
        when(self.repository).load(1).thenReturn(self.entity)
        when(self.handler).render().thenReturn(None)
    
    def should_modify_instances(self):
        when(self.handler).param('field1').thenReturn("Field1 data updated")
        when(self.handler).param('field2').thenReturn("Field2 data updated")
        self.handler.put(1)
        assert self.entity.field1 == "Field1 data updated"
        assert self.entity.field2 == "Field2 data updated"
        verify(self.repository).save(self.entity)
    
    def should_delete_instances(self):
        self.handler.delete(1)
        verify(self.repository).remove(self.entity)
