from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Sign_Up_Form(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class Blog_Post_Form(forms.Form):
    pass


class Blog_Feed_Back(forms.Form):
    comment = forms.CharField(max_length=2000, widget = forms.Textarea(attrs={'rows': 4, 'cols': 40}), help_text='Write here your message!', label='') 
