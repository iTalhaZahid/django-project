from django.contrib import admin
import firstapp.models as models

# ModelAdmin classes to customize the admin interface
class ActorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth']
    # for enabling search functionality
    search_fields = ['first_name', 'last_name']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth']
    search_fields = ['first_name', 'last_name']

class ContentAdmin(admin.ModelAdmin):
    list_display = ['subtitle', 'video_url']
    search_fields = ['subtitle']

class MovieAdmin(admin.ModelAdmin):
    def getactors(self,current_movie):      #custom method to get actors 
        actors=current_movie.actors.all()   #collecting all actors objects related to the movie
        # actor_list=[]
        # for actor in actors:
        #     fname=actor.first_name
        #     lname=actor.last_name
        #     actor_list.append(f"{fname} {lname}")
        # return actor_list
        names = [f"{a.first_name} {a.last_name}" for a in actors]
        return names
    getactors.short_description = 'ACTORS'
    list_display = ['title', 'rating', 'language', 'release_date','getactors']
    search_fields = ['title', 'description']
    # for enabling filtering options in the admin interface
    list_filter = ['language', 'release_date', 'rating']
    # for better many-to-many relationship handling
    filter_horizontal = ['actors', 'directors', 'genres']
    


# Register models with their respective Admin classes
admin.site.register(models.Actor, ActorAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Director, DirectorAdmin)
admin.site.register(models.Content, ContentAdmin)
admin.site.register(models.Movie, MovieAdmin)