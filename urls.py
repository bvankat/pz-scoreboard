from django.conf.urls import * 

urlpatterns = patterns('',
    (r'^/meets$', 'scoreboard.views.Main2'),
    (r'^/game/(?P<gameid>[a-zA-Z0-9_.-]+)$', 'scoreboard.views.Game'),
    (r'^/(?P<date>[a-zA-Z0-9_.-]+)$', 'scoreboard.views.Date'),
    (r'^', 'scoreboard.views.Main'), 
)
