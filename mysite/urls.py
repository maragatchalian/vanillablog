from django.conf.urls import include, url
from django.contrib import admin
from vanillablog.views import PostView, ListView, CreatePost

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ListView.as_view(), name='list'),
    url(r'^create/$', CreatePost.as_view(), name='create_post')
]