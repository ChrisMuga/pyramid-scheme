from wsgiref.simple_server import make_server
from pyramid.config import Configurator


# views
from Users import AppUser

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/hello')
        config.add_route('index', '/')
        config.add_route('new_user', "/api/new-user")
        config.add_route('fetch_users', "/api/fetch-users")
        config.add_view(AppUser.hello_world, route_name='hello')
        config.add_view(AppUser.index, route_name="index")
        config.add_view(AppUser.new_user, route_name="new_user", renderer="json", request_method="POST")
        config.add_view(AppUser.fetch_users, route_name="fetch_users", renderer="json", request_method="GET")
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()
