from django.conf.urls import patterns, include, url

from yushen import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yushen_django_1_0.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^products/$', views.ProductsView.as_view(), name = 'products'),
    url(r'^products/detail_identifier(?P<pk>\d)/', views.PartDetailView.as_view(), name = 'detail')
)
