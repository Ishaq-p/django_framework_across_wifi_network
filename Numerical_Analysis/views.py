from django.shortcuts import render
from django.http import HttpResponse
from .bisection import bisect as bisection1
from .horners import horners as horners1
from .fixed_point_iteration import fixed_point as fixed_point1
from .newton import newtons as newtons1
from .secant import secant as secant1
from .regula_falsi import regular_falsi as regular_falsi1
from .falsi_fpi import falsi_fpi as falsi_fpi1
# from sympy import *
from sympy import symbols, sympify, lambdify
import math



# Create your views here.
def home1(request):
    return render(request, 'index_NA.html')

def bisection(request):
    if request.method == 'POST':
        # Get input values from the form
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        p0 = float(request.POST.get('tolerance'))
        tol = float(request.POST.get('tolerance'))
        float_digits = int(request.POST.get('float_digits'))

        x = symbols('x')
        f = sympify(request.POST.get('function'))
        f = lambdify(x, f)

        # Perform the bisection method calculations
        # Prepare context data to pass to the template
        context = {
            'result': bisection1(a, b, p0, f, float_digits, tol),
        }

        # Render the template with the results
        return render(request, 'bisection.html', context)

    # Render the initial form
    return render(request, 'bisection.html')


def horners(request):
    if request.method == 'POST':
        alpha = float(request.POST.get('alpha'))
        coefs = request.POST.get('coefs').split(',')
        coefs = [float(i) for i in coefs]

        context = {
            'result': horners1(alpha, coefs),
            }
        return render(request, 'horners.html', context)
    
    return render(request, 'horners.html')

def FPI(request):
    if request.method == 'POST':

        x0 = float(request.POST.get('x0'))
        criterion = float(request.POST.get('criterion'))
        float_digits = int(request.POST.get('float_digits'))

        x = symbols('x')
        func = sympify(request.POST.get('func'))
        func = lambdify(x, func)

        context = {
            'result': fixed_point1(x0, criterion, float_digits, func),
        }
        return render(request, 'FPI.html', context)



    return render(request, 'FPI.html')

def newtons(request):
    if request.method == 'POST':

        x0 = float(request.POST.get('x0'))
        criterion = float(request.POST.get('criterion'))
        float_digits = int(request.POST.get('float_digits'))

        x = symbols('x')
        func = sympify(request.POST.get('func'))
        func_ = sympify(request.POST.get('func_'))

        func = lambdify(x, func)
        func_ = lambdify(x, func_)

        context = {
            'result': newtons1(x0, criterion, float_digits, func, func_),
        }

        return render(request, 'newtons.html', context)


    return render(request, 'newtons.html')

def secant(request):
    if request.method == 'POST':

        x0 = float(request.POST.get('x0'))
        x1 = float(request.POST.get('x1'))
        criterion = float(request.POST.get('criterion'))
        float_digits = int(request.POST.get('float_digits'))

        x = symbols('x')
        func = sympify(request.POST.get('func'))
        func = lambdify(x, func)

        context = {
            'result': secant1(x0, x1, criterion, float_digits, func),
        }
        return render(request, 'secant.html', context)

    return render(request, 'secant.html')

def regula_falsi(request):
    if request.method == 'POST':

        x0 = float(request.POST.get('x0'))
        x1 = float(request.POST.get('x1'))
        criterion = float(request.POST.get('criterion'))
        float_digits = int(request.POST.get('float_digits'))

        x = symbols('x')
        func = sympify(request.POST.get('func'))
        func = lambdify(x, func)

        context = {
            'result': regular_falsi1(x0, x1, criterion, float_digits, func),
        }
        return render(request, 'regula_falsi.html', context)

    return render(request, 'regula_falsi.html')


def text_to_function(expression):
    def function(x):
        return eval(expression, {'__builtins__': None}, {'x': x, 'pi': math.pi, 'e': math.e, 'sin': math.sin})
    return function    


def falsi_fpi(request):
    if request.method == 'POST':
        
        x0 = float(request.POST.get('x0'))
        x1 = float(request.POST.get('x1'))
        criterion = float(request.POST.get('criterion'))
        float_digits = int(request.POST.get('float_digits')) 

        func = request.POST.get('func')
        func = text_to_function(func)

        context = {
            'result': falsi_fpi1(x0, x1, criterion, float_digits, func),
        }
        return render(request, 'falsi_FPI.html', context)

    return render(request, 'falsi_FPI.html')