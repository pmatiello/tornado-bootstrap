import tornado.httpserver
import tornado.ioloop
import tornado.web
import config
from handlers.message import messages_handler, message_handler
from models.message import message_repository


database = config.database.session_factory

routes = tornado.web.Application([
    (r"/", messages_handler, {'repository': message_repository(database())}),
    (r"/([0-9]+)/", message_handler, {'repository': message_repository(database())}),
])


if __name__ == "__main__":
    print "Server started"
    
    http_server = tornado.httpserver.HTTPServer(routes)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()