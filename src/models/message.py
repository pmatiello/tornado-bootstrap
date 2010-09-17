class message(object):
    
    def __init__(self, name, message):
        self.name = name
        self.message = message


class message_repository():
    
    def __init__(self, session):
        self.session = session
    
    def load(self, id):
        return self.session.query(message).filter(message.id == id).first()
    
    def save(self, message):
        self.session.add(message)
        self.session.commit()
    
    def remove(self, message):
        self.session.delete(message)
        self.session.commit()
    
    def list(self):
        return self.session.query(message).all()