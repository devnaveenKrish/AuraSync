from django.db import models
from django.contrib.auth.models import User

	# 1.	Angry
	# 2.	Disgust
	# 3.	Fear
	# 4.	Happy
	# 5.	Sad
	# 6.	Surprise
	# 7.	Neutral

class Emotion_analysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emotion_label = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True) 
    emotion_status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    
    
class User_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length = 10)
    address = models.CharField(max_length=225)
    gender = models.CharField(max_length=255)
    dob = models.DateField(null=True)
    age = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)
    trainer = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username


    





