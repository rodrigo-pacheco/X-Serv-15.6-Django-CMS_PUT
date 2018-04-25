from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cms.views.slash'),
    url(r'^(\d+)$', 'cms.views.number'),
    url(r'.*', 'cms.views.notfound'),
)
