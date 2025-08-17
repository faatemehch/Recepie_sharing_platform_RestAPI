from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.name)


class Recepie(models.Model):
    DIFFICULTY = (
        ('e', 'Easy'),
        ('m', 'Medium'),
        ('h', 'Hard'),
    )
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, db_index=True)
    # author = models.ForeignKey()
    short_description = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    calories_per_serving = models.PositiveIntegerField()
    # image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
