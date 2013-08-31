from django import forms
from rest_framework.serializers import CharField, ImageField

HIDDEN_PASSWORD_STRING='<hidden>'

class PasswordField(CharField):
    """Special field to update a password field."""
    widget = forms.widgets.PasswordInput
                
    def from_native(self, value):
        """
        Hash if new value sent, else retrieve current password.
        Only problem is that you cannot set your password as <hidden>
        """
        from django.contrib.auth.hashers import make_password
        if value == HIDDEN_PASSWORD_STRING or value == '':
            return self.parent.object.password
        else:
            return make_password(value)

    def to_native(self, value):
        """Hide hashed-password in API display"""
        return HIDDEN_PASSWORD_STRING

class HyperlinkedImageField(ImageField):
    def to_native(self, value):
        request = self.context.get('request', None)
        if request and value.name:
            return request.build_absolute_uri(value.url)
        else:
            return super(HyperlinkedImageField, self).to_native(value)
