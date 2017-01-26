from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='my_index'),
    url(r'^reset$', views.reset, name='my_reset'),
    url(r'^clear_log$', views.clear_log, name='my_clear'),
    url(r'^process_money/(?P<building>\w+)$', views.process, name='my_process')
]
