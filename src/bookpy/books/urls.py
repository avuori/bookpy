from django.conf.urls.defaults import patterns, url
#from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^$', 'books.views.index'),
)