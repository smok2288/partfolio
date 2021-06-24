from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django import forms
from .apps import user_registered
# from blog.admin import PostAdmin
# from blog.admin import PostAdmin


class RegisterUserForm(forms.Form):
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(label='пароль', widget=forms.PasswordInput, help_text='Введите пароль')
    password2 = forms.CharField(label='Пароль повторно', widget=forms.PasswordInput, help_text='введите пароль повторно')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError:
                # self.add_error('password', ValidationError.message)
                raise ValidationError
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password1': ValidationError('Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()

        user_registered.send(RegisterUserForm)
        return user

    # class Meta:
    #     model = PostAdmin
    #     fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'send_massages')