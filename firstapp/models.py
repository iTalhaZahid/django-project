from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Actor(models.Model):
    first_name = models.CharField(max_length=30)    #Char field for short text and TextField for long text(unlimited length)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
class Language(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Content(models.Model):
    subtitle = models.CharField(max_length=100)
    video_url = models.URLField()
    def __str__(self):
        return self.subtitle
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.FloatField()
    actors = models.ManyToManyField(Actor)
    # duration = models.TimeField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    directors = models.ManyToManyField(Director)  # Changed from ForeignKey to ManyToManyField
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, null=True, blank=True)
    genres = models.ManyToManyField(Genre)  # Changed from ForeignKey to ManyToManyField
    release_date = models.DateField()
    def __str__(self):
        return self.title