from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.list_employees, name='list_employees'),
    path('update_salary/<str:employee_id>/', views.update_salary, name='update_salary'),
    path('find_employee/<str:employee_id>/', views.find_employee_by_id, name='find_employee'),
    path('lowest_salary/', views.find_lowest_salary, name='lowest_salary'),
    path('highest_sales_salary/', views.find_highest_sales_salary, name='highest_sales_salary'),
]
