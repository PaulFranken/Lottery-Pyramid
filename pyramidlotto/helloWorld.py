__author__ = 'PaulFranken'

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Paul' %request.matchdict)