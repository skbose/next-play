from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, user_id, email, password=None, **extra_fields):
        if not user_id or not email:
            raise ValueError('The User ID and Email fields must be set')
        email = self.normalize_email(email)
        user = self.model(user_id=user_id, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(user_id, email, password, **extra_fields)

class User(AbstractBaseUser):
    user_id = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=50, choices=[('candidate', 'Candidate'), ('recruiter', 'Recruiter')])

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['email', 'name', 'user_type']

    def __str__(self):
        return self.user_id
# class User(AbstractUser):
#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"

class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=255)  # Store hashed password
    user_type = models.CharField(max_length=50, choices=[('candidate', 'Candidate'), ('recruiter', 'Recruiter')])  # Added user_type field

    def __str__(self):
        return self.user.user_id
# class Login(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)

#     user_type = models.CharField(max_length=50)

#     class Meta:
#         verbose_name = "Login"
#         verbose_name_plural = "Logins"