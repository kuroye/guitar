from django.db import models

# Create your models here.

class Song(models.Model):

    def string_default():
        return {"s6": "E2",
                "s5": "A2",
                "s4": "D3",
                "s3": "G3",
                "s2": "B3",
                "s1": "E4"}

    name = models.CharField(max_length=50)
    guitar_string = models.JSONField('StringInfo', default=string_default)

