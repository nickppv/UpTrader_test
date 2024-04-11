from django.urls import path
from just_menu import views

app_name = 'just_menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:country>/', views.brand, name='brand'),
    path('<str:country>/<str:brand>/', views.model, name='models'),
]
