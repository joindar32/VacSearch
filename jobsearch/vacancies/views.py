from django.shortcuts import render
from .forms import VacancyFilterForm
from .models import Vacancy
import requests
from datetime import datetime, timedelta


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
            days_ago = datetime.now() - timedelta(days=form.cleaned_data.get('published_within_days'))
            params['date_from'] = days_ago.strftime('%Y-%m-%d')
        if form.cleaned_data.get('city_name'):
            city_response = requests.get('https://api.hh.ru/areas')
            print(f"City Response Status Code: {city_response.status_code}")
            if city_response.status_code == 200:
                city_data = city_response.json()
                print(f"City Data: {city_data}")
                for country in city_data:
                    for area in country.get('areas', []):
                        if area.get('name', '').lower() == form.cleaned_data.get('city_name').lower():
                            params['area'] = area.get('id', '')
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
        print(f"Vacancies API Response Status Code: {response.status_code}")

        if response.status_code == 200:
            vacancies_data = response.json().get('items', [])
            print(f"Vacancies Data: {vacancies_data}")
            for vacancy_data in vacancies_data:
                # Check if 'salary' information is available
                salary = vacancy_data.get('salary', None)
                salary_from = salary.get('from') if salary else None
                salary_to = salary.get('to') if salary else None

                # Save each vacancy to the database
                vacancy = Vacancy(
                    title=vacancy_data.get('name', ''),
                    company=vacancy_data.get('employer', {}).get('name', ''),
                    published_at=datetime.strptime(vacancy_data.get('published_at', ''), '%Y-%m-%dT%H:%M:%S%z'),
                    area=vacancy_data.get('area', {}).get('name', ''),
                    salary_from=salary_from,
                    salary_to=salary_to,
                    requirements=vacancy_data.get('snippet', {}).get('requirement', ''),
                    responsibilities=vacancy_data.get('snippet', {}).get('responsibility', ''),
                    experience='',
                    employment='',
                    schedule='',
                    description='',
                )
                vacancy.save()  # Save the vacancy object to the database
                vacancies.append(vacancy)

        else:
            print(f"Error fetching vacancies. Status code: {response.status_code}")

    return render(request, 'vacancies/search_vacancies.html', {'form': form, 'vacancies': vacancies})



def vacancy_detail(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    vacancy_description = vacancy.description.split('<li>')  # Split the description here
    return render(request, 'vacancies/detail.html', {'vacancy': vacancy, 'vacancy_description': vacancy_description})