from django.urls import path
from .views import search_vacancies, vacancy_detail

urlpatterns = [
    path('', search_vacancies, name='search_vacancies'),
    path('vacancy/<str:vacancy_id>/', vacancy_detail, name='vacancy_detail'),
]
