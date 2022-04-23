from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """ Displays the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)    

    return render(request, 'profiles/profile.html', {
        'profile': profile
    })