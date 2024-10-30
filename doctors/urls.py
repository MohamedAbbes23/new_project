from django.urls import path
from django.contrib.auth import views as auth_views
from .views import landing_page, doctor_dashboard, delete_patient, edit_patient, add_patient, delete_appointment, create_prescription, edit_appointment, add_appointment


urlpatterns = [
    path('', landing_page, name='landing'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('patient/add/', add_patient, name='add_patient'),
    path('patient/edit/<int:pk>/', edit_patient, name='edit_patient'),
    path('patient/delete/<int:pk>/', delete_patient, name='delete_patient'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing_page'), name='logout'),
    path('appointment/add/', add_appointment, name='add_appointment'),
    path('appointment/edit/<int:appointment_id>/', edit_appointment, name='edit_appointment'),
    path('appointment/delete/<int:appointment_id>/', delete_appointment, name='delete_appointment'),
    path('prescription/create/', create_prescription, name='create_prescription'),

]
