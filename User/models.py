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
