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
    url(r'^add_review/(?P<book_id>\d+)$', views.add_review),
    url(r'^user_reviews/(?P<user_id>\d+)$', views.user_reviews),
    url(r'^append_review/(?P<book_id>\d+)$', views.append_review),
    url(r'^delete_review/(?P<review_id>\d+)$', views.delete_review),
    url(r'^destroy_review/(?P<review_id>\d+)$', views.destroy_review),
    url(r'^login$', views.login)
]
