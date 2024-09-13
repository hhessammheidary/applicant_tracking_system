from django.contrib import admin
from .models import Applicant, Interview, Feedback


class ApplicantTable(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender', 'status')


class InterviewTable(admin.ModelAdmin):
    list_display = ('id', 'interviewer', 'date', 'type')


class FeedbackTable(admin.ModelAdmin):
    list_display = ('id', 'user', 'interview', 'text')


admin.site.register(Applicant, ApplicantTable)
admin.site.register(Interview, InterviewTable)
admin.site.register(Feedback, FeedbackTable)
