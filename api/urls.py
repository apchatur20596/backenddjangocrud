from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('createEmp/', views.newEmployee, name="createEmp"),
    path('readAllEmp/',views.readAllEmp, name="readAllEmp"),
    path('readEmp/<str:pk>', views.readEmployee, name="readEmp"),

]