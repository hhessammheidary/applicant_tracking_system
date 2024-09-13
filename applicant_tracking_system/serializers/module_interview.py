from rest_framework import serializers
from applicant_tracking_system.models import Interview


class InterviewSerializer(serializers.ModelSerializer):
    interviewer = serializers.SerializerMethodField()

    def get_interviewer(self, instance):
        return instance.interviewer.username

    class Meta:
        model = Interview
        fields = (
            'id',
            'interviewer',
            'date',
            'type',
        )
