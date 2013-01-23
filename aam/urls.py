from django.conf.urls import patterns, include, url

from ade.views import ADE_requestListView, ADE_requestDetailView, create_xls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', ADE_requestListView.as_view(), name='home'),
    url(r'^ade/(?P<pk>\d+)/$',
        ADE_requestDetailView.as_view(),
        name='ade'),
    url(r'^ade/(?P<pk>\d+)/download/$', create_xls, name='excel'),
    url(r'^admin/', include(admin.site.urls)),
)
