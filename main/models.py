from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    steps = models.TextField()
    time_to_cook = models.CharField(max_length=100)
    img = models.ImageField()
    author = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f'{self.title}, {self.time_to_cook}, {self.author}'
    
class Category(models.Model):
    title = models.CharField(max_length=200)
    
class Group(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
