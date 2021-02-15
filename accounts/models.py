from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.sessions.models import Session
import datetime
from django.core.cache import cache
from django.conf import settings
from PIL import Image


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, phone, password, **extra_fields):
        values = [email, first_name, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    organization = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    share_my_contact = models.BooleanField(default=False,null=True,blank=True)
    update_through_email = models.BooleanField(default=False,null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', ]

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=150)
    image = models.ImageField(
        default='avatar-icon.png', upload_to='media/profile_pics')

    def __str__(self):
        return f'{self.first_name} Profile'

    def last_seen(self):
        return cache.get('seen_%s' % self.user.first_name)

    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > self.last_seen() + datetime.timedelta(
                         seconds=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False



    # def get_all_logged_in_users(self):
    #     sessions = Session.objects.filter(expire_date__gte=timezone.now())
    #     uid_list = []

    #     for session in sessions:
    #         data = session.get_decoded()
    #         uid_list.append(data.get('_auth_user_id', None))

    #     return CustomUser.objects.filter(id__in=uid_list)





def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,first_name=instance.first_name, last_name=instance.last_name, phone=instance.phone, email=instance.email)

post_save.connect(create_profile, sender=CustomUser)


