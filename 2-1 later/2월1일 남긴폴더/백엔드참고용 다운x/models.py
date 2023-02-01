from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=200, primary_key=True, null=False)
  models = models.CharField(max_length=200)

  def get_delete_url(self) :
    return f"deleteuser/{self.pk}/"
  
  def get_update_url(self) :
    return f"updateuser/{self.pk}/"

    
class Minicar(models.Model):
  speed = models.IntegerField(default=0, null=True)
  battery = models.IntegerField(default=0, null=True)
  color = models.TextField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  # user = models.ForeignKey("User", on_delete=models.CASCADE)

  def get_delete_url00(self) :
    return f"deleteminicar/{self.pk}/"
  
  def get_update_url00(self) :
    return f"updateminicar/{self.pk}/"
