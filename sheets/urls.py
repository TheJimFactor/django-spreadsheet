
from django.conf.urls import patterns, include, url
from sheets import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spreadsheet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name="index"),
    url(r'sandbox/$', views.sandbox, name="sandbox"),
    url(r'^savesheet/$', views.savesheet, name="savesheet"),
    url(r'^loadsheet/$', views.loadsheet, name="loadsheet"),

)
