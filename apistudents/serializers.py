from rest_framework import serializers
from students.models import *


class Studentserializer( serializers.ModelSerializer ):
    class Meta:
        model = Students
        fields = "__all__"