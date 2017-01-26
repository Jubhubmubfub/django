from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.users),
    url(r'^process$', views.process),
    url(r'^user_interests/(?P<user_id>\d+)$', views.user_interests)

]
