"""blog_site URL Configuration

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
from django.urls import path, include
from .views import home_view
from blog.views import BlogPostView
from rest_framework import routers
from users.views import user_registration_view

router = routers.DefaultRouter()
router.register('blog-posts',BlogPostView)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home_view,name='home-page'),
    path('blog/', include('blog.urls')),

    path('register/', user_registration_view),

    path('blog-api/',include(router.urls)),

    #REST authorization
    path('api-auth/',include('rest_framework.urls'))
]
