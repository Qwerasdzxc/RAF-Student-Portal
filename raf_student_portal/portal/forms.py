from django.forms import ModelForm, Form
import django.forms as f
from .models import Subject, News
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    first_name = f.CharField(max_length=30)
    last_name = f.CharField(max_length=30)
    email = f.EmailField(max_length=128, help_text='Required. Inform a valid email address.')
    birth_date = f.DateField(required=False, help_text='Optional. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date')

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description']

class NewsForm(ModelForm):
    subject = f.ModelChoiceField(queryset=Subject.objects.all())

    class Meta:
        model = News
        fields = ['title', 'description', 'subject']
