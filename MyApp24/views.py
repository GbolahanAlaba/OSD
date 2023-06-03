from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Sum
from .forms import *
from .models import *


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.info(request, 'Invalid Login')
            return redirect("login")            
        else:
            auth.login(request, user)
            return redirect('dashboard')
    else:
        return render(request,"login.html")  

  

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username=username):
                messages.info(request, 'Username Exists')
                return render(request, "register.html")
            
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
                user.save();
                return redirect("login")

        else:
            messages.info(request, 'Password not matching')
            return render(request, "register.html")
    
    else:
        return render(request,"register.html")
    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     Repassword = request.POST['repassword']

    #     obj = Sign_Up()
    #     obj.First_Name = first_name
    #     obj.Last_Name = last_name
    #     obj.Username = username
    #     obj.Password = password
    #     obj.save()

    #     return redirect("login")

    # return render(request, 'register.html')

# Homepage
def homepage(request):
    return render(request, 'index.html')
# Dashboard
def dashboard(request):
    return render(request, 'dashboard.html')

# Inventory Links
def warehouse(request):
    return render(request, 'inventory/warehouse.html')
def mainstore(request):
    return render(request, 'inventory/mainstore.html')
def branch(request):
    return render(request, 'inventory/branch.html')
def purchase_return(request):
    return render(request, 'inventory/purchase_return.html')

def products_entry(request):
    if request.POST:
        form = INVForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('products_entry')

    return render(request, 'inventory/products_entry.html', {'form': INVForm})

# def products_entry(request):
#     if request.method == 'POST':
#         form = Sample(request.POST)
#         if form.is_valid():
            
#             obj = Samp()
#             obj.Product = form.cleaned_data['Product']
#             obj.Vendor = form.cleaned_data['Vendor']
#             obj.save()
#         return redirect('products_entry')

#     return render(request, 'inventory/products_entry.html', {'form': Sample})



# Transactions Links
def sales(request):
    return render(request, 'transactions/sales.html')

# Testing
