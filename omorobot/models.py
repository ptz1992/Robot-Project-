from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=200, null=True)
  models = models.CharField(max_length=200, null=True)


    
class Minicar(models.Model):
  speed = models.IntegerField(null=True)
  battery = models.IntegerField(null=True)
  color = models.TextField(null=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  user = models.ForeignKey("User", on_delete=models.CASCADE, null=True)
