from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            print(f"User found: {user.email}, Hashed Password: {user.password}")  # Debugging
            if user.check_password(password):
                return user
            else:
                print("Password mismatch")
        except User.DoesNotExist:
            print("User does not exist")
        return None
