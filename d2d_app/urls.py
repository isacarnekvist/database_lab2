from django.conf.urls import patterns, url
from d2d_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register$', views.register_view, name='register'), 
    url(r'^register_post$', views.register_post, name='register_post'), 
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^add_contract/$', views.add_contract_view, name='add_contract'),
    url(r'^remove(?P<contract_id>\d+)$', views.remove, name='remove'),
    url(r'^check_login/$', views.check_login, name='check_login'),
    url(r'^pay(?P<contract_id>\d+)$', views.pay, name='pay'),
    url(r'^satisfied(?P<contract_id>\d+)$', views.satisfied, name='satisfied'),
)
