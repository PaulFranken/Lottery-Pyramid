from pyramid.config import Configurator
from .views import sample_view
from pyramidlotto import Lottery
from pyramidlotto import helloWorld
import os


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('sample', '/sample')
    config.add_route('tickets_view', '/tickets_view')
    config.add_route('players_view', '/players_view')
    config.add_route('play_view', '/play_view')
    config.scan()
    return config.make_wsgi_app()
