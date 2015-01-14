from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from HomePage.views import index
#from News.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,}),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}), 
    #url(r'^left-behind/', LeftBehind),
    #url(r'^news/', News),
    #url(r'^literature/', Literature),
    #url(r'^reporter/', Reporter),
    #url(r'^content/', Content),
    #url(r'^list/', ArticleList),
)
