from django.db import models

# Create your models here.


class Genre(models.Model):
    genre_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.genre_name


class Language(models.Model):
    language_name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.language_name


class Director(models.Model):
    director_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.director_name


class Writer(models.Model):
    writer_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.writer_name


class Cast(models.Model):
    cast_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cast_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=255)
    genre_id = models.ForeignKey(Genre, on_delete=models.RESTRICT)
    release_date = models.DateField()
    language_id = models.ForeignKey(Language, on_delete=models.RESTRICT)
    description = models.CharField(max_length=2500)
    director_id = models.ForeignKey(Director, on_delete=models.RESTRICT)
    writer_id = models.ForeignKey(Writer, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie_name


class Star(models.Model):
    cast_id = models.ForeignKey(Cast, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(models.Model):
    GENDER_CHOICE = (
        (1, 'MALE'),
        (2, 'FEMALE'),
    )
    first_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    gender = models.IntegerField(choices=GENDER_CHOICE)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.User.first_name


class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Movie_Image(models.Model):
    img_path = models.CharField(max_length=1000)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Movie_Video(models.Model):
    video_path = models.CharField(max_length=1000)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
