from tornado.ioloop import IOLoop
from tornado.web import Application, url
from tornado.options import define, options
from database import init_database

import tornado.options
import handler
import os

define('port', default=8000, help='run on the given port', type=int)

settings = {
    "cookie_secret": "O6R7HH++SnKHj1eD9TK0QD4sKJbM/0lLvv394rMuokQ=",
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}


def make_app():
    return Application([
        url(r"/info", handler.InfoHandler),
        url(r"/invite/(web|ios|design|android|pm|lab)", handler.InviteHandler),
        url(r"/invite", handler.InviteHandler),
        url(r"/invite/(.+)/(0|1)", handler.InviteHandler),
        url(r"/query", handler.QueryHandler),
        url(r"/query/(\d{11})", handler.QueryHandler),
        url(r"/", handler.MainHandler),
        url(r"/applicant", handler.ApplyHandler),
        url(r"/advice", handler.AdviceHandler)
    ], **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    init_database()
    app = make_app()
    app.listen(options.port)
    IOLoop.current().start()