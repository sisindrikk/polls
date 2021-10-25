from django.db import models

class Recipes(models.Model):
    food=models.CharField(max_length=25)
    ingredients=models.TextField(max_length=200)
    process= models.TextField()

    def __str__(self):
        return self.food