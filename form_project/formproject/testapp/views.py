from django.shortcuts import render
from testapp.forms import StudentForm

# Create your views here.
def studentinput_form(request):
    submitted = False
    sname = ""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print("Form validation successful and print data")
            print("Name:",form.cleaned_data['name'])
            print("Rollno:",form.cleaned_data['rollno'])
            print("Marks:",form.cleaned_data['marks'])
            sname = form.cleaned_data['name']
            submitted = True
    form = StudentForm()
    my_dict = {'form':form,'submitted':submitted,'sname':sname}
    return render(request,'testapp/input.html',context=my_dict)
