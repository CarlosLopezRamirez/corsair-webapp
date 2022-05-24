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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponse("Login Success")
        else:
            # Return an 'invalid login' error message.
            return render(request, 'accounts/login.html')
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
            # return error message: form.errors
            return render(request, 'accounts/invalid-register.html', {'errors':form.errors})
            #print("invalid")
    else:
        form = NewUserForm()
    return render(request, 'accounts/register.html', {'form': form})

#def invalid_form(request, error):
 #   return render(request, error)

def send_email(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    current_site = get_current_site(request)
    mail_subject = 'Activate your Corsair account.'
    message = render_to_string('accounts/acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
    })
    to_email = user.email
    email = EmailMessage(
            mail_subject, message, to=[to_email]
    )
    email.send()
    return render(request,'accounts/confirm-email.html', {'user_id':user_id})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        return redirect('accounts:login')
    else:
        return HttpResponse('Activation link is invalid!')