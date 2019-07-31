from wsgiref.simple_server import make_server
from pyramid.config import Configurator


# views
from Users import User

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/hello')
        config.add_route('index', '/')
        config.add_route('create', "/create")
        config.add_view(User.hello_world, route_name='hello')
        config.add_view(User.index, route_name="index")
        config.add_view(User.create, route_name="create")
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
