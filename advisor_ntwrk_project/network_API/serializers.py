from rest_framework import serializers
from .models import Advisor
from rest_framework.validators import UniqueValidator



class AdvisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advisor
        fields = ('name', 'photo')

