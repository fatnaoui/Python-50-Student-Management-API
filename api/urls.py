from django.urls import path
from api import views
urlpatterns = [
    path('students/',views.StudentAPI.as_view()),
    path('students/<int:pk>',views.StudentDAPI.as_view()),
    path('deletestudent/<int:pk>',views.StudentDeAPI.as_view())
]