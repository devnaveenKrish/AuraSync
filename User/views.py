from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Count
from django.http import StreamingHttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import os
from django.utils import timezone
from deepface import DeepFace
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
from PIL import Image
import base64
import io
from .models import Emotion_analysis, User_Details, Feedback
from django.contrib.auth.decorators import login_required


def index(request):
    user_details = None  # Define a default value for user_details
    if request.user.is_authenticated:
        user = request.user
        user_details = User_Details.objects.filter(user=user).first()

    if request.method == "POST":

        email = request.POST.get('EMAIL')
        message = request.POST.get('message')
        msg = Feedback.objects.create(email = email, feedback_text=message)
        msg.save()
        return render(request, 'User/index.html', {'user_details': user_details})

    return render(request, 'User/index.html', {'user_details': user_details})
def trainer_dashboard(request):
    trainer = request.user.id
    users = User_Details.objects.filter(trainer=trainer)
    print(users)
    return render(request,'Trainer/main/UserTable.html', {'users': users})

# def user_login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_active:
#             login(request, user)
#             return redirect(index)
#         elif User_Details.user_type == 'user':
#             login(request, user)
#             return redirect(index)  
#         else:
#             print(username, password)
#             return render(request, 'User/auth/login.html', {'msg':'Oops! Our emotion detection model senses a bit of frustration. It seems the password got scrambled in your neurons. Give it another go!😉'})
#     return render(request, 'User/auth/login.html')
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_active:
            user_details = User_Details.objects.filter(user=user).first()
            
            if user_details:
                if user_details.user_type == 'user':
                    login(request, user)
                    return redirect(index)  
                elif user_details.user_type == 'trainer':
                    login(request, user)
                    return redirect(trainer_dashboard)  
            else:
                return render(request, 'User/auth/login.html', {
                    'msg': 'User details are incomplete. Please contact support.'
                })
        else:
            # Failed authentication
           print(username, password)
           return render(request, 'User/auth/login.html', {'msg':'Oops! Our emotion detection model senses a bit of frustration. It seems the password got scrambled in your neurons. Give it another go!😉'})
    
    return render(request, 'User/auth/login.html')

def user_logout(request):
    logout(request)
    return redirect(index)

def detail(request): 
    print("Yes")
    return render(request,'User/auth/additional_Details.html')

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
            return redirect('detail')
        else:
            return render(request, 'User/auth/singup.html', {'msg' : 'Looks like your neurons are not communicating enough. Please check the password and try again!'})
    return render(request, 'User/auth/singup.html')

def detail(request): 
    if request.method == "POST":
        user = request.POST.get('username')
        phno = request.POST.get("phno")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        state = request.POST.get("state")
        role = request.POST.get("role")
        if User.objects.filter(username = user).exists():
            user_inst = User.objects.get(username = user)
            tbl_details = User_Details.objects.create(user = user_inst, phone_number = phno, address = address, gender = gender, age = age, state = state, user_type = role)
            tbl_details.save()
            return redirect('user_login')
        else:
            msg = "Haha! Found your deffective neuron! Check the Username and try again!"
            return render(request, 'User/auth/additional_Details.html', {'msg' : msg})
        
    return render(request,'User/auth/additional_Details.html')




def analysis(request):
    return render(request, 'User/analysis/analysis.html')

def Analysis_page(request, user_id):
    current_date = timezone.now().date()
    user = User.objects.filter(id = user_id).first()
    user_details = User_Details.objects.filter(user = user).first()
    emotion_counts = (
        Emotion_analysis.objects
        .filter(user=user, created_at__date = current_date)
        .values('emotion_label')
        .annotate(count=Count('emotion_label'))
        .order_by('-count')
    )
    print("Emotion_count : ",emotion_counts)
    all_emotions = Emotion_analysis.objects.filter(user = user).values('emotion_label').annotate(count=Count('emotion_label')).order_by('-count')
    print("All emotions : ",all_emotions)
    print("Emotion_count : ",emotion_counts)
    all_emotions = Emotion_analysis.objects.filter(user = user).values('emotion_label').annotate(count=Count('emotion_label')).order_by('-count')
    print("All emotions : ",all_emotions)
    total_emotion_count = Emotion_analysis.objects.filter(user=user, created_at__date = current_date).values('emotion_label').count()
    Highcharts_data = list(emotion_counts)
    return render(request, 'User/analysis/user_report.html', {'user' : user, 'user_details' : user_details, 'Highcharts_data': Highcharts_data, 'total_emotion_count': total_emotion_count, 'all_emotions' : all_emotions})

def trainer(request):
    trainers = User_Details.objects.filter(user_type="trainer")
    return render(request, 'User/trainer/trainer_list.html', {'trainers' : trainers})

def trainer_assign(request, trainer_id):
    user_id = request.user.id
    trainer = User_Details.objects.filter(id = trainer_id).first()
    user = User_Details.objects.filter(user = user_id).first()
    user.trainer = trainer.user.id
    user.save()
    return redirect('index')

def trainer_disallocate(request, user_id):
    users = User_Details.objects.filter(id = user_id).first()
    print(f'User id : {user_id} | user name : {users}')
    users.trainer = None
    users.save()
    return redirect('trainer_dashboard')


def councellor(request):
    councellors = User_Details.objects.filter(user_type='counceller')
    return render(request, 'User/councellor/councellor.html', {'councellors': councellors})



    return render(request, 'User/analysis/user_report.html', {'user' : user, 'user_details' : user_details, 'Highcharts_data': Highcharts_data, 'total_emotion_count': total_emotion_count, 'all_emotions' : all_emotions})


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import base64
from django.http import JsonResponse
from deepface import DeepFace
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import cv2
import os
from django.conf import settings
from PIL import Image
from io import BytesIO

def decode_base64_image(base64_image):
    # Check for the base64 prefix and strip it if present
    if base64_image.startswith('data:image/png;base64,'):
        base64_image = base64_image.split(',')[1]
    img_data = base64.b64decode(base64_image)
    np_img = np.frombuffer(img_data, np.uint8)  # Use frombuffer instead of fromstring
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    return img

def save_image(image, user_id, emotion):
    # Create the directory if it doesn't exist
    save_dir = os.path.join(settings.MEDIA_ROOT, 'captured_images')
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Generate the filename using user ID and detected emotion
    filename = f"{user_id}_{emotion}.png"
    save_path = os.path.join(save_dir, filename)

    # Save the image
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert to RGB for PIL
    image_pil.save(save_path)

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
            emotion = result[0]['dominant_emotion']  # Access the first result
            user = request.user  # Assuming the user is logged in
            emotion_label = emotion
            emotion_status = True

            # Save emotion to database (your existing functionality)
            emotion_data = Emotion_analysis.objects.create(user=user, emotion_label=emotion_label, emotion_status=emotion_status)
            emotion_data.save()

            # Save the image with emotion and user ID as filename
            save_image(img, user.id, emotion)  # Save image

            # Return the emotion as JSON response
            return JsonResponse({'emotion': emotion})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

        

