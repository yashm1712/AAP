from django.urls import path, include
from . import views

urlpatterns = [

    path('reunion/', views.reunion, name='reunion'),
    path('add_reunion/', views.add_reunion, name='add_reunion'),
    path('participants/', views.participants_list, name='participants'),
    path('mentor/', views.mentor, name='mentor'),
    path('webinar/', views.webinar, name='webinar'),

]
