from .models import Tasks
from rest_framework import serializers

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'completed', 'created_at','user']
        read_only_fields = ['user']