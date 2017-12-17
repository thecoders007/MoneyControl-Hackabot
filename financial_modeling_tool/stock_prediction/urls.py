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
    url(r'^add-stock/$', views.add_stock),
    url(r'^response/$', views.respond_chat),
    url(r'^learn/$', views.learn),
    url(r'^detail/(?P<p>[\w\-\_]+)/$',views.detail),
    url(r'^news/$', views.news),

]
