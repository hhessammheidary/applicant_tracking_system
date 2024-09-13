from rest_framework import serializers
from applicant_tracking_system.models import Feedback, Interview


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = (
            'user',
            'interview',
            'text',
        )

    def save(self, **kwargs):
        user = self.context['request'].user
        feedback = super().save(user=user)
        return feedback
