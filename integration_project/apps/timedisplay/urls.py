from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.displayTime, name="my_index"),
    url(r'^new_user',views.create, name="my_new")
]
