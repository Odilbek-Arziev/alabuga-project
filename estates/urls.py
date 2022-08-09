from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('hierarchy/<str:value>', views.hierarchy, name='hierarchy'),
    path('create_dweller/', views.create_dweller, name='create_dweller'),
    path('edit_dweller/<int:pk>', views.edit_dweller, name='edit_dweller'),
    path('delete_dweller/<int:pk>', views.delete_dweller, name='delete_dweller'),
]