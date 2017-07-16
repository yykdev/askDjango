from django.conf import settings
from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.blog_index),
    url(r'^post/$', views.post_list),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]