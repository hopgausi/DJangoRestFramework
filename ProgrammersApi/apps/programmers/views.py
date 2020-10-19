from rest_framework import generics
from apps.programmers.models import Programmer, Company, Language
from apps.programmers.serializer import (
    ProgrammerSerializer, CompanySerializer, LanguageSerializer, ProgrammerCompanyLanguageSerializer
    )


class ProgrammersCompanyLanguageList(generics.ListCreateAPIView):
    queryset = Programmer.objects.all()
    serializer_class =  ProgrammerCompanyLanguageSerializer
    
    
class ProgrammersList(generics.ListCreateAPIView):
    queryset = Programmer.objects.all()
    serializer_class =  ProgrammerSerializer

class ProgrammerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Programmer.objects.all()
    serializer_class =  ProgrammerSerializer

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class =  CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class =  CompanySerializer

class LanguageList(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class =  LanguageSerializer

class LanguageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class =  LanguageSerializer

