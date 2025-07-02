from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm, ProfileChangeForm
from accounts.models import CustomUser, Profile


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, F"{user.username} foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi!")
            return redirect('accounts:login')
    else:
        messages.warning(request, F"Biz hozirda test rejimida ishlayapmiz!")
        form = CustomUserCreationForm()
    context = {
        "form": form
    }
    return render(request, 'accounts/register.html', context=context)


def profile(request):
    return render(request, 'accounts/profile.html')


def change_profile(request):
    profile = Profile.objects.filter(user=request.user)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

        if profile:
            profile = ProfileChangeForm(request.POST, request.FILES, instance=request.user.profile)
        else:
            profile = ProfileChangeForm(request.POST, request.FILES)

        if profile.is_valid():
            profile = profile.save(commit=False)
            profile.user = request.user
            profile.save()

        return redirect('accounts:profile')

    else:
        form = CustomUserChangeForm(instance=request.user)
        if profile:
            profile = ProfileChangeForm(instance=request.user.profile)
        else:
            profile = ProfileChangeForm()

    context = {
        "form": form,
        "profile": profile
    }
    return render(request, 'accounts/profile_change.html', context=context)
