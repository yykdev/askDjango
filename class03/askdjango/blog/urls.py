from django.conf import settings
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.my_sum),
    # url(r'^sum/(?P<x>\d+)/(?P<z>\d+)/$', views.my_sum),
    # url(r'^sum/(?P<x>\d+)/$', views.my_sum),
    url(r'^sum/(?P<numbers>[0-9/]+)/$', views.my_sum)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]