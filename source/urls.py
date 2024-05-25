
from django.urls import path
from . import views

urlpatterns = [
    path('source/', views.source, name='source'),
    path('api/source/', views.source_list),
    path('api/source/<int:pk>', views.source_detail),
    path('api/fetch-stories/<int:source_id>/', views.FetchStoriesView.as_view(), name='fetch_stories'),
    path('api/search/', views.search_sources, name='search_sources'),
    path('api/filter/', views.filter_sources_by_tag, name='filter_sources_by_tag'),
]
