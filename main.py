from tornado.ioloop import IOLoop
from tornado.web import Application, url
from tornado.options import define, options

import tornado.options
import handler

define('port', default=8000, help='run on the given port', type=int)


def make_app():
    return Application([
        url(r"/", handler.MainHandler),
        url(r"/applicant", handler.ApplyHandler),
        url(r"/advice", handler.AdviceHandler)
    ])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    IOLoop.current().start()