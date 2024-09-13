from django.urls import path
from . import views

urlpatterns = [
    path('Applicants/', views.ApplicantView.as_view({
        'get': 'list',
    })),
    path('Applicants/<int:pk>', views.ApplicantView.as_view({
        'get': 'retrieve',
    })),
    path('Interviews/', views.InterviewView.as_view({
        'get': 'list',
    })),
    path('Feedbacks/', views.FeedBackView.as_view({
        'get': 'list',
        'post': 'create',
    })),


]
