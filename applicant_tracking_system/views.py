from django.http import HttpResponse
from .models import Applicant, Feedback, Interview, TelegramBot
from .serializers import FeedbackSerializer, InterviewSerializer, ApplicantSerializer
from django.shortcuts import render
from rest_framework import viewsets, authentication, permissions


def index(request):
    return HttpResponse("HI")


class ApplicantView(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer


class InterviewView(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(interviewer=self.request.user)
        return query_set


class FeedBackView(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

