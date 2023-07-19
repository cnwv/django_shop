from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User


class UserAdminRegisterForm(UserRegisterForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'username', 'email', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar', 'username', 'email', 'avatar')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'
