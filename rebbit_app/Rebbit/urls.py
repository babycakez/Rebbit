from django.conf.urls import url
from Rebbit import views
urlpatterns = [
    url('^index/$', views.homepage),
    #url('^$', views.subreddit),
    url('^signup/$', views.signup),
    url('^signin/$', views.signin),
    url('^account/$', views.accounthome),
    url('^auth/$', views.auth_verify),
    url('^logout/$', views.logout),
]

