from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default='Come to me!')
    city = models.CharField(max_length=300)
    address = models.TextField(default='')
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default = 'Hello!')
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete = models.CASCADE, default=1)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.id
        }