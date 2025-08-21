from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.name)


class Recipe(models.Model):
    DIFFICULTY = (
        ('e', 'Easy'),
        ('m', 'Medium'),
        ('h', 'Hard'),
    )
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
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


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Customers"
        ordering = ['-joined_at']


class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='comments')
    name = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)
