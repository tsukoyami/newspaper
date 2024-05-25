
from django.urls import path
from . import views

urlpatterns = [
    path('story/', views.story, name='story'),  # To render index.html
    path('api/story/', views.story_list, name='story_list'),
    path('api/story/<int:pk>/', views.story_detail, name='story_detail'),
    path('api/search_story/', views.search_story, name='search_sources'),
    path('api/filter_story/', views.filter_story_by_tag, name='filter_sources_by_tag'),
]
