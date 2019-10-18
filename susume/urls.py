from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^jobs/*$', views.job),
    re_path(r'^jobs/(?P<id>\d+)/*$', views.job, name='job'),
    re_path(r'^jobs/.+/*$', views.job, name='job'),
    re_path(r'^spells/*$', views.spell, name='spell'),
    re_path(r'^spells/(?P<id>\d+)/*$', views.spell, name='spell'),
    re_path(r'^spells/.+/*$', views.spell, name='spell'),
    re_path(r'^servers/*$', views.server, name='server'),
    re_path(r'^servers/(?P<id>\d+)/*$', views.server, name='server'),
    re_path(r'^servers/.+/*$', views.server, name='server'),
    # Default non-match route. remove to show 404
    re_path(r'^.*$', views.index, name='index'),
]