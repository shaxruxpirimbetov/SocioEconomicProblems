from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProblemListCreateAPIView.as_view()),
    path("<int:pk>/", views.ProblemDetailAPIView.as_view()),
]