from rest_framework import serializers
from .models import Task


#  serializing the Task model
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['custom_id', 'title', 'due_date', 'completed', 'description']
