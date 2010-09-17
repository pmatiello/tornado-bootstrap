# Copyright (c) 2010 Pedro Matiello <pmatiello@gmail.com>

"""
Application entry-point.
"""

import tornado.httpserver
import tornado.ioloop
import tornado.web
from handlers.entity import entity_handler, entities_handler
from models.entity import entity_repository
from util.database import session_factory

routes = tornado.web.Application([
    (r"/", entities_handler, {'repository': entity_repository(session_factory())}),
    (r"/([0-9]+)/", entity_handler, {'repository': entity_repository(session_factory())}),
])


if __name__ == "__main__":
    print "Server started"
    
    http_server = tornado.httpserver.HTTPServer(routes)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()