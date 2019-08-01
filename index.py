from wsgiref.simple_server import make_server
from pyramid.config import Configurator


# views
from Users import AppUser

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/hello')
        config.add_route('index', '/')
        config.add_route('create', "/create")
        config.add_view(AppUser.hello_world, route_name='hello')
        config.add_view(AppUser.index, route_name="index")
        config.add_view(AppUser.create, route_name="create", renderer="json")
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()
