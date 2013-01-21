from django.conf.urls import patterns, include, url

from ade.views import ADE_requestListView, ADE_requestDetailView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aam.views.home', name='home'),
    # url(r'^aam/', include('aam.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', ADE_requestListView.as_view(), name='home'),
    url(r'^ade/(?P<pk>\d+)/$',
        ADE_requestDetailView.as_view(),
        name='ade'),
    url(r'^admin/', include(admin.site.urls)),
)
