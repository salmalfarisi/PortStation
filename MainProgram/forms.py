#from django.forms import ModelForm
from .models import *

# ubah bentuk form
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Submit

# login and registration form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
        
class CreateUserForm(UserCreationForm, forms.ModelForm):
    first_name = forms.CharField(max_length=100,required=True, widget= forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, required=True,widget= forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=254, help_text='Inform a valid email address.',widget= forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=50, help_text='Make unique username. Max. 50 characters',widget= forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        #fields = '__all__'
        fields = ('username', 'email', 'first_name', 'last_name')
		
class FileForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')
	
	
	# class Meta:
        # model = Image
        # fields = ('name', 'desc', 'picture')
    
    # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # self.helper = FormHelper()
        # self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Create'))
		
class ProfileForm(forms.ModelForm):
	first_name = forms.CharField(max_length=100, required=True, widget= forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=100, required=True, widget= forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(max_length=254, required=True, widget= forms.TextInput(attrs={'class':'form-control'}))
	username = forms.CharField(max_length=50, required=True, widget= forms.TextInput(attrs={'class':'form-control'}))
	#picture = forms.ImageField()
	
	class Meta:
		model = User
		#fields = '__all__'
		fields = ('username', 'email', 'first_name', 'last_name')
		
class UserImageForm(forms.ModelForm):
	users = forms.CharField(widget=forms.HiddenInput(), required=False)
	imageprofile = forms.ImageField()
	
	class Meta:
		model = UserImageProfile
		fields = ('users', 'imageprofile',)
		
class CreatePostForm(forms.ModelForm):
	title = forms.CharField(max_length=240, required=True, widget= forms.TextInput(attrs={'class':'form-control'}))
	desc = forms.CharField(max_length=1000, required=False, widget= forms.Textarea(attrs={'class':'form-control', 'rows':'5'}))
	
	class Meta:
		model = Post
		fields = ('title', 'desc',)
		
class CreateCommentForm(forms.ModelForm):
	comment = forms.CharField(max_length=500, required=True, widget= forms.Textarea(attrs={'class':'form-control', 'rows':'5'}))
	
	class Meta:
		model = PostComment
		fields = ('comment', )
		
class CreateForumForm(forms.ModelForm):
	title = forms.CharField(max_length=240, required=True, widget= forms.TextInput(attrs={'class':'form-control'}))
	article = forms.CharField(max_length=3000, required=True, widget= forms.Textarea(attrs={'class':'form-control', 'rows':'10'}))
	
	class Meta:
		model = Forum
		fields = ('title', 'article')