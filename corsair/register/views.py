from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def register(request):

    if request.method == "GET":
        return render(request, 'register/register.html')

    elif request.method == "POST":

        csrf_token = request.POST['csrfmiddlewaretoken']
        email = request.POST['email']
        password = request.POST['password']
        return HttpResponseRedirect("/directory/")


def confirmEmail(request, token):
    return render(request, 'register/confirm-email.html')


def resendEmail(request):
    return render(request, 'register/resend-email.html')
