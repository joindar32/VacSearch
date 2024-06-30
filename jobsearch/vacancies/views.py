from django.shortcuts import render
from .forms import VacancyFilterForm
from .models import Vacancy
import requests


def search_vacancies(request):
    form = VacancyFilterForm(request.GET or None)
    vacancies = []

    if form.is_valid():
        params = {}
        if form.cleaned_data.get('job_title'):
            params['text'] = form.cleaned_data.get('job_title')
        if form.cleaned_data.get('skills'):
            params['text'] = form.cleaned_data.get('skills')
        if form.cleaned_data.get('work_format'):
            params['schedule'] = form.cleaned_data.get('work_format')
        if form.cleaned_data.get('published_within_days'):
            from datetime import datetime, timedelta
            days_ago = datetime.now() - timedelta(days=form.cleaned_data.get('published_within_days'))
            params['date_from'] = days_ago.strftime('%Y-%m-%d')
        if form.cleaned_data.get('city_name'):
            city_response = requests.get('https://api.hh.ru/areas').json()
            for country in city_response:
                for area in country['areas']:
                    if area['name'].lower() == form.cleaned_data.get('city_name').lower():
                        params['area'] = area['id']
                        break
        if form.cleaned_data.get('vacancy_type'):
            params['type'] = form.cleaned_data.get('vacancy_type')
        if form.cleaned_data.get('with_salary'):
            params['only_with_salary'] = 'true'
        if form.cleaned_data.get('min_salary'):
            params['salary_from'] = form.cleaned_data.get('min_salary')
        if form.cleaned_data.get('max_salary'):
            params['salary_to'] = form.cleaned_data.get('max_salary')

        response = requests.get('https://api.hh.ru/vacancies', params=params)

        if response.status_code == 200:
            vacancies = response.json().get('items', [])

    return render(request, 'vacancies/search_vacancies.html', {'form': form, 'vacancies': vacancies})


def vacancy_detail(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    vacancy_description = vacancy.description.split('<li>')  # Split the description here
    return render(request, 'vacancies/detail.html', {'vacancy': vacancy, 'vacancy_description': vacancy_description})