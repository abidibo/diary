from django.conf.urls import patterns,url
from melissa import views

urlpatterns = patterns('melissa.views',

    url(r'^/?$', views.DiaryView.as_view(), name='melissa-diary'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.PageView.as_view(), name='melissa-page-detail'),

)
