from django.contrib.auth.forms import UserCreationForm
from users.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('Cedula_persona', 'Edad_persona', 'Telefono_persona', 'Rol_persona')
