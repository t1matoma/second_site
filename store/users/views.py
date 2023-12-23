from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import UserFrom, UserCreate, Profile
from product.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserFrom(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserFrom()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreate(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Поздравляем, вы успешно зарегистрировались")
            return HttpResponseRedirect(reverse('log'))
    else:
        form = UserCreate()
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = Profile(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('prof'))
        else:
            print(form.errors)
    else:
        form = Profile(instance=request.user)

    basket = Basket.objects.filter(user=request.user)
    total_sum = sum(i.sum() for i in basket)
    total_quantity = sum(i.quantity for i in basket)
    context = {
        'form': form,
        'basket': basket,
        'total_sum': total_sum,
        'total_quantity': total_quantity,
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))
