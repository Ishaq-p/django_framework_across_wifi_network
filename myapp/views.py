from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import SignUpForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import FileUploadForm
from .forms import ParagraphForm
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import torch 
import timm
from PIL import Image
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform
import os
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from gtts import gTTS



chatbot_chat = []

def chatbot_history_set_zero(request):
    if request.method == 'POST':
        chatbot_chat.clear()
    return render(request, 'AIbot.html', {'chatbot_chat': chatbot_chat})


def home(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'index.html', context)


def profiles(request):
    users = User.objects.all()
    return render(request, 'profiles.html', {'users': users})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user': user})

def animations(request):
    return render(request, 'animations.html')

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


def logout_view(request):
    logout(request)
    return redirect('home')


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

            final_pred = classification_model(uploaded_file.name)
            # classification_model(img_path=os.path.join(os.getcwd(), 'media/'+uploaded_file.name))

            return render(request, 'upload_file.html', {'bool': bool, 'uploaded_file_url': uploaded_file.name, 'pwd': os.getcwd(), 'final_pred': final_pred})
    else:
        form = FileUploadForm()
    return render(request, 'upload_file.html', {'form': form})


def model_categories_read(model=True):
    if model:
        model = timm.create_model('tf_efficientnet_b0', checkpoint_path=os.path.join(os.getcwd(), 'tf_efficientnet_b0_aa-827b6e33.pth'))
        return model
    else:
        with open(os.path.join(os.getcwd(), 'imagenet_classes.txt'), "r") as f:
            categories = [s.strip() for s in f.readlines()]
        return categories


def classification_model(img_path):
    img = Image.open(os.path.join('media',img_path)).convert('RGB')
    model = model_categories_read(model=True)
    categories = model_categories_read(model=False)
    model.eval()

    config = resolve_data_config({}, model=model)
    transform = create_transform(**config)
    tensor = transform(img).unsqueeze(0)
    
    with torch.no_grad():
        out = model(tensor)
    probabilities = torch.nn.functional.softmax(out[0], dim=0)
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    final_pred=[]
    for i in range(top5_prob.size(0)):
        final_pred.append((categories[top5_catid[i]], round(top5_prob[i].item(), 3)))
    return final_pred



def save_file(content, filename):
    with open('media/'+filename, 'wb') as file:
        file.write(content)
    file.close()



def Num_Analysis(request):
    # return HttpResponse("Hello, world. You're at the NUM_ANALYSIS index.")
    return render(request, 'index_NA.html')

def text2voice(request):
    if request.method == 'POST':
        form = ParagraphForm(request.POST)
        if form.is_valid():
            paragraph_text = form.cleaned_data['paragraph']
            text2voice_func(paragraph_text)
            # Do something with the paragraph_text, such as saving it to a database.
            return render(request, 'text2voice.html', {'result': paragraph_text})
    else:
        form = ParagraphForm()
    return render(request, 'text2voice.html', {'form': form})

def text2voice_func(message):
    tts = gTTS(text=message)
    audio_path = os.path.join("media/text2voice", "output.mp3")
    tts.save(audio_path)
    return audio_path



# Use Django's CSRF protection
@csrf_exempt
def chatbot(request):
    user_message = None
    rasa_response = None
    if request.method == 'POST':
        user_message = request.POST.get('query')
        rasa_response = send_message_to_rasa(user_message)
        chatbot_chat.append([user_message, rasa_response])

    return render(request, 'AIbot.html', {'user_message': user_message, 'rasa_response': rasa_response, 'chatbot_chat': chatbot_chat})

def send_message_to_rasa(message):
    rasa_url = 'http://0.0.0.0:5005/webhooks/rest/webhook'
    data = {"message": message}
    headers = {"Content-Type": "application/json"}
    response = requests.post(rasa_url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        rasa_response = response.json()
        if rasa_response:
            return rasa_response[0]['text']
        else:
            return 'Rasa response is empty'
    else:
        return f'Rasa Error: {response.status_code} - {response.text}'
    







