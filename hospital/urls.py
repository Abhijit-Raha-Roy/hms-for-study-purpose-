from django.urls import path
from .views import *
urlpatterns=[
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('',index,name='index'),
    path('admin_login/',login,name='login'),
    path('logout_admin/',logout_admin,name='logout_admin'),
    path('view_doctor/',view_doctor,name='view_doctor'),
    path('add_doctor/',add_doctor,name='add_doctor'),
    path('delete_doctor(?p<int:pid>)',delete_doctor,name='delete_doctor'),

    path('view_patient/',view_patient,name='view_patient'),
    path('add_patient/',add_patient,name='add_patient'),
    path('delete_patient(?p<int:pid>)',delete_patient,name='delete_patient'),


    path('view_appointment/',view_appointment,name='view_appointment'),
    path('add_appointment/',add_appointment,name='add_appointment'),
    path('delete_appointment(?p<int:pid>)',delete_appointment,name='delete_appointment'),


]