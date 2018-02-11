from django.urls import path
from . import views

app_name = "rest"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('index_image/<int:pk>/', views.index_image, name="index_image"),
]