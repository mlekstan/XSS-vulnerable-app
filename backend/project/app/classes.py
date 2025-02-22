from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import SetPasswordMixin
from django.contrib.auth.forms import UsernameField


class MySetPasswordMixin(SetPasswordMixin):

    @staticmethod
    def create_password_field():
        password = forms.CharField(
            required=True,
            strip=False,
            widget=forms.PasswordInput(),
            help_text=password_validation.password_validators_help_text_html(),
        )
        
        return password

    def validate_password(self, password_field_name="password"):
        password = self.cleaned_data.get(password_field_name)

        if not password and password_field_name not in self.errors:
            error = ValidationError(
                self.fields[password_field_name].error_messages["required"],
                code="required",
            )
            self.add_error(password_field_name, error)

    def validate_password_for_user(self, user, password_field_name="password"):
        password = self.cleaned_data.get(password_field_name)
        if password:
            try:
                password_validation.validate_password(password, user)
            except ValidationError as error:
                self.add_error(password_field_name, error)

    def set_password_and_save(self, user, password_field_name="password", commit=True):
        user.set_password(self.cleaned_data[password_field_name])
        if commit:
            user.save()
        return user

class MyBaseUserCreationForm(MySetPasswordMixin, forms.ModelForm):
    password = MySetPasswordMixin.create_password_field()
    password.widget.attrs.update({"class": "form-control", "id": "reg-password", "name": "password"})

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control", "id": "reg-email", "name": "email"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password")
        field_classes = {"username": UsernameField}
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "id": "reg-username", "name": "username"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs["autofocus"] = True


    def clean(self):
        self.validate_password()
        return super().clean()

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        self.validate_password_for_user(self.instance)

    def save(self, commit=True):
        user = super().save(commit=False)
        user = self.set_password_and_save(user, commit=commit)
        if commit and hasattr(self, "save_m2m"):
            self.save_m2m()
        return user