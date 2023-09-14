"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from myapp.views import *
from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', home, name='home'),
    path('admin_login/', admin_login, name='admin_login'),
    path('login/', login_view, name='login'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profiles/', profiles, name='profiles'),
    path('profiles/<str:username>/', profile, name='profile'),
    path('animations/', animations, name='animations'),
    path('main/', home, name='main'),
    path('calc/', calculator, name='calculator'),
    path('quadeq/', quadratic_eq, name='quad'),
    path('upload/', upload_file, name='upload_file'),
    path('text2voice/', text2voice, name='text2voice'),
    path('AIbot/', chatbot, name='AIbot'),
    path('AIbot/chatbot_history_set_zero/', chatbot_history_set_zero, name='chatbot_history_set_zero'),
    path('N_Analysis/', Num_Analysis, name='Num_Analysis'),

    path('N_Analysis/', include('Numerical_Analysis.urls')),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

