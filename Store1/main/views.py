from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def index(request):
    prod = Product.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Main page of site', 'prod': prod})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'The form was wrong'


    form = ProductForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)