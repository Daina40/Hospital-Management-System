from django.urls import path
from . import views

urlpatterns = [
    path('specialized_details', views.specialized_details, name='specialized_details'),
    path('specialized_delete_item/<int:id>/', views.specialized_delete_item, name='specialized_delete_item'),
    path('specialized_edit_item/<int:id>/', views.specialized_edit_item, name='specialized_edit_item'),
]