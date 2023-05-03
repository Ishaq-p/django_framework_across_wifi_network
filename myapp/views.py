from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .forms import SignUpForm1
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User





def profiles(request):
    users = User.objects.all()
    return render(request, 'profiles.html', {'users': users})

def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})


def register(request):
    if request.method == 'POST':
        form = SignUpForm1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm1()
    return render(request, 'registration/register.html', {'form': form})




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
            return redirect('register')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')
    


# def signup_view(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             user.first_name = form.cleaned_data.get('first_name')
#             user.last_name = form.cleaned_data.get('last_name')
#             user.email = form.cleaned_data.get('email')
#             user.save()
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('register')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def game(request):
    return render(request, 'game.html')

def dynamic_display(request):
    return render(request, 'dynamic_display.html')

# def upload(request):
#     return render(request, 'upload.html')




# class FileUploadView(FormView):
#     template_name = 'file_sharing/upload.html'
#     form_class = FileForm

#     def form_valid(self, form):
#         form.save()
#         return redirect('files')

# class FileListView(ListView):
#     template_name = 'file_sharing/files.html'
#     model = File

# class FileDownloadView(DetailView):
#     model = File

#     def get(self, request, *args, **kwargs):
#         file = self.get_object()
#         file_path = file.file.path
#         with open(file_path, 'rb') as f:
#             response = HttpResponse(f.read())
#             response['Content-Type'] = 'application/octet-stream'
#             response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
#             return response


