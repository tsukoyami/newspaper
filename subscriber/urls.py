
from django.urls import path
from . import views

urlpatterns = [
    path('api/subscriber/', views.subscriber),
]
