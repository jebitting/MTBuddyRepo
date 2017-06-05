from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^landing$', views.landing, name="landing"),
    #url(r'^landing/(?P<id>\d+)$', views.landing, name="landing"),
    # update to pass the id of the traveler
    url(r'^create$', views.create, name="create"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
    # update to pass the info of the trip to delete
    url(r'^logout$', views.logout, name="logout"),
]
