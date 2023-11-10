from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
                return redirect("login")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
        return redirect("register")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


# Added below function because of the firefox problem auto add slash after url and ends with 404
def login_redirect(request):
    return redirect("login")


def register_redirect(request):
    return redirect("register")
