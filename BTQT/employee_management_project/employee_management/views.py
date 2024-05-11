from django.shortcuts import render
from django.http import HttpResponse
from .models import OfficeEmployee, SalesEmployee

def list_employees(request):
    office_employees = OfficeEmployee.objects.all()
    sales_employees = SalesEmployee.objects.all()
    context = {
        'office_employees': office_employees,
        'sales_employees': sales_employees
    }
    return render(request, 'list_employees.html', context)

def update_salary(request, employee_id):
    try:
        office_employee = OfficeEmployee.objects.get(employee_id=employee_id)
        office_employee.monthly_salary = office_employee.calculate_salary()
        office_employee.save()
        return HttpResponse("Salary updated successfully for office employee.")
    except OfficeEmployee.DoesNotExist:
        try:
            sales_employee = SalesEmployee.objects.get(employee_id=employee_id)
            sales_employee.monthly_salary = sales_employee.calculate_salary()
            sales_employee.save()
            return HttpResponse("Salary updated successfully for sales employee.")
        except SalesEmployee.DoesNotExist:
            return HttpResponse("Employee not found.")

def find_employee_by_id(request, employee_id):
    try:
        office_employee = OfficeEmployee.objects.get(employee_id=employee_id)
        return HttpResponse(f"Office Employee found: {office_employee.full_name}")
    except OfficeEmployee.DoesNotExist:
        try:
            sales_employee = SalesEmployee.objects.get(employee_id=employee_id)
            return HttpResponse(f"Sales Employee found: {sales_employee.full_name}")
        except SalesEmployee.DoesNotExist:
            return HttpResponse("Employee not found.")

def find_lowest_salary(request):
    office_employees = OfficeEmployee.objects.order_by('monthly_salary')[:1]
    sales_employees = SalesEmployee.objects.order_by('monthly_salary')[:1]
    lowest_salary_employee = None
    if office_employees:
        lowest_salary_employee = office_employees[0]
    if sales_employees:
        if not lowest_salary_employee or sales_employees[0].monthly_salary < lowest_salary_employee.monthly_salary:
            lowest_salary_employee = sales_employees[0]
    if lowest_salary_employee:
        return HttpResponse(f"The employee with the lowest salary is: {lowest_salary_employee.full_name}")
    else:
        return HttpResponse("No employees found.")

def find_highest_sales_salary(request):
    sales_employees = SalesEmployee.objects.order_by('-monthly_salary')[:1]
    if sales_employees:
        return HttpResponse(f"The sales employee with the highest salary is: {sales_employees[0].full_name}")
    else:
        return HttpResponse("No sales employees found.")
