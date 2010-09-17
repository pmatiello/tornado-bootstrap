from mockito import any, mock, verify, when
from handlers.message import message_handler, messages_handler
from models.message import message

class messages_handler_spec():
    
    def setup(self):
        self.handler = object.__new__(messages_handler)
        self.repository = mock()
        self.handler.initialize(self.repository)
        self.message_list = [1,2,3]
        when(self.repository).list().thenReturn(self.message_list)
        when(self.handler).render().thenReturn(None)
    
    def should_list_all_messages(self):
        self.handler.get()
        verify(self.repository).list()
        verify(self.handler).render('index.html', messages=self.message_list)
    
    def should_create_new_messages(self):
        when(self.handler).param('name').thenReturn("Author name")
        when(self.handler).param('message').thenReturn("Message text")
        self.handler.post()
        verify(self.repository).save(any(message))

class message_handler_spec():
    
    def setup(self):
        self.handler = object.__new__(message_handler)
        self.repository = mock()
        self.handler.initialize(self.repository)
        self.message = message("Author name", "Message text")
        when(self.repository).load(1).thenReturn(self.message)
        when(self.handler).render().thenReturn(None)
    
    def should_modify_messages(self):
        when(self.handler).param('name').thenReturn("Author name updated")
        when(self.handler).param('message').thenReturn("Message text updated")
        self.handler.put(1)
        assert self.message.name == "Author name updated"
        assert self.message.message == "Message text updated"
        verify(self.repository).save(self.message)
    
    def should_delete_messages(self):
        when(self.handler).param('name').thenReturn("Author name updated")
        when(self.handler).param('message').thenReturn("Message text updated")
        self.handler.delete(1)
        verify(self.repository).remove(self.message)
