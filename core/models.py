from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=255, default="New Project")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    number_of_rooms = models.IntegerField()
    input_data_json = models.CharField(max_length=2048)
    output_data_json = models.CharField(max_length=2048)

    def __str__(self):
        return self.name
