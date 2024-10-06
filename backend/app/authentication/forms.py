from django import forms
from .models import User, Login


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['user_id', 'email', 'name', 'user_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        email = self.cleaned_data.get("email")
        if commit:
            user.set_password(password)  # Hash the password
            user.save()
            login_entry = Login(user=user, email=email, password=user.password)  # Save email and hashed password
            login_entry.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
