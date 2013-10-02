from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^open/$', 'LokoApp.views.open'),
    url(r'^close/$', 'LokoApp.views.close'),
    url(r'^$', 'LokoApp.views.index'),
    # url(r'^LokoServer/', include('LokoServer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
