from mockito import any, mock, verify, when
from models.message import message, message_repository
import config.database

class message_repository_spec():

    def setup(self):
        self.session = mock()
        self.repository = message_repository(self.session)
        self.msg = message("Author name", "Message text")
    
    def should_load_messages(self):
        query = mock()
        filtered_query = mock()
        when(self.session).query(message).thenReturn(query)
        when(query).filter(any()).thenReturn(filtered_query)
        when(filtered_query).first().thenReturn(self.msg)
        assert self.repository.load(1) == self.msg
    
    def should_save_messages(self):
        self.repository.save(self.msg)
        verify(self.session).add(self.msg)
        verify(self.session).commit()
    
    def should_delete_messages(self):
        self.repository.remove(self.msg)
        verify(self.session).delete(self.msg)
        verify(self.session).commit()
    
    def should_list_messages(self):
        query = mock()
        when(self.session).query(message).thenReturn(query)
        when(query).all().thenReturn([self.msg])
        assert self.repository.list() == [self.msg]