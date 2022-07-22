"""user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework .urlpatterns import format_suffix_patterns 
from userprofile import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('userprofile/new', views.userlist.as_view()),
    # url(r'^',include('userprofile.urls'))
    path('',views.get ,name='get'),
    path('create/',views.post ,name='post'),
    path('update/',views.put ,name='put'),
    path('delete/<int:id>',views.delete ,name='delete'),
    path('find/<int:id>',views.find ,name='find'),
    path('getEmployer/',views.getEmployer ,name='getEmployer'),
    path('createEmployer/',views.createEmployer ,name='createEmployer'),
    path('deleteEmployer/<int:id>',views.deleteEmployer ,name='deleteEmployer'),
    path('joinUserEmployer/',views.joinUserEmployer ,name='joinUserEmployer'),
    # path('getKeyValueData/',views.getKeyValueData ,name='getKeyValueData'),



]
