from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/', blank=True,null=True)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"{self.user.username}-{self.text[:10]}"
