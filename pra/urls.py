from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pra.views.home', name='home'),
    # url(r'^pra/', include('pra.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^q1/$', "views.q1"),
    url(r'^q2/$', "views.q2"),
    url(r'^q3/$', "views.q3"),
    url(r'^q4/$', "views.q4"),
)
