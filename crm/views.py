from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record


# Homepage
def home(request):
    return render(request, "crm/home.html")


# Register
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {"form": form}
    return render(request, "crm/register.html", context=context)


# Login
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user != None:
                auth.login(request, user)
                return redirect("record_db")
    context = {"form": form}
    return render(request, "crm/login.html", context=context)


# user table
@login_required(login_url="login")
def record_db(request):
    records = Record.objects.all()
    context = {"records": records}
    return render(request, "crm/record_db.html", context=context)


# Creat a record
@login_required(login_url="login")
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("record_db")
    context = {"form": form}
    return render(request, "crm/create_record.html", context=context)


# Update a recored
@login_required(login_url="login")
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("record_db")
    context = {"form": form}
    return render(request, "crm/update_record.html", context=context)


# Read a record
@login_required(login_url="login")
def singel_record(request, pk):
    all_records = Record.objects.get(id=pk)
    context = {"record": all_records}
    return render(request, "crm/view_record.html", context=context)


# Delete a record
@login_required(login_url="login")
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    return redirect("record_db")


# Logout
def logout(request):
    auth.logout(request)
    return redirect("login")
