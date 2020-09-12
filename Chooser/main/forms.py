from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class JoinForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'nickname',)
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
 
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
    # email = forms.CharField(
    #     max_length=30,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'nickname',
    #             'required': 'True',
    #         }
    #     )
    # )
    # password = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'PASSWORD',
    #             'required': 'True',
    #         }
    #     )
    # )