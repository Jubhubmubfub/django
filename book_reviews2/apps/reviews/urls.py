from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^log_user_in$', views.log_user_in),
    url(r'^print_messages$', views.print_messages),
    url(r'^logout$', views.logout),
    url(r'^add_book$', views.add_book),
    url(r'^add_book_review$', views.add_book_review),
    url(r'^create_book$', views.create_book),
    url(r'^login$', views.login)
]
