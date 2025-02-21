from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=255)  # Ensure this field exists
    email = models.EmailField(primary_key=True, unique=True)
    password = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email

# Expense Model
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Groceries', 'Groceries'),
        ('Leisure', 'Leisure'),
        ('Electronics', 'Electronics'),
        ('Utilities', 'Utilities'),
        ('Clothing', 'Clothing'),
        ('Health', 'Health'),
        ('Others', 'Others'),
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    dateandtime = models.DateTimeField(auto_now_add=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.category} - {self.amount}"
