from django.conf.urls import url

from Rebbit import views

urlpatterns = [
    url(r'^index/$', views.homepage),
    url(r'^r/(?P<sub_id>\w+)/$', views.subreddit),
    url(r'^r/(?P<sub_id>\w+)/(?P<post_id>\w+)/$', views.subredditdetail),
    url('^signup/$', views.signup),
    url('^createpost/$', views.createpost),
    url('^authpost/$', views.auth_post),
    url(r'^r/(?P<sub_id>\w+)/(?P<post_id>\w+)/authcomment/$', views.auth_comment),
    url('^createsub/$', views.createsub),
    url('^auth_sub/$', views.auth_sub),
    url('^signin/$', views.signin),
    url('^account/$', views.accounthome),
    url('^auth/$', views.auth_verify),
    url('^authsign/$', views.auth_signup),
    url('^logout/$', views.logout),
    url('^about/$', views.aboutus),
    url(r'^r/(?P<sub_id>\w+)/(?P<post_id>\w+)/votepost/$', views.votepost),
    url(r'^r/(?P<sub_id>\w+)/(?P<post_id>\w+)/(?P<comment_id>\d+)/commentvote/$', views.votecomment),

]

