import logging

from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import SetPasswordMixin
from django.contrib.auth.forms import UsernameField

UserModel = get_user_model()
logger = logging.getLogger("django.contrib.auth")

class MySetPasswordMixin(SetPasswordMixin):
    """
    Form mixin that validates and sets a password for a user.
    """

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }

    @staticmethod
    def create_password_field(label=_("Password")):
        password = forms.CharField(
            label=label,
            required=False,
            strip=False,
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
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
    """
    A form that creates a user, with no privileges, from the given username and
    password.

    This is the documented base class for customizing the user creation form.
    It should be kept mostly unchanged to ensure consistency and compatibility.
    """

    password = MySetPasswordMixin.create_password_field()

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

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