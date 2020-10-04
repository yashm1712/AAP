from django.urls import path, include
from . import views

urlpatterns = [

    path('reunion/', views.reunion, name='reunion'),
    path('add_reunion/', views.add_reunion, name='add_reunion'),
    path('participants/', views.participants_list, name='participants'),
    path('participant_list/<int:id>', views.p_list, name='participant_list'),
    path('<int:reunion_id>/', views.reunion_delete, name='reunion_delete'),


    path('mentor/', views.mentor, name='mentor'),


    path('webinar/', views.webinar, name='webinar'),
    path('add_webinar/', views.add_webinar, name='add_webinar'),
    path('webinar_delete/<int:webinar_id>/', views.webinar_delete, name='webinar_delete'),


    path('add_achievement/', views.add_achievement, name='add_achievement'),

]
