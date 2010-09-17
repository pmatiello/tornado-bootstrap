from models.message import message
from handlers import request_handler

class messages_handler(request_handler):
    
    def initialize(self, repository):
        self.repository = repository
    
    def get(self):
        self.render('index.html', messages=self.repository.list())
    
    def post(self):
        self.repository.save(message(self.param('name'), self.param('message')))
        self.render('index.html', messages=self.repository.list())

class message_handler(request_handler):
    
    def initialize(self, repository):
        self.repository = repository
    
    def put(self, id):
        msg = self.repository.load(id)
        msg.name = self.param('name')
        msg.message = self.param('message')
        self.repository.save(msg)
        self.render('index.html', messages=self.repository.list())
    
    def delete(self, id):
        self.repository.remove(self.repository.load(id))
        self.render('index.html', messages=self.repository.list())