from pyramid.view import view_config
from pyramidlotto import Lottery
from pyramidlotto import DatabaseFunctions

import re

@view_config(route_name='home', renderer='templates/lottotemplate.pt')
def my_view(request):
    return {'project': 'PyramidLotto'}

@view_config(route_name='sample', renderer='templates/mytemplate.pt')
def sample_view(request):
    return {'project': 'PyramidLotto'}

@view_config(route_name='tickets_view', renderer='json')
def my_tickets_view(request):
    name = request.POST.get('name')
    amount = (int(request.POST.get('amount')))
    lottery = Lottery.Lottery(amount)
    list = lottery.generate_tickets()
    database = DatabaseFunctions.DatabaseFunctions()
    database.save_to_db(name, list)

    return {'ticket': list, 'name': name}

@view_config(route_name='players_view', renderer='json')
def my_players_view(request):
    database = DatabaseFunctions.DatabaseFunctions()
    list = database.get_players()
    return {'names': list}

@view_config(route_name='play_view', renderer='json')
def play(request):
    lottery = Lottery.Lottery(0)
    winningNumber = lottery.get_winning_number()
    #onnette manier om een bug te fixen
    regex = re.compile('[^a-zA-Z]')
    name = regex.sub('', request.POST.get('name'))
    numberList = lottery.play(name)

    return {'tickets': numberList, 'winningNumber': winningNumber}
