from django.urls import path, include
from .views import blog_detail_view, blog_list_view,blog_create_view


urlpatterns = [
    path('', blog_list_view),
    path('create/', blog_create_view),
    path('<str:slug>/', blog_detail_view),
]