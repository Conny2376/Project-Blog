from django.db import models
from .models import User

# Create your models here.
class CustomUser(models.Model):
    ROLE_CHOICES = [
        ('admin', "Адміністратор"),
        ('user', "Користувач"),
    ]
    name = models.CharField("Ім'я", max_length=100),
    email = models.EmailField('Email', unique=True)
    role = models.CharField("Роль", max_length=10, choices=ROLE_CHOICES,
                            default='user')
    
    def __str__(self):
        return f"{self.name} ({self.email}) - {self.role}"
    
class UserGroup(models.Model):
    name = models.CharField("Назва групи", max_length=100)
    users = models.ManyToManyField(User, related_name='groups', verbose_name="Користувачі")

    def __str__(self):
        return self.name
