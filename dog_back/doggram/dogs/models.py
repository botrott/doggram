from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Achievement(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birth_year = models.IntegerField()
    owner = models.ForeignKey(
        User, related_name='dogs', 
        on_delete=models.CASCADE
        )
    achievements = models.ManyToManyField(Achievement, through='AchievementCat')
    image = models.ImageField(
        upload_to='dogs/images/', 
        null=True,  
        default=None
        )

    def __str__(self):
        return self.name


class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.dog}'