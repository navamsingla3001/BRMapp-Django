"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include

urlpatterns = [
    path('BRMapp/',include('BRMapp.urls')),
    #path('result',exam_views.result),
    #path('showTest',exam_views.showTest),
    #url('^$',testapp_views.greeting),
    #path('about/',testapp_views.about),
    #path('showcontact/',testapp_views.showcontact),
    path('admin/', admin.site.urls),
]
