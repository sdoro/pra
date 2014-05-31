from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'age_imm.views.home', name='home'),
    # url(r'^age_imm/', include('age_imm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^query-01/', "views.q1"),
    #url(r'^query-02/', "views.q2"),
    #url(r'^query-03/', "views.q3"),
    #url(r'^query-04/', "views.q4"),
    url(r'^agenzie/(\d+)/$', "views.ann"),
    url(r'^data_a/(?P<anno>\d{4})/(?P<mese>\d{1,2})/$', "views.data_ann"),
)
