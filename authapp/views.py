from django.http import Http404
from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import messages
from django.contrib import auth
from django.urls import reverse
from basket.models import Basket
from django.contrib.auth.decorators import login_required
from .models import User
from .utils import send_verify_email


def verify(request, user_id, hash):
    user = User.objects.get(pk=user_id)
    if user.activation_key == hash and not user.is_activation_key_expired():
        user.is_active = True
        user.activation_key = None
        user.save()
        auth.login(request, user)
        return HttpResponseRedirect(reverse('index'))
    raise Http404('')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            send_verify_email(user)
            messages.success(request, 'Для активации аккаунта подтвердите регистрацию по почте!')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required  # если не пользователь не авторизован, декоратор позвалет не заходить в контроллер
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:profile'))
    else:
        form = UserProfileForm(instance=request.user)
        # total_quantity = 0
        # total_sum = 0
        # baskets = Basket.objects.filter(user=request.user)
        # for basket in baskets:
        #     total_quantity += basket.quantity
        #     total_sum += basket.sum()

    context = {
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
        # 'total_quantity': sum(basket.quantity for basket in baskets),
        # 'total_sum': sum(basket.sum() for basket in baskets),
    }
    return render(request, 'authapp/profile.html', context)
