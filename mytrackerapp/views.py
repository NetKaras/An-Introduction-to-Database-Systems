from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_tables2 import RequestConfig
from .models import RecordModel
from .forms import RecordForm
from .tables import RecordTable

def table(request):
    table = RecordTable(RecordModel.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'table.html', {'table':table})

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
'''
def update_record(request, record_id):
    record_id = int(record_id)
    try:
        record_sel = RecordModel.objects.get(id = record_id)
    except RecordModel.DoesNotExist:
        return redirect('table')
    record_form = RecordForm(request.POST or None, instance = record_sel)
    if record_form.is_valid():
       record_form.save()
       return redirect('table')
    return render(request, 'upload_form.html', {'upload_form':record_form})
'''
def delete_record(request):
    if request.method == "POST":
        pks = request.POST.getlist('check')
    for i in pks:
        i = str(i)
        selected_objects = RecordModel.objects.get(date=i)
        selected_objects.delete()
    return redirect('table')
