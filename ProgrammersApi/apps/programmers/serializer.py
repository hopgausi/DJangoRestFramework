from apps.programmers.models import Programmer, Language, Company
from rest_framework import serializers

class ProgrammerCompanyLanguageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Programmer
        fields = '__all__'
        depth = 1

class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        exclude = ['company','languages']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'