from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="my_index"),
    url(r'^submit_survey$', views.submit, name="my_submit"),
    url(r'^post$', views.post, name="my_post")
]
