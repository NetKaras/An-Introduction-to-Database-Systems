from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django_tables2 import RequestConfig
from .models import RecordModel
from .forms import RecordForm
from .tables import RecordTable
from django.db import connection

def index(request):
    return render(request, 'index.html')
  

def table(request):
    if not request.user.is_authenticated:
            return HttpResponseForbidden()
    table = RecordTable(RecordModel.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'table.html', {'table':table})

def upload(request):
    if not request.user.is_authenticated:
            return HttpResponseForbidden()
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
    if not request.user.is_authenticated:
            return HttpResponseForbidden()
    if request.method == "POST":
        pks = request.POST.getlist('check')
    for i in pks:
        i = str(i)
        selected_objects = RecordModel.objects.get(date=i)
        selected_objects.delete()
    return redirect('table')
