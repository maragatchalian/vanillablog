from django.conf.urls import include, url
from django.contrib import admin
from vanillablog.views import ListView, CreatePost, ViewPost

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ListView.as_view(), name='list'),
    url(r'^create/$', CreatePost.as_view(), name='create_post'),
    url(r'^post/(?P<pk>\d+)/$', ViewPost.as_view(), name='post_detail'),
]