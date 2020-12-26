from django.shortcuts import render, redirect
from django.views import View
from django.forms import formset_factory
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from .models import Product, Category, PurchaseDetail, PurchaseList
from .forms import ProductForm, CategoryForm, PurchaseDetailForm, PurchaseListForm
from django.db.models import Sum, Avg

def index(request):
    last_purch = PurchaseDetail.objects.all().order_by('detail_id')[:10]
    return render(request, 'index.html', {'last_purch': last_purch})

def add_category(request):
    if not request.user.is_authenticated:
            return HttpResponseForbidden()
    if request.method == 'POST':
        add = CategoryForm(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect('index')
        else:
            return HttpResponse('''invalid form''')
    else:
        categories = Category.objects.all()
        add = CategoryForm()
        return render(request, 'category.html', {'category_form': add, 'existing_categories': categories})

def add_product(request):
    if not request.user.is_authenticated:
            return HttpResponseForbidden()
    if request.method == 'POST':
        add = ProductForm(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect('index')
        else:
            return HttpResponse('''invalid form''')
    else:
        products = Product.objects.all()
        add = ProductForm()
        return render(request, 'product.html', {'product_form': add, 'existing_products': products})

def delete_category(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == "POST" and 'del_cat' in request.POST:
        cat_name = request.POST.getlist('cat_name')
        for i in cat_name:
            selected_object = Category.objects.get(category_name=i)
            selected_object.delete()
            return redirect('index')
    else:
        category = Category.objects.all()
        return render(request, 'delete_cat.html', {'existing_categories': category})

def delete_product(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == "POST" and 'del_prod' in request.POST:
        prod_name = request.POST.get('prod_name')
        selected_object = Product.objects.get(product_name=prod_name)
        selected_object.delete()
        return redirect('index')
    else:
        product = Product.objects.all()
        return render(request, 'delete_prod.html', {'existing_products': product})

def make_purchase(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    prod_count =  Product.objects.all().count()
    purch_form_fact = formset_factory(PurchaseDetailForm, extra=prod_count)
    if request.method =="POST" and 'make_purch' in request.POST:
        purch_date = request.POST.get('purch_date')
        purch_form = purch_form_fact(request.POST, request.FILES)
        if purch_form.is_valid():
            record = PurchaseList(purchase_date=purch_date)
            record.save()
            puch_id = PurchaseList.objects.order_by('purchase_id').last()
            for form in purch_form:
                if form.is_valid():
                    purch_prod = form.cleaned_data.get('product')
                    purch_cost = form.cleaned_data.get('product_cost')
                    detail_record = PurchaseDetail(purchase=puch_id, product=purch_prod, product_cost=purch_cost)
                    detail_record.save()
            return redirect('index')
        else:
            return HttpResponse('''invalid form''')
    else:
        return render(request, 'purchase.html', {'purchase_detail': purch_form_fact})

def delete_purchase(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    purch_detail = PurchaseDetail.objects.all()
    if request.method == "POST" and 'del_purch' in request.POST:
        purch_id = request.POST.get('purch_id')
        selected_object = PurchaseList.objects.get(purchase_id=purch_id)
        selected_object.delete()
        return redirect('index')
    else:
        return render(request, 'delete_purch.html', {'purch_det': purch_detail})

def date_filter(request):
    if not request.user.is_authenticated:
            return HttpResponseForbidden()
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if start_date is None :
            start_date = '2020-12-28'
            end_date = '2020-12-28'
        if start_date > end_date:
            return HttpResponse()
        filt_det = PurchaseDetail.objects.filter(purchase__purchase_date__range=[start_date, end_date])
        if 'view_all' in request.GET:
            filt_det = PurchaseDetail.objects.all()
        summ = filt_det.aggregate(total=Sum('product_cost'))
        context = {'filtered_date':filt_det, 'period_sum': summ, 'st_date': start_date, 'en_date': end_date}
        return render(request, 'date_filter.html', context)
    else:
        return HttpResponse()

def date_and_cat_filter(request):
    if not request.user.is_authenticated:
            return HttpResponseForbidden()
    categories = Category.objects.all()
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        category = request.GET.get('cat_name')
        if start_date is None :
            start_date = '2020-12-28'
            end_date = '2020-12-28'
        if start_date > end_date:
            return HttpResponse('''Invalid date range''')
        filt_det = PurchaseDetail.objects.filter(purchase__purchase_date__range=[start_date, end_date])
        cat_filt = filt_det.filter(product__category_name=category)
        summ = filt_det.aggregate(total=Sum('product_cost'))
        context = {'filtered_date':cat_filt, 'period_sum': summ, 'categories': categories, 'st_date': start_date, 'en_date': end_date}
        return render(request, 'date_cat_filter.html', context)
    else:
        return HttpResponse()

def date_and_prod_filter(request):
    if not request.user.is_authenticated:
            return HttpResponseForbidden()
    products = Product.objects.all()
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        prod = request.GET.get('prod_name')
        if start_date is None :
            start_date = '2020-12-28'
            end_date = '2020-12-28'
        if start_date > end_date:
            return HttpResponse('''Invalid date range''')
        filt_det = PurchaseDetail.objects.filter(purchase__purchase_date__range=[start_date, end_date])
        prod_filt = filt_det.filter(product__product_name=prod)
        summ = prod_filt.aggregate(total=Sum('product_cost'))
        av = prod_filt.aggregate(aver = Avg('product_cost'))
        context = {'filtered_date':prod_filt, 'period_sum': summ, 'products': products, 'average_cost': av, 'st_date': start_date, 'en_date': end_date}
        return render(request, 'date_prod_filter.html', context)
    else:
        return HttpResponse()

