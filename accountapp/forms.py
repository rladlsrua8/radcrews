from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class AccountUdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True