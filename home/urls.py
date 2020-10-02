from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

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

    path('alumni_list', views.allAlumni, name='alumni_list'),
    path('search_alumni', views.search_alumni, name='search_alumni'),
    path('students_list', views.allStudents, name='students_list'),
    path('search_student', views.search_student, name='search_students'),


    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='password/password_reset.html'),
         name='reset_password'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_sent.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_form.html'),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_done.html'),
         name='password_reset_complete'),

]
