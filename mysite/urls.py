from django.conf.urls import include, url
from django.contrib import admin
from vanillablog.views import ListView, CreatePost, ViewPost, DeletePost, EditPost

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ListView.as_view(), name='list'),
    url(r'^selete/$', CreatePost.as_view(), name='create_post'),
    url(r'^post/(?P<pk>\d+)/$', ViewPost.as_view(), name='post_detail'),
     url(r'^edit/(?P<pk>\d+)/$', EditPost.as_view(), name='edit_post'),
    url(r'^delete/(?P<pk>\d+)/$', DeletePost.as_view(), name='delete_post'),
]