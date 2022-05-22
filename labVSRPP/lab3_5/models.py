from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, nickname, email, groups=Group.objects.get(pk=2), password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not nickname:
            raise ValueError('Users must have a nickname')

        user = self.model(
            nickname=nickname,
            email=self.normalize_email(email),
            groups=groups,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, email, password, groups):
        """
        Creates and saves a superuser with the given email and password.
        """
        SuperUser = self.create_user(
            email=email,
            nickname=nickname,
            groups=Group.objects.get(pk=groups),
            password=password,
        )
        SuperUser.is_staff = True
        SuperUser.is_admin = True
        SuperUser.save(using=self._db)
        return SuperUser


class User(AbstractBaseUser):
    # username = None
    nickname = models.CharField(max_length=50, unique=True, null=True)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, default=2)
    email = models.EmailField(max_length=50, unique=True)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['groups', 'email']

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Groups(models.Model):
    group_id = models.BigAutoField(primary_key=True)
    gr_name = models.CharField(max_length=45, blank=True, null=True, unique=True)
    faculty = models.ForeignKey("Faculty", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.gr_name}"

    class Meta:
        db_table = 'groups'


class Students(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    surname = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    group = models.ForeignKey(Groups, models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField(User,models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.group}"

    class Meta:
        db_table = 'students'


class Faculty(models.Model):
    id = models.BigAutoField(primary_key=True)
    faculty_name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.faculty_name}"

    class Meta:
        db_table = 'faculty'
