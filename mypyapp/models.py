from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name