from django.shortcuts import * 
from django.db.models import * 
from datetime import datetime, timedelta, date
from django.views.decorators.cache import cache_page
from bs4 import BeautifulSoup
import urllib2

def Main(request):
    longtoday = datetime.now() - timedelta(hours=10)
    today = datetime.now() - timedelta(hours=5)
    yesterday = datetime.now() - timedelta(days=1)
    yesterday = yesterday.strftime('%Y%m%d')
    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow = tomorrow.strftime('%Y%m%d')
    
    dictionaries = { 'longtoday': longtoday, 'today': today, 'yesterday': yesterday, 'tomorrow': tomorrow, }
    return render_to_response('scoreboard/main.html', dictionaries)

def Main2(request):
    longtoday = datetime.now() - timedelta(hours=10)
    today = datetime.now()
    yesterday = datetime.now() - timedelta(days=1)
    yesterday = yesterday.strftime('%Y%m%d')
    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow = tomorrow.strftime('%Y%m%d')
    
    dictionaries = { 'longtoday': longtoday, 'today': today, 'yesterday': yesterday, 'tomorrow': tomorrow, }
    return render_to_response('scoreboard/main2.html', dictionaries)
	
	
def Date(request, date):
    today = datetime.strptime(date, "%Y%m%d")
    yesterday = today - timedelta(days=1)
    yesterday = yesterday.strftime('%Y%m%d')
    tomorrow = today + timedelta(days=1)
    tomorrow = tomorrow.strftime('%Y%m%d')

    dictionaries = { 'today': today, 'yesterday': yesterday, 'tomorrow': tomorrow, }
    return render_to_response('scoreboard/main.html', dictionaries)

def Game(request, gameid):
    game_id = gameid
    url = 'http://owh.newsengin.com/tpweb/web/gateway.php?site=ow&tpl=boxscore&ID=' + game_id
    site = urllib2.urlopen(url)
    html = site.read()
    soup = BeautifulSoup(html)
    text = soup.prettify()
	
    dictionaries = { 'game_id': game_id, 'text': text, }
    return render_to_response('scoreboard/game.html', dictionaries)

