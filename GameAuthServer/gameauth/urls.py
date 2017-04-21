from django.conf.urls import url, include

from . import views


urlpatterns = [
        #url(r'^$', views.index, name='index'),
        # ex: /gameauth/5/
        url(r'^(?P<activity_id>[0-9]+)/$', views.detail, name='detail'),
        # ex: /gameauth/5/results/
        url(r'^(?P<activity_id>[0-9]+)/results/$', views.results, name='results'),
        # es: /gameauth/5/addActivity/
        url(r'^(?P<activity_id>[0-9]+)/addActivity/$', views.addActivity, name='addActivity'),
    ]

