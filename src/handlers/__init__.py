from tornado.web import RequestHandler

class request_handler(RequestHandler):
    
    def param(self, name):
        return self.get_argument(name)
    
    def params(self, name):
        return self.get_arguments(name)