from django.contrib import admin
from .models import Director, Writer, Cast, Genre, Language, Movie


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'director_name')


class WriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'writer_name')


class CastAdmin(admin.ModelAdmin):
    list_display = ('id', 'cast_name')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre_name')


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'language_name')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_name', 'genre_id', 'release_date',
                    'language_id', 'director_id', 'writer_id')


# Register your models here.admin.site.register(Director)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Writer, WriterAdmin)
admin.site.register(Cast, CastAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Movie, MovieAdmin)
