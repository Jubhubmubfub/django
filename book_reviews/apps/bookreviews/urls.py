from django.conf.urls import url
from . import views

urlpatters = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^print_messages$', views.print_messages),
    url(r'^log_user+$', views.print_messages),
    url(r'^logout$', views.logout)
]
