from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import*
from .forms import CompanyForm, CreateUserForm
from .filters import CompaniesFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def registerPage(request):
   
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user =form.cleaned_data.get('username')
                messages.success(request, 'kulanıcı oluşturuldu')
                return redirect('login')

        context = {'form':form}

        return render(request,'companies/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Kulanıcu adı veya şifre yanlış')

           
        context = {}
        return render(request,'companies/login.html',context)
   
    

def logoutUser(request):
    logout(request)
   
    return redirect('login')

    
@login_required(login_url='login')
def home(request):
   companies = Companies.objects.all()
   myFilter = CompaniesFilter(request.GET, queryset=companies)
   companies = myFilter.qs

    
   context = {'companies':companies,'myFilter':myFilter}

   return render(request,'companies/companies.html',context)

@login_required(login_url='login')
def companies(request):
    companies = Companies.objects.all()
    myFilter = CompaniesFilter(request.GET, queryset=companies)
    companies = myFilter.qs

    
    context = {'companies':companies,'myFilter':myFilter}

    return render(request,'companies/companies.html',context)

@login_required(login_url='login')
def added_companies(request):
    return render(request,'companies/added_companies.html')

@login_required(login_url='login')
def user(request, pk_test):

    user = User.objects.get(id=pk_test)
    context = {'user':user}
    return render(request,'companies/user.html',context)

@login_required(login_url='login')
def add_companies(request):

    form = CompanyForm()
    if request.method == 'POST':
       # print('priting POST:',request.POST)
       form = CompanyForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('/')

    context ={'form': form}
    return render(request,'companies/add_companies.html', context)

@login_required(login_url='login')
def update_companies(request, pk):
    companies= Companies.objects.get(id=pk)
    form = CompanyForm(instance=companies)
    if request.method == 'POST':
       # print('priting POST:',request.POST)
       form = CompanyForm(request.POST, instance=companies)
       if form.is_valid():
           form.save()
           return redirect('/')


    context ={'form': form}
    return render(request,'companies/update_companies.html', context)

@login_required(login_url='login')
def delete_companies(request, pk):
    companies= Companies.objects.get(id=pk)
    if request.method == 'POST':
        companies.delete()
        return redirect('/')
    context ={'item':companies}
    return render(request,'companies/delete_companies.html', context)


