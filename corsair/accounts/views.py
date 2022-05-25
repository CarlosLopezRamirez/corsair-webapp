from distutils.log import error
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import NewUserForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def home(request):
    return HttpResponse("This is the homepage")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:directory') # TODO: pass user object with login
        else:
            return render(request, 'accounts/login.html', {'error':'invalid username or password'})
    else:
        return render(request, 'accounts/login.html')

def reset_pw(request):
    return render(request, 'accounts/reset-pw.html')

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.getUser()
            user.is_active = False
            user.save()
            return redirect('accounts:send_email', user_id=user.id) 
        else:
            return render(request, 'accounts/invalid-register.html', {'errors':form.errors})

    else:
        form = NewUserForm()
    return render(request, 'accounts/register.html', {'form': form})

def send_email(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    current_site = get_current_site(request)
    mail_subject = 'Activate your Corsair account.'
    message = render_to_string('accounts/acc-active-email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
    })
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
    return render(request, 'accounts/confirm-email.html', {'user_id':user_id})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        print(user)
        # return redirect('home')
        return redirect('main:edit-profile') # TODO: pass user object with registration
    else:
        return HttpResponse('Activation link is invalid!')
