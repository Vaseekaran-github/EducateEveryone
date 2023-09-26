from django.urls import path

from . import views

urlpatterns = [
    path('feedback/',views.feedback, name='feedback'),
    path('generate_graph/', views.generate_graph, name='generate_graph'),
    # Other URL patterns
]
