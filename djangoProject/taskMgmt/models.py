#models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Task(models.Model):
    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True)
    due_time = models.TimeField(null=True)
    urgent = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    description = models.TextField(max_length=255, null=True)
    completed = models.BooleanField(default=False)

'''class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Hunt(models.Model):
    hunt_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    event_date = models.DateField()

class Clue(models.Model):
    clue_id = models.AutoField(primary_key=True)
    hunt = models.ForeignKey(Hunt, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    name = models.CharField(max_length=100)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    hunt = models.ForeignKey(Hunt, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    point_value = models.IntegerField()

class Participant(models.Model):
    participant_id = models.AutoField(primary_key=True)
    team_id = models.IntegerField()  # Assume linked to a Teams table or modify as required
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    points = models.IntegerField()

class TaskCompletion(models.Model):
    task_completion_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    points = models.IntegerField()
    completion_time = models.DateTimeField()
    progress = models.CharField(max_length=100)'''

def __str__(self):
        return self.title
