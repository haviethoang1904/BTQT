from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=100)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.full_name

class OfficeEmployee(Employee):
    days_worked = models.IntegerField()

    def calculate_salary(self):
        base_salary = self.basic_salary
        total_salary = base_salary + (self.days_worked * 180000)
        if total_salary > 8000000:
            total_salary *= 1.05
        return total_salary

class SalesEmployee(Employee):
    products_sold = models.IntegerField()

    def calculate_salary(self):
        base_salary = self.basic_salary
        total_salary = base_salary + (self.products_sold * 120000)
        if total_salary < 5000000:
            total_salary *= 1.3
        if self.products_sold > 40:
            total_salary *= 1.3
        return total_salary
