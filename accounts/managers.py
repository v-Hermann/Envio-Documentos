from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, fullname=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        # Normalize the email address
        email = self.normalize_email(email)

        # Set the username to the email value
        extra_fields.setdefault('username', email)

        # Create a new instance of the user model
        user = self.model(email=email, fullname=fullname, **extra_fields)

        # Set the password
        user.set_password(password)

        # Save the user instance to the database
        user.save()

        return user

    def create_superuser(self, email, password=None, fullname=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, fullname, **extra_fields)