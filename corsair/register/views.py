from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'register/register.html')

def confirmEmail(request, token):
    return render(request, 'register/confirm-email.html')

def resendEmail(request):
    return render(request, 'register/resend-email.html')