from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_tables2 import RequestConfig
from .models import RecordModel
from .forms import RecordForm
from .tables import RecordTable
from django.db import connection

def index(request):
    return render(request, 'index.html')
  

def table(request):
    table = RecordTable(RecordModel.objects.all())
    RequestConfig(request).configure(table)
    context = {'table':table if request.user.is_authenticated else table}
    return render(request, 'table.html', context)

def upload(request):
    upload = RecordForm()
    if request.method == 'POST':
        upload = RecordForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('table')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'table'}}">reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form': upload})

def delete_record(request):
    if request.method == "POST":
        pks = request.POST.getlist('check')
    for i in pks:
        i = str(i)
        selected_objects = RecordModel.objects.get(date=i)
        selected_objects.delete()
    return redirect('table')
