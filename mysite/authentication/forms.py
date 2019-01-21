from django import forms


class AuthUser(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


class SigninUser(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}), max_length=100)
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    file = forms.FileField()
