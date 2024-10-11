from django.shortcuts import render, redirect, HttpResponse
from django.http import StreamingHttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import os
from deepface import DeepFace
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
from PIL import Image
import base64
import io
from .models import Emotion_analysis


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
    return redirect(index)

def singup(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                msg = "Username already exists. Please try another one!"
                return render(request, 'User/auth/singup.html', {'msg' : msg})
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
import base64
from django.http import JsonResponse
from deepface import DeepFace
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import cv2

def decode_base64_image(base64_image):
    # Check for the base64 prefix and strip it if present
    if base64_image.startswith('data:image/png;base64,'):
        base64_image = base64_image.split(',')[1]
    img_data = base64.b64decode(base64_image)
    np_img = np.frombuffer(img_data, np.uint8)  # Use frombuffer instead of fromstring
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    return img

@csrf_exempt
def detect_facial_emotion(request):
    if request.method == 'POST':
        try:
            # Get the image from POST data
            image_data = request.POST.get('image')

            if not image_data:
                return JsonResponse({'error': 'No image data provided'}, status=400)

            # Decode the image
            img = decode_base64_image(image_data)

            # Use DeepFace to detect emotion
            result = DeepFace.analyze(img, actions=['emotion'])

            # Extract the dominant emotion
            emotion = result[0]['dominant_emotion']  # Updated to access the first result
            user = request.user
            emotion_label = emotion
            emotion_status = True
            emotion_data = Emotion_analysis.objects.create(user=user, emotion_label=emotion_label, emotion_status=emotion_status)
            emotion_data.save()
            

            # Return the emotion as JSON response
            return JsonResponse({'emotion': emotion})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


        

