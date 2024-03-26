from django.urls import path
from .views import add_district, show_district, update_district, delete_district

urlpatterns = [
    path('add/', add_district, name='add_url'),
    path('show/', show_district, name='show_url'),
    path('update/<int:pk>/', update_district, name='update_url'),
    path('delete/<int:pk>/', delete_district, name='delete_url'),
]