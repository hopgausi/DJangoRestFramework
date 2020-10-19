from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.programmers import views



urlpatterns = [
    path('all/', views.ProgrammersCompanyLanguageList.as_view()),
    path('programmers/all/', views.ProgrammersList.as_view()),
    path('programmers/<int:pk>/', views.ProgrammerDetail.as_view()),
     path('companies/all/', views.CompanyList.as_view()),
    path('companies/<int:pk>/', views.CompanyDetail.as_view()),
    path('languagies/all/', views.LanguageList.as_view()),
    path('languagies/<int:pk>/', views.LanguageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)