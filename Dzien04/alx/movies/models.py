from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Comment(models.Model):
    body = models.TextField()
    stars = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.stars} - {self.body}"

    class Meta:
        verbose_name = "Komentarz"
        verbose_name_plural = "Komentarze"


class Movie(models.Model):

    def check_title_len(s):
        if len(s.strip()) < 2:
            raise ValidationError(message="Za krótki tytuł")

    MPAA = (
        ("-","Brak"),
        ("PG-13","Za zgodą rodziców"),
        ("NC-17","Powyżej 17-go roku życia"),
    )

    def create_path(instance, filename):
        pass

    title = models.CharField(max_length=255, verbose_name="Tytuł", validators=[check_title_len])
    description = models.TextField(max_length=1024, verbose_name="Opis")
    released = models.DateField(verbose_name="Data premiery", null=True, blank=True)
    year = models.IntegerField(null=True, blank=True, editable=False)
    imdb = models.DecimalField(null=True, blank=True, verbose_name="Ocena", max_digits=4, decimal_places=2 )
    trailer = models.URLField(null=True,blank=True, verbose_name="Link do trailera")
    poster = models.ImageField(null=True, blank=True, verbose_name="Plakat", unique=False)
    mpaa_rating = models.CharField(max_length=100, choices=MPAA, default="-", verbose_name="Rating MPAA")

    created = models.DateTimeField(editable=False, auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                   null=True, editable=False)

    def __str__(self):
        return f"{self.title} - {self.year if self.year else 'BRAK DATY'}"

    def save(self, *args, **kwargs):
        if self.released:
            self.year = self.released.year
        super(Movie, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmy"
