from django.urls import path
from . import views

urlpatterns = [
    path('patient_details', views.patient_details, name='patient_details'),
    path('patient_edit_item/<int:id>/', views.patient_edit_item, name='patient_edit_item'),
    path('patient_delete_item/<int:id>/', views.patient_delete_item, name='patient_delete_item'),
]