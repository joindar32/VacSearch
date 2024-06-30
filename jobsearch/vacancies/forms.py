from django import forms

class VacancyFilterForm(forms.Form):
    job_title = forms.CharField(label='Название должности', max_length=100, required=False)
    skills = forms.CharField(label='Навыки', max_length=100, required=False)
    work_format = forms.ChoiceField(label='Формат работы', choices=[('remote', 'Удаленная работа'), ('fullDay', 'Полный день')], required=False)
    published_within_days = forms.IntegerField(label='Опубликована за последние (дни)', required=False)
    city_name = forms.CharField(label='Город', max_length=100, required=False)
    vacancy_type = forms.ChoiceField(label='Тип вакансии', choices=[('open', 'Открытая'), ('closed', 'Закрытая')], required=False)
    with_salary = forms.BooleanField(label='Только с зарплатой', required=False)
    min_salary = forms.IntegerField(label='Минимальная зарплата', required=False)
    max_salary = forms.IntegerField(label='Максимальная зарплата', required=False)
