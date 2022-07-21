from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from .models import user
from .models import Employer

class userSerializers(serializers.ModelSerializer):

    class Meta:
        model = user
        fields=('firstname', 'lastname')
        # fields = '__all__'

class employerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields= '__all__'       
class userEmployeeJoin(serializers.ModelSerializer): 
    userId=userSerializers()
    class Meta:
        model= Employer
        fields = '__all__'

