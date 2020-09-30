from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.blog_home, name='blog_home'),
    path('like/', views.blog_like, name='blog_like'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('your_blogs/<int:id>', views.your_blog, name='your_blogs'),
    path('search', views.search, name='search'),

]
