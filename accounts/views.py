from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, ProfileForm
from .models import Profile
from django.http import HttpResponse

def account_home(request):
    user_status = "Logged in" if request.user.is_authenticated else "Guest"
    return HttpResponse(f"This is the accounts home page. User Status: {user_status}")

# User Registration View
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Check if the profile already exists
            profile, created = Profile.objects.get_or_create(user=user)

            if created:
                print(f"✅ Profile created for user: {user.username}")
            else:
                print(f"⚠️ Profile already exists for user: {user.username}")

            login(request, user)  
            return redirect('profile')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

# User Login View (using Django's built-in LoginView in urls.py)
# User Logout View (using Django's built-in LogoutView in urls.py)

# User Profile View
@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form, 'profile': profile, 'user': request.user})  # Make sure profile is passed

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect back to profile after updating
    else:
        form = ProfileForm(instance=profile)  # Pre-fill form with existing data

    return render(request, 'edit_profile.html', {'form': form})
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'