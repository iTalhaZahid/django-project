from django.urls import path
from . import views

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # ===============================
    # ACTORS
    # ===============================
    path('actors/', views.fecth_actors, name='actor_list'),
    path('actors/create/', views.actor_create, name='actor_create'),
    path('actors/<int:actor_id>/edit/', views.actor_edit, name='actor_edit'),
    path('actors/<int:actor_id>/delete/', views.actor_delete, name='actor_delete'),

    # ===============================
    # GENRES
    # ===============================
    path('genres/', views.genre_list, name='genre_list'),
    path('genres/create/', views.create_genre, name='genre_create'),
    path('genres/<int:genre_id>/edit/', views.edit_genre, name='genre_edit'),
    path('genres/<int:genre_id>/delete/', views.delete_genre, name='genre_delete'),

    # ===============================
    # LANGUAGES
    # ===============================
    path('languages/', views.language_list, name='language_list'),
    path('languages/create/', views.language_create, name='language_create'),
    path('languages/<int:language_id>/edit/', views.language_edit, name='language_edit'),
    path('languages/<int:language_id>/delete/', views.language_delete, name='language_delete'),

    # ===============================
    # DIRECTORS
    # ===============================
    path('directors/', views.director_list, name='director_list'),
    path('directors/create/', views.director_create, name='director_create'),
    path('directors/<int:director_id>/edit/', views.director_edit, name='director_edit'),
    path('directors/<int:director_id>/delete/', views.director_delete, name='director_delete'),

    # ===============================
    # CONTENT
    # ===============================
    path('contents/', views.content_list, name='content_list'),
    path('contents/create/', views.content_create, name='content_create'),
    path('contents/<int:content_id>/edit/', views.content_edit, name='content_edit'),
    path('contents/<int:content_id>/delete/', views.content_delete, name='content_delete'),

    # ===============================
    # MOVIES
    # ===============================
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/create/', views.movie_create, name='movie_create'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_id>/edit/', views.movie_edit, name='movie_edit'),
    path('movies/<int:movie_id>/delete/', views.movie_delete, name='movie_delete'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),


    # ===============================
    # DASHBOARD (Combined all tables)
    # ===============================
    path('dashboard/', views.dashboard, name='dashboard'),

]
