from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    published_at = models.DateTimeField()
    area = models.CharField(max_length=255)
    salary_from = models.IntegerField(null=True, blank=True)
    salary_to = models.IntegerField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    responsibilities = models.TextField(null=True, blank=True)
    experience = models.CharField(max_length=255)
    employment = models.CharField(max_length=255)
    schedule = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
