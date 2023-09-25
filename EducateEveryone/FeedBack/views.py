
from django.shortcuts import redirect, render
from django.http import *
from django.contrib import messages
from . import models

def feedback(request):

    if request.method == "POST":
        name=request.POST.get('name')
        class1=request.POST.get('class')
        academic_performance=request.POST.get('acadperf')
        attendance=request.POST.get('attend')
        study_habits=request.POST.get('studhabi')
        goals=request.POST.get('goals')
        disability=bool(request.POST.get('learn'))
        d_type=request.POST.get('disable')
        financial_concerns=request.POST.get('fincon')
        career_interest=request.POST.get('Career')
        future_plans=request.POST.get('plan')


        myuser=models.StudentDifficulty.objects.create(Name=name,
            Class=class1,
            Academic_Performance=academic_performance,
            Attendance=attendance,
            StudyHabits=study_habits,
            Goals=goals,
            Learning_Disabilities=disability,
            Disability_Type=d_type,
            Financial_Concerns=financial_concerns,
            Career_Interests=career_interest,
            Future_Plans=future_plans,
            )
        

        myuser.save()

        messages.success(request,"Your feedback was successfully recorded")

        return redirect('home')
    
    return render(request,"FeedBack/feedback.html")

