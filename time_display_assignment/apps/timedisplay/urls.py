from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.displayTime),
    url(r'^new_user',views.create)
]
