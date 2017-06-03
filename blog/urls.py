from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'projects', views.projects, name='projects'),
    url(r'about', views.about, name='about'),
    # url(r'blog', views.blog, name='blog'),
    #url(r'test', views.test, name='test')
]
