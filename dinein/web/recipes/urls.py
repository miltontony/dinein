from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'dinein.web.recipes.views.home', name='home'),
    url(r'^add/$', 'dinein.web.recipes.views.add', name='add'),
    url(
        r'^edit/(?P<slug>[\w-]+)/$',
        'dinein.web.recipes.views.edit',
        name='edit'
    ),
)
