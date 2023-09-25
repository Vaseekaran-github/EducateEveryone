

# Create your models here.

from django.db import models

class StudentDifficulty(models.Model):
    Name = models.CharField(max_length=100) 
    Class= models.IntegerField()
    Academic_Performance = models.CharField(max_length=100)  # For academic grades, e.g., 'B+', 'A', etc.
    Attendance = models.IntegerField()  # To store attendance percentage as an integer, e.g., 85
    StudyHabits = models.TextField()  # For longer descriptions of study habits
    Goals = models.TextField()  # For longer descriptions of educational and career goals
    Learning_Disabilities = models.BooleanField(default=False)  # Boolean field for learning disabilities
    Disability_Type = models.CharField(max_length=100, blank=True)  # Short description, e.g., 'Dyslexia'
    Financial_Concerns = models.CharField(max_length=100)  # Short description, e.g., 'Tuition fees'
    Career_Interests = models.TextField()  # For longer descriptions of career interests
    Future_Plans = models.TextField()  # For longer descriptions of future plans

    

