from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None, is_organisation=False):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.is_organisation = is_organisation
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create and save a new super user"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_organisation = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def _str_(self):
        """return string representation of our user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Events for an organisation"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    event_title = models.TextField()
    event_description = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    expires_on = models.DateField()
    is_Expired = models.BooleanField(default=False)
    goal_amount = models.IntegerField()
    received_amount = models.IntegerField(default=0)


class OrgDetails(models.Model):
    """Store details for an organisation"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    location = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)


class DonationHistory(models.Model):
    """Store donation records"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    # event_id = models.IntegerField()
    event_id = models.ForeignKey(
        ProfileFeedItem,
        on_delete=models.CASCADE,
    )

    amount_donated = models.IntegerField()