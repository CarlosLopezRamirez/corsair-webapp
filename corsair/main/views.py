from django.shortcuts import render

# Create your views here.

def edit_profile(request):
    return render(request, 'main/edit-profile.html')

def directory(request):
    return render(request, 'main/directory.html')