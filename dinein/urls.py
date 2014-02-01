from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'dinein.web.views.home', name='home'),
    url(r'', include('social_auth.urls')),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout_then_login',
        name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
