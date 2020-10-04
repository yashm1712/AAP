from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.blog_home, name='blog_home'),
    path('like/', views.blog_like, name='blog_like'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blog_comment/', views.blog_comment, name='blog_comment'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('your_blogs/<int:id>', views.your_blog, name='your_blogs'),
    path('<int:blog_id>/', views.blog_delete, name='blog_delete'),
    path('search', views.search, name='search'),

]
