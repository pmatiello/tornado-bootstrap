# Copyright (c) 2010 Pedro Matiello <pmatiello@gmail.com>

"""
Routing configuration.
"""

import tornado.web
from handlers.entity import entity_handler, entities_handler
from models.entity import entity_repository
from util.database import session_factory

routes = [
    (r"/", entities_handler, {'repository': entity_repository(session_factory())}),
    (r"/([0-9]+)/", entity_handler, {'repository': entity_repository(session_factory())})
]

application = tornado.web.Application(routes,
                                      template_path='view/')