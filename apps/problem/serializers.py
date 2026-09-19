from rest_framework import serializers
from apps.user.serializers import UserSerializer
from .models import Problem

class ProblemSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Problem
        fields = "__all__"