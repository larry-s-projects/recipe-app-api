from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """Extending from BaseUserManager. this is the manager class

    Args:
        BaseUserManager ([type]): [description]
    """

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user. self.model creates a new user model. 
        Normalize_email is a helper function that comes with the BaseUserManager """

        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        #helper function comes with the django abstract base user
        user.set_password(password)

        #self._db is just required to support multiple databases
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


        return user



class User(AbstractBaseUser, PermissionsMixin):
    """This is the model itself. Custom user model that supports using email instea of username

    Args:
        AbstractBaseUser ([type]): [description]
        PermissionsMixin ([type]): [description]
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # This is just to determine if the user in a system is active or not
    is_active = models.BooleanField(default=True)

    # If you want to create a staff user, you are going to have to use a special command
    is_staff = models.BooleanField(default=False)

    objects = UserManager() # creating a new user manager for our object

    USERNAME_FIELD = "email"

