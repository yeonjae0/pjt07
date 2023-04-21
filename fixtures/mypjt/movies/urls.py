from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:pk>/', views.actor_detail),
    path('movies/', views.movie_list),
    path('movies/<int:pk>/', views.movie_detail),
    path('reviews/', views.review_list),
    path('reviews/<int:pk>/', views.review_detail),
    path('movies/<int:pk>/reviews/', views.create_review),
]
