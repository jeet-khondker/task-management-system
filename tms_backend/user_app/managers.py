from django.contrib.auth.models import BaseUserManager

"""
Custom User Account Model Manager
'email' is the unique identifier for authentication instead of 'username'
"""

class UserAccountManager(BaseUserManager):

    """
    Create and save a User with the given email, full name and password
    """
    def create_user(self, email, full_name, password):
        if not email:
            raise ValueError("メールアドレスが必要です。")
        if not full_name:
            raise ValueError("氏名が必要です。")

        email = self.normalize_email(email)

        user_account = self.model(email = email, full_name = full_name,)

        user_account.set_password(password)
        user_account.save(using = self._db)

        return user_account

    """
    Create and save a SuperUser with the given email, full name and password
    """
    def create_superuser(self, email, full_name, password):
        email = self.normalize_email(email)

        user_account = self.create_user(email = email, full_name = full_name, password = password,)

        user_account.is_admin = True
        user_account.is_staff = True
        user_account.is_superuser = True

        user_account.save(using = self._db)

        return user_account