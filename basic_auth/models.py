from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Student(models.Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=20)
    score = IntegerField()

    def __str__(self):
        return self.name