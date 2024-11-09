from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from Psychometric.models import psychometric_question
from User.models import User_Details, Feedback


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
                return redirect('users_list')
            else:
                return render(request, 'Admin/main/sign-in.html', {'msg' : 'Access denied! You are not authorised to enter this dashboard!'})
        else:
            return render(request, 'Admin/main/sign-in.html', {'msg' : 'Access denied! Maybe try using some magic words. Or double check your password!'})
    return render(request, 'Admin/main/sign-in.html')

def admin_logout(request):
    logout(request)
    return redirect(admin_login)

def psychometric_questions(request):
    page = "Psychometric Questions"
    questions = psychometric_question.objects.filter(question_status = True)
    return render(request, 'Admin/psychometric_test/psychometric_question.html', {'page' : page, 'questions' : questions})

def create_question(request):
    if request.method=="POST":
        question = request.POST.get('question')
        option_1 = request.POST.get('option_1')
        option_2 = request.POST.get('option_2')
        option_3 = request.POST.get('option_3')
        option_4 = request.POST.get('option_4')
        correct = request.POST.get('correct')
        if correct == 'option1':
            correct = 1
        elif correct == 'option2':
            correct = 2
        elif correct == 'option3':
            correct = 3
        elif correct == 'option4':
            correct = 4
        elif correct == 'any':
            correct = 5
        quest = psychometric_question.objects.create(question = question, choice_1 = option_1, choice_2 = option_2, choice_3 = option_3, choice_4 = option_4, correct_answer = correct, question_status = True)
        quest.save()
        return redirect(psychometric_questions)
        
    return render(request, 'Admin/psychometric_test/create_question.html')

def delete_question(request, qn_id):
    qn = psychometric_question.objects.get(id = qn_id)
    qn.question_status = False
    qn.save()
    return redirect(psychometric_questions)

def edit_question(request, qn_id):
    qn = psychometric_question.objects.get(id = qn_id)
    if request.method == "POST":
        qn.question = request.POST.get('question')
        qn.choice_1 = request.POST.get('option_1')
        qn.choice_2 = request.POST.get('option_2')
        qn.choice_3 = request.POST.get('option_3')
        qn.choice_4 = request.POST.get('option_4')
        correct_answers = request.POST.get('correct')
        print(correct_answers)
        if correct_answers == 'option1':
            qn.correct_answer = 1
            print(qn.choice_1)
        elif correct_answers == 'option2':
            qn.correct_answer = 2
            print(qn.choice_2)
        elif correct_answers == 'option3':
            qn.correct_answer = 3
            print(qn.choice_3)
        elif correct_answers == 'option4':
            qn.correct_answer = 4
            print(qn.choice_4)
        elif correct_answers == 'any':
            qn.correct_answer = 5
        qn.save()
        return redirect(psychometric_questions)
    return render(request, 'Admin/psychometric_test/edit_questions.html', {'qn' : qn})

def users_list(request):
    users = User.objects.filter(is_active = True    )
    return render(request,'Admin/Users/UserTable.html',{'users':users})

def delete_user(request, user_id):
    user = User.objects.get(id = user_id)
    user.is_active = False
    user.save()
    return redirect(users_list)

def edit_user (request,user_id):
    user = User.objects.get(id = user_id)
    if request.method == 'POST':
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.username = request.POST.get('username')
        user.email= request.POST.get('email')
        user.save()
        return redirect(users_list)
    return render(request, 'Admin/Users/edit_user.html', {'usr' : user})

def councellers(request):
    councellers = User_Details.objects.filter(user_type="counceller")
    print(councellers)
    return render(request, 'Admin/Counceller/Councellers_list.html', {'councellers' : councellers})

def trainers(request):
    users = User_Details.objects.filter(user_type='trainer')
    return render(request, 'Admin/trainer/trainer_list.html', {'users': users})

def delete_user(request, user_id):
    user = User_Details.objects.get(id = user_id)
    user.user.delete() 
    return redirect('trainers')  

def feedback_form(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'Admin/main/feedback.html', {'feedbacks': feedbacks}) 