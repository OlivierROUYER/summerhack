from django.contrib.auth import get_user_model, authenticate
from django import forms

UserModel = get_user_model()


class ConnexionForm(forms.Form):
    username = forms.CharField(label=('Username'), max_length=50, required=True,
                               widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=('Password'), max_length=50, required=True,
                               widget=forms.PasswordInput(attrs={'autofocus': True}))

    error_messages = {
        'not_valid': ('This username is not valid')
    }

    def clean(self):
        try:
            cleaned_data = super(ConnexionForm, self).clean()
            if cleaned_data['username'] and cleaned_data['password']:
                username = cleaned_data.get('username')
                UserModel.objects.filter(username=username, password=cleaned_data['password']).count()
                print(UserModel.objects.filter(username=username, password=cleaned_data['password']))
                authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
        except Exception:
            print("error clean in login_form")

    class Meta:
        model = UserModel
        fields = 'username', 'password'

        widgets = {
            'class': 'form-control',
            'username': forms.TextInput(
                attrs={
                    'class': 'my-class',
                    'placeholder': 'Name goes here',
                }),
            'password': forms.HiddenInput(
                attrs={
                    'class': 'my-class',
                    'placeholder': 'Password',
                }),
        }
