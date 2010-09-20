# Copyright (c) 2010 Pedro Matiello <pmatiello@gmail.com>

"""
Application entry-point.
"""

import tornado.httpserver
import tornado.ioloop
from config.routes import application

if __name__ == "__main__":
    print "Server started"
    
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()