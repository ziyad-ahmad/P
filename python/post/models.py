from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Post(models.Model):
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Posts',blank=True)

    def __str__(self):
        return f'{self.auther} - {self.content[:20]}'