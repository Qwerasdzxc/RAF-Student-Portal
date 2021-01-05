from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

class News(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)    
