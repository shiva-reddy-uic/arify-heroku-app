"""arify_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from arify_app import views
from arify_app.views import scenes_list, scene_links

urlpatterns = [

    path('', views.index, name='index'),
    path('add_scene/', views.add_scene, name='add_scene'),
    path("scenes/", scenes_list, name="scenes_list"),
    path("scenes/<str:pk>/", scene_links, name="scene_links"),
    path('add_ar_object/', views.add_ar_object, name='add_ar_object'),
    path('admin/', admin.site.urls),
]
