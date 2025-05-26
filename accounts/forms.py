from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile  # Importing your profile model

class RegisterForm(forms.ModelForm):
    full_name = forms.CharField(max_length=255, required=True)  # New field for full names
    bio = forms.CharField(widget=forms.Textarea, required=False)
    address = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match!")
        
        if User.objects.filter(username=cleaned_data.get('username')).exists():
            self.add_error('username', "This username is already taken!")

        if User.objects.filter(email=cleaned_data.get('email')).exists():
            self.add_error('email', "An account with this email already exists!")

        return cleaned_data
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash password before saving
        
        if commit:
            user.save()
            profile, created = Profile.objects.get_or_create(user=user)
            
            # Debugging output
            if created:
                print(f"✅ Profile created for user: {user.username}")
            else:
                print(f"⚠️ Profile already exists for user: {user.username}")
            
            profile.full_name = self.cleaned_data.get('full_name', '')  # Assign profile data
            profile.bio = self.cleaned_data.get('bio', '')
            profile.phone_number = self.cleaned_data.get('phone_number', '')
            profile.address = self.cleaned_data.get('address', '')
            profile.save()  # Ensure it saves
        
        return user
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'profile_pic', 'phone_number', 'address']

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.full_name = self.cleaned_data.get('full_name', '')  # Ensure full_name is assigned
        profile.bio = self.cleaned_data.get('bio', '')  # Explicitly assign bio
        
        if commit:
            profile.save()
        return profile

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'Please enter your username'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'Please enter your password'}
    )