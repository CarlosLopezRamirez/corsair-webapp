from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({
				'placeholder': field.label,
				'class': "form-control"
			})

class NewUserForm(PlaceholderMixin, UserCreationForm):
	first_name = forms.CharField(max_length=150, required=True, label="First Name")
	last_name = forms.CharField(max_length=150, required=True, label="Last Name")
	email = forms.EmailField(required=True, label="Email")

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

	def getUser(self):
		user = super(NewUserForm, self).save(commit=False)
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		user.email = self.cleaned_data.get('email')
		return user
