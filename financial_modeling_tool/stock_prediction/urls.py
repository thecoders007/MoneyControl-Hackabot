from django.conf.urls import url, include
from stock_prediction import views
from stock_prediction.views import *


urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^main/$', views.main),
    url(r'^classes/$', views.classes),
    url(r'^compare/$', views.compare),
]
