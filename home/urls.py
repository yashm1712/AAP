from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_validate, name='login'),
    path('logout/', views.logout_validate, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('test/', views.test, name='test'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('view_profile/<int:id>', views.view_profile, name='view_profile'),
    path('accounts/', include('allauth.urls')),
    path('students_list', views.allStudents, name='students_list'),
    path('alumni_list', views.allAlumni, name='alumni_list'),
    path('edit_profile/<int:id>', views.EditProfile, name='edit_profile'),

]
