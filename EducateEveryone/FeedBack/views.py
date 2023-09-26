
from django.shortcuts import redirect, render
from django.http import *
from django.contrib import messages
from . import models
from matplotlib import pyplot as plt
from io import BytesIO
import base64

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



def generate_graph(request):
    data = models.StudentDifficulty.objects.all()

    # Extract values for Academic_Performance and Attendance
    academic_performance = [entry.Academic_Performance for entry in data]
    attendance = [entry.Attendance for entry in data]

    # Create a scatter plot
    plt.scatter(academic_performance, attendance)
    plt.xlabel('Academic Performance')
    plt.ylabel('Attendance')
    plt.title('Academic Performance vs. Attendance')

    # Save the plot to a memory buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Convert the buffer content to base64
    graph_data = base64.b64encode(buffer.read()).decode()

    # Embed the base64 image data in an HTML response
    html_response = f'<img src="data:image/png;base64,{graph_data}" alt="Graph">'

    return HttpResponse(html_response)

