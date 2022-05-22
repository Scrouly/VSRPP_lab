from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, name, surname, address, username, email, groups = Group.objects.get(pk=1), password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a nickname')
        if not name:
            raise ValueError('User must have a nickname')
        if not surname:
            raise ValueError('User must have a nickname')
        if not address:
            raise ValueError('User must have a nickname')

        user = self.model(
            groups = groups,
            username=username,
            name=name,
            surname=surname,
            address=address,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, surname, address, username, email, groups, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        SuperUser = self.create_user(
            groups=Group.objects.get(pk=groups),
            username=username,
            name=name,
            surname=surname,
            address=address,
            email=email,
            password=password,
        )
        SuperUser.is_staff = True
        SuperUser.is_admin = True
        SuperUser.save(using=self._db)
        return SuperUser


class User(AbstractBaseUser):
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=50, unique=True, null=True)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, default=2)
    email = models.EmailField(max_length=50, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['groups','name', 'surname', 'address', 'email']

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Books(models.Model):
    book_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=150,null=True)
    in_stock = models.BooleanField(default=True)
    in_stock_status_date = models.DateTimeField(auto_now=True)
    added_date = models.DateTimeField(auto_now_add=True)
    renter = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.gr_name}"

    class Meta:
        db_table = 'books'
