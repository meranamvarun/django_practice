"""tutorial2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""



from django.conf.urls import patterns, include, url

from  django.contrib import admin

admin.autodiscover()

#from django.contrib.auth import views as auth_views 

urlpatterns = patterns('',
    (r'^articles/',include('article.urls')),
    url(r'^$','tutorial2.views.home'),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^accounts/login/$', 'tutorial2.views.login'),
    url(r'^accounts/auth/$', 'tutorial2.views.auth_view'),
    url(r'^accounts/logout/$', 'tutorial2.views.logout'),
    url(r'^accounts/loggedin/$', 'tutorial2.views.loggedin'),
    url(r'^accounts/invalid/$', 'tutorial2.views.invalid_login'),
)






















