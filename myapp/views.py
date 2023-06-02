from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm1
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import FileUploadForm




def home(request):
    return render(request, 'index.html')


def profiles(request):
    users = User.objects.all()
    return render(request, 'profiles.html', {'users': users})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect(reverse('admin:index'))
        else:
            error_message = 'Invalid login credentials for admin'
    else:
        error_message = ''
    return render(request, 'admin_login.html', {'error_message': error_message})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')
    

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        while not form.is_valid():
            form = SignUpForm(request.POST)
            return render(request, 'signup.html', {'error_message': 'Invalid entries'})
        else:
            user = form.save(commit=False)
            user.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def calculator(request):
    if request.method == 'POST':
        # Retrieve the numbers from the POST request
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))

        result = num1 + num2
        return render(request, 'calculator.html', {'result': result})
    
    else:
        # Render the form template for entering the numbers
        return render(request, 'calculator.html')
    

def quadratic_eq(request):
    if request.method == 'POST':
        coeff1 = float(request.POST.get('coeff1'))
        coeff2 = float(request.POST.get('coeff2'))
        bias   = float(request.POST.get('bias'))

        if coeff1==0:
            return render(request, 'quadratic.html', {'final_result': "Sorry (coeff1) can't be 0, try another equation."})

        delta = coeff2**2 - (4*coeff1*bias)
        if delta<0:
            return render(request, 'quadratic.html', {'result_error': 'sorry delta is less than 0, try another equation.'})
        else:
            x1 = (-coeff2 + (delta**(1/2))) / (2*coeff1)
            x2 = (-coeff2 - (delta**(1/2))) / (2*coeff1)
            return render(request, 'quadratic.html', {'final_result': [x1, x2]})
    else:
        return render(request, 'quadratic.html')


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            save_file(uploaded_file.read(), uploaded_file.name)
            # Perform further processing or save the file
            if uploaded_file: bool = True

            return render(request, 'upload_file.html', {'bool': bool})
    else:
        form = FileUploadForm()
    return render(request, 'upload_file.html', {'form': form})


def save_file(content, filename):
    with open('media/'+filename, 'wb') as file:
        file.write(content)
    file.close()


def Num_Analysis(request):
    # return HttpResponse("Hello, world. You're at the NUM_ANALYSIS index.")
    return render(request, 'index_NA.html')


    




