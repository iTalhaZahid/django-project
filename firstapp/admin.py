from django.contrib import admin
import firstapp.models as models
# Register your models here.
admin.site.register(models.Actor)
admin.site.register(models.Genre)
admin.site.register(models.Language)
admin.site.register(models.Director)
admin.site.register(models.Content)
admin.site.register(models.Movie)