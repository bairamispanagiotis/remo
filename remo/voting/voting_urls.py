from django.conf.urls.defaults import *

urlpatterns = patterns('remo.voting.views',
    url(r'^$', 'list_votings', name='voting_list_votings'),
    url(r'^new/$', 'edit_voting', name='voting_new_voting'),
)
