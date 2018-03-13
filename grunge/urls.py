from django.conf.urls import url
from django.contrib import admin
from views import home, alrev, laban, interviews, stuexc, gigs, alrev_detail, interviews_detail, stuexc_detail, laban_detail, song_detail

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^albumreviews/$', alrev, name='albumreviews'),
    url(r'^albumreviews/(?P<id>\d+)/$', alrev_detail, name='albumreview'),
    url(r'^latestbands/$', laban, name='latestbands'),
    url(r'^latestbands/(?P<id>\d+)/$', laban_detail, name='latestband'),
    url(r'^interviews/$', interviews, name='interviews'),
    url(r'^interviews/(?P<id>\d+)/$', interviews_detail, name='interview'),
    url(r'^studioexchange/$', stuexc, name='studioexchanges'),
    url(r'^studioexchange/(?P<id>\d+)/$', stuexc_detail, name='studioexchange'),
    url(r'^gigs/$', gigs, name='gigs'),
    url(r'^songs/(?P<id>\d+)/$', song_detail, name='song'),
]


