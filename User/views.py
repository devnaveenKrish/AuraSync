from django.shortcuts import render, redirect, HttpResponse
from django.http import StreamingHttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def index(request):
    return render(request, 'User/index.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect(index)
        else:
            print("No")
            print(username, password)
            return render(request, 'User/auth/login.html', {'msg':'Oops! Our emotion detection model senses a bit of frustration. It seems the password got scrambled in your neurons. Give it another go!😉'})
    return render(request, 'User/auth/login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

def singup(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email)
            user.set_password(password)
            user.save()
        else:
            return render(request, 'User/auth/singup.html', {'msg' : 'Looks like your neurons are not communicating enough. Please check the password and try again!'})
    return render(request, 'User/auth/singup.html')

def analysis(request):
    return render(request, 'User/analysis/analysis.html')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# def capture_emotion(request):
#     cap = cv2.VideoCapture(0)  # Open the webcam
#     ret, frame = cap.read()  # Read a frame
#     # emotion = predict_emotion(frame)  # Run frame through your model
#     return JsonResponse({'emotion': emotion})