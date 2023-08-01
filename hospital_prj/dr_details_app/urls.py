from django.urls import path
from . import views

urlpatterns = [
    path('dr_details', views.dr_details, name='dr_details'),
    path('dr_edit_item/<int:id>/', views.dr_edit_item, name='dr_edit_item'),
    path('dr_delete_item/<int:id>/', views.dr_delete_item, name='dr_delete_item'),
]