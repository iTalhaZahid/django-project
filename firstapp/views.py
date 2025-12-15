from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Movie, Actor, Genre, Language, Director, Content



# =========================
# Basic home
# =========================
def home(request):
    movies = (
        Movie.objects
        .select_related('language', 'content')
        .prefetch_related('actors', 'directors', 'genres')
        .all()
    )
    context = {
        'movies': movies,
    }
    return render(request, 'home.html', context)


# =========================
# ACTOR VIEWS
# =========================

def actor_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')

        actor = Actor(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)
        actor.save()

        # redirect to actor list after create
        return redirect('actor_list')

    return render(request, 'actor_create.html')


def fecth_actors(request):  # you might want to rename this to actor_list in urls
    actors = Actor.objects.all()
    genre = Genre.objects.all()
    context = {
        'actors': actors,
        'genres': genre,
    }
    return render(request, 'actor_list.html', context)


def actor_edit(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)

    if request.method == 'POST':
        actor.first_name = request.POST.get('first_name')
        actor.last_name = request.POST.get('last_name')
        actor.date_of_birth = request.POST.get('date_of_birth')
        actor.save()
        return redirect('actor_list')

    context = {
        'actor': actor,
    }
    return render(request, 'actor_edit.html', context)


def actor_delete(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)
    actor.delete()
    return redirect('dashboard')


# =========================
# GENRE VIEWS
# =========================

def create_genre(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = Genre(title=title)
        genre.save()
        # better UX to redirect to a list
        return redirect('genre_list')
    return render(request, 'genre_create.html')


def genre_list(request):
    genres = Genre.objects.all()
    context = {
        'genres': genres,
    }
    return render(request, 'genre_list.html', context)


def edit_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        genre.title = title
        genre.save()
        return redirect('genre_list')

    context = {'genre': genre}
    return render(request, 'genre_edit.html', context)


def delete_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    # this was redirect('view') before (probably a bug)
    return redirect('dashboard')


# =========================
# LANGUAGE VIEWS
# =========================

def language_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        language = Language(title=title)
        language.save()
        return redirect('language_list')

    return render(request, 'language_create.html')


def language_list(request):
    languages = Language.objects.all()
    context = {
        'languages': languages,
    }
    return render(request, 'language_list.html', context)


def language_edit(request, language_id):
    language = get_object_or_404(Language, id=language_id)

    if request.method == 'POST':
        language.title = request.POST.get('title')
        language.save()
        return redirect('language_list')

    context = {
        'language': language,
    }
    return render(request, 'language_edit.html', context)


def language_delete(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    language.delete()
    return redirect('dashboard')


# =========================
# DIRECTOR VIEWS
# =========================

def director_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')

        director = Director(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
        )
        director.save()
        return redirect('director_list')

    return render(request, 'director_create.html')


def director_list(request):
    directors = Director.objects.all()
    context = {
        'directors': directors,
    }
    return render(request, 'director_list.html', context)


def director_edit(request, director_id):
    director = get_object_or_404(Director, id=director_id)

    if request.method == 'POST':
        director.first_name = request.POST.get('first_name')
        director.last_name = request.POST.get('last_name')
        director.date_of_birth = request.POST.get('date_of_birth')
        director.save()
        return redirect('director_list')

    context = {
        'director': director,
    }
    return render(request, 'director_edit.html', context)


def director_delete(request, director_id):
    director = get_object_or_404(Director, id=director_id)
    director.delete()
    return redirect('dashboard')


# =========================
# CONTENT VIEWS
# =========================

def content_create(request):
    if request.method == 'POST':
        subtitle = request.POST.get('subtitle')
        video_url = request.POST.get('video_url')

        content = Content(subtitle=subtitle, video_url=video_url)
        content.save()
        return redirect('content_list')

    return render(request, 'content_create.html')


def content_list(request):
    contents = Content.objects.all()
    context = {
        'contents': contents,
    }
    return render(request, 'content_list.html', context)


def content_edit(request, content_id):
    content = get_object_or_404(Content, id=content_id)

    if request.method == 'POST':
        content.subtitle = request.POST.get('subtitle')
        content.video_url = request.POST.get('video_url')
        content.save()
        return redirect('content_list')

    context = {
        'content': content,
    }
    return render(request, 'content_edit.html', context)


def content_delete(request, content_id):
    content = get_object_or_404(Content, id=content_id)
    content.delete()
    return redirect('dashboard')


# =========================
# MOVIE VIEWS
# =========================

def movie_create(request):
    """
    Note: in movie_create.html form, you MUST use:
    <form method="post" enctype="multipart/form-data"> ... </form>
    so poster file uploads work.
    """
    actors = Actor.objects.all()
    languages = Language.objects.all()
    directors = Director.objects.all()
    contents = Content.objects.all()
    genres = Genre.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        language_id = request.POST.get('language')
        content_id = request.POST.get('content')  # can be empty
        release_date = request.POST.get('release_date')

        # ManyToMany - list of actor, director, and genre ids
        actor_ids = request.POST.getlist('actors')
        director_ids = request.POST.getlist('directors')
        genre_ids = request.POST.getlist('genres')

        poster = request.FILES.get('poster')  # might be None

        language = get_object_or_404(Language, id=language_id)

        content_obj = None
        if content_id:
            content_obj = get_object_or_404(Content, id=content_id)

        movie = Movie(
            title=title,
            description=description,
            rating=rating or 0,
            language=language,
            poster=poster,
            content=content_obj,
            release_date=release_date,
        )
        movie.save()

        # Set ManyToMany fields after save
        if actor_ids:
            movie.actors.set(actor_ids)
        if director_ids:
            movie.directors.set(director_ids)
        if genre_ids:
            movie.genres.set(genre_ids)

        return redirect('movie_list')

    context = {
        'actors': actors,
        'languages': languages,
        'directors': directors,
        'contents': contents,
        'genres': genres,
    }
    return render(request, 'movie_create.html', context)


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movie_list.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    context = {
        'movie': movie,
    }
    return render(request, 'movie_detail.html', context)


def movie_edit(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    actors = Actor.objects.all()
    languages = Language.objects.all()
    directors = Director.objects.all()
    contents = Content.objects.all()
    genres = Genre.objects.all()

    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.description = request.POST.get('description')
        movie.rating = request.POST.get('rating') or 0

        language_id = request.POST.get('language')
        content_id = request.POST.get('content')
        movie.release_date = request.POST.get('release_date')

        movie.language = get_object_or_404(Language, id=language_id)

        if content_id:
            movie.content = get_object_or_404(Content, id=content_id)
        else:
            movie.content = None

        # handle poster update if a new file is uploaded
        poster = request.FILES.get('poster')
        if poster:
            movie.poster = poster

        movie.save()

        # update ManyToMany fields
        actor_ids = request.POST.getlist('actors')
        director_ids = request.POST.getlist('directors')
        genre_ids = request.POST.getlist('genres')
        movie.actors.set(actor_ids)
        movie.directors.set(director_ids)
        movie.genres.set(genre_ids)

        return redirect('movie_detail', movie_id=movie.id)

    context = {
        'movie': movie,
        'actors': actors,
        'languages': languages,
        'directors': directors,
        'contents': contents,
        'genres': genres,
    }
    return render(request, 'movie_edit.html', context)


def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('dashboard')

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    context = {'movie': movie}
    return render(request, 'movie_detail.html', context)


# =========================
# Dashboard VIEWS
# =========================


@login_required(login_url='signin')
def dashboard(request):
    movies = Movie.objects.all()
    actors = Actor.objects.all()
    genres = Genre.objects.all()
    languages = Language.objects.all()
    directors = Director.objects.all()
    contents = Content.objects.all()

    context = {
        'movies': movies,
        'actors': actors,
        'genres': genres,
        'languages': languages,
        'directors': directors,
        'contents': contents,
    }
    return render(request, 'dashboard.html', context)



# =========================
# AUTH (Signup / Signin / Signout)
# =========================
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username or not password1:
            messages.error(request, 'Username and password are required.')
            return render(request, 'signup.html')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        # Auto-login after signup
        user = authenticate(request, username=username, password=password1)
        if user:
            auth_login(request, user)
            return redirect('home')

    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'signin.html')
    return render(request, 'signin.html')


def signout(request):
    auth_logout(request)
    return redirect('home')
