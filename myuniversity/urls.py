"""myuniversity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,patterns
from django.contrib import admin
from register.views import Home
from register.views import CourseView
from register import urls as reg_urls
from register.views import SignView
from myuniversity.views import anonymous_required
from django.contrib.auth import views as auth_views

from django.conf.urls import include

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^coures/',CourseView.as_view(), name='courselist'),
    url(r'^register/',include(reg_urls)),
    url(r'^user/login/$',anonymous_required(auth_views.login),{'template_name': 'signin.html'},name='signin'),
    url(r'^user/logout/$',auth_views.logout,{'template_name': 'logout.html'},name='logout'),

]
