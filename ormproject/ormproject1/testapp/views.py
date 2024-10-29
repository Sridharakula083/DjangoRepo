from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q

# Create your views here.
def retrive_view(request):
    #emp_list = Employee.objects.all()
    #emp_list = Employee.objects.filter(ename__iexact='Dan Kline')
    #emp_list = Employee.objects.filter(ename__contains='Da')
    #emp_list = Employee.objects.filter(id__in=[1,3,5,7,9])
    #emp_list = Employee.objects.filter(esal__gte=15000)
    #emp_list = Employee.objects.filter(esal__lt=15000)
    #emp_list = Employee.objects.filter(esal__lte=15000)
    #emp_list = Employee.objects.filter(ename__startswith='D')
    #emp_list = Employee.objects.filter(ename__endswith='e')
    #emp_list = Employee.objects.filter(esal__range=[12000,15000])
    #emp_list = Employee.objects.filter(ename__startswith='D') | Employee.objects.filter(esal__lt=15000)
    #emp_list = Employee.objects.filter(ename__startswith='D') & Employee.objects.filter(esal__lt=15000)
    #emp_list = Employee.objects.filter(Q(ename__startswith='D') & Q(esal__gte=15000))
    #emp_list = Employee.objects.exclude(ename__startswith='D')
    emp_list = Employee.objects.filter(~Q(ename__startswith='s'))
    return render(request,'testapp/index.html',{'emp_list':emp_list})
