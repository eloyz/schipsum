from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ipsum.views',
    url(r'^$', 'detail', name="homepage"),
)
