from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd2d.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('d2d_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
