from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^reset$', views.reset),
    url(r'^clear_log$', views.clear_log),
    url(r'^process_money/(?P<building>\w+)$', views.process)
]
