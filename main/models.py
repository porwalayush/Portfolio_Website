from django.db import models

# Create your models here.
class New_Message(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=254)
    Subject = models.TextField()
    Message = models.TextField()
    def __str__(self):
        return str(self.Name)
