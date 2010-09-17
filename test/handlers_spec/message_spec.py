from mockito import any, mock, verify, when
from handlers.message import messages_handler

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
        when(self.handler).param('name').thenReturn('Author name')
        when(self.handler).param('message').thenReturn('Message text')
        self.handler.post()
        verify(self.repository).list()
        verify(self.repository).save(any())
        verify(self.handler).render('index.html', messages=self.message_list)