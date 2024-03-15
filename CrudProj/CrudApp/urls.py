from django.urls import path
from .views import *

urlpatterns = [
    path('create1',patient_create),
    path('list',patient_list),
    path('update/<int:pk>',update_patient),
    path('delete/<int:pk>',delete_patient),
    path('logout',user_logout),
    path('login',user_login)
    
]