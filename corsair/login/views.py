from django.shortcuts import render

def login(request):
    # IMPLEMENT
    return render(request, 'login/login.html')

def resetPassword(request):
    # IMPLEMENT
    return render(request, 'login/reset-pw.html')

def changePassword(request, token):
    # IMPLEMENT
    return render(request, 'login/change-pw.html')
