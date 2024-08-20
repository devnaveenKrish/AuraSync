from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='admin_login')
def admin_index(request):
    return render(request, 'Admin/main/admin_index.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            if user.is_staff:
                login(request, user)
                return redirect(admin_index)
            else:
                return render(request, 'Admin/main/sign-in.html', {'msg' : 'Access denied! You are not authorised to enter this dashboard!'})
        else:
            return render(request, 'Admin/main/sign-in.html', {'msg' : 'Access denied! Maybe try using some magic words. Or double check your password!'})
    return render(request, 'Admin/main/sign-in.html')

def admin_logout(request):
    logout(request)
    return redirect(admin_login)