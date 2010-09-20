# Copyright (c) 2010 Pedro Matiello <pmatiello@gmail.com>

"""
A request handler with a few improvements.
"""

from tornado.web import RequestHandler

class request_handler(RequestHandler):
    
    def param(self, name):
        return self.get_argument(name)
    
    def params(self, name):
        return self.get_arguments(name)
