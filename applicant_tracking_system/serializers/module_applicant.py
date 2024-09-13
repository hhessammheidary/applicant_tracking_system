from rest_framework import serializers
from applicant_tracking_system.models import Applicant


class ApplicantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Applicant
        fields = (
            'id',
            'name',
            'cv',
            'linkedin',
            'age',
            'gender',
            'status'
        )
