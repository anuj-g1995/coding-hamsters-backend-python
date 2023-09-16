from rest_framework import serializers
from .models import Job, JobApplyModel


class JobApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplyModel
        fields = '__all__'


# class JobAllSerializer(serializers.ModelSerializer):
#     b = JobApplySerializer()
#
#     class Meta:
#         model = Job
#         fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
