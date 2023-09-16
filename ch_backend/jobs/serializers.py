from rest_framework import serializers
from .models import Job, JobApplyModel


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplyModel
        fields = '__all__'
