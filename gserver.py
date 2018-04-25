from gevent.wsgi import WSGIServer
from mysite import create_app

app = create_app('mysite.config.ProdConfig')

server = WSGIServer(('', 80), app)
server.serve_forever()
