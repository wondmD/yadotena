from django.shortcuts import render, redirect
from .models import Product, Sell, Expense
import datetime
from .forms import ProductForm, SellForm, ExpenseForm
#import django user model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#import methos to login user
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy



#home page that shows todays expence and sell and link to sell and expence adding page
@login_required(login_url=reverse_lazy('login'))
def home(request):
    today_expenses = Expense.objects.filter(date__date=datetime.date.today())
    total_expenses = sum([expense.amount for expense in today_expenses])
    today_sells = Sell.objects.filter(date_sold__date=datetime.date.today())
    total_sells = sum([sell.Product.price * sell.quantity for sell in today_sells])
    last_week_expenses = Expense.objects.filter(date__gte=datetime.date.today() - datetime.timedelta(days=7))
    last_week_total_expenses = sum([expense.amount for expense in last_week_expenses])

    last_month_expenses = Expense.objects.filter(date__gte=datetime.date.today() - datetime.timedelta(days=30))
    last_month_total_expenses = sum([expense.amount for expense in last_month_expenses])

    last_year_expenses = Expense.objects.filter(date__gte=datetime.date.today() - datetime.timedelta(days=365))
    last_year_total_expenses = sum([expense.amount for expense in last_year_expenses])

    
    last_week_sells = Sell.objects.filter(date_sold__gte=datetime.date.today() - datetime.timedelta(days=7))
    last_week_sells_total = sum([sell.Product.price*sell.quantity for sell in last_week_sells])

    last_month_sells = Sell.objects.filter(date_sold__gte=datetime.date.today() - datetime.timedelta(days=30))
    last_month_sells_total = sum([sell.Product.price*sell.quantity for sell in last_month_sells])

    last_year_sells = Sell.objects.filter(date_sold__gte=datetime.date.today() - datetime.timedelta(days=365))
    last_year_sells_total = sum([sell.Product.price*sell.quantity for sell in last_year_sells])

    context = {
        'total_expenses': total_expenses,
        'total_sells': total_sells,
        'today_expenses': today_expenses,
        'today_sells': today_sells,
        'last_week_total_expenses': last_week_total_expenses,
        'last_month_total_expenses': last_month_total_expenses,
        'last_year_total_expenses': last_year_total_expenses,
        'last_week_sells_total': last_week_sells_total,
        'last_month_sells_total': last_month_sells_total,
        'last_year_sells_total': last_year_sells_total,
    }
    
    return render(request, 'index.html', context)




@login_required(login_url=reverse_lazy('login'))
def register_product(request):
    products = Product.objects.all()[::-1]
    if request.method == 'POST':
        #chech if product exists already
        if Product.objects.filter(name=request.POST['name']).exists():
            return render(request, 'product_form.html', {'error_message': 'Product already exists', 'product_form': ProductForm(), 'products': products})
        #save new product to database if not exists
    
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_add')
    else:
        form = ProductForm()
    
    return render(request, 'product_form.html', {'product_form': form, 'products': products})

@login_required(login_url=reverse_lazy('login'))
def register_sell(request):
    if request.method == 'POST':
        form = SellForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sell_form')
    else:
        form = SellForm()
    sells = Sell.objects.all()[::-1][:30]
    return render(request, 'sell_form.html', {'sell_form': form,'sells': sells})


@login_required(login_url=reverse_lazy('login'))
def register_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_add')
    else:
        form = ExpenseForm()
    expense = Expense.objects.all()[::-1][:30]
    return render(request, 'expense_form.html', {'expense_form': form, 'exps': expense})
@login_required(login_url=reverse_lazy('login'))
def tabels(request):
    products = Product.objects.all()[::-1]
    sells = Sell.objects.all()[::-1]
    expenses = Expense.objects.all()[::-1]
    return render(request, 'tables.html', {'products': products, 'sells': sells, 'expenses': expenses})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # check if user exists and password is correct
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')