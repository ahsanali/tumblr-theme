from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tumblr import create_app
if __name__ == '__main__':
	app = create_app()
	app.debug = True
	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(80)
	IOLoop.instance().start()
