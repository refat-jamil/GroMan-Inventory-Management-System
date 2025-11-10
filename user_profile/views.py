# user_profile/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UserForm
from .models import Profile

@login_required
def profile_view(request):
    return render(request, 'profile/profile.html')

@login_required
def profile_edit(request):
    # Ensure the user has a profile
    profile, created = Profile.objects.get_or_create(user=request.user)

    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=profile)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

    return render(request, 'profile/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
