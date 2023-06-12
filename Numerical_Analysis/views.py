from django.shortcuts import render
from django.http import HttpResponse
from .bisection import bisect as bisection1
from .horners import horners as horners1
from .fixed_point_iteration import fixed_point as fixed_point1
from .newton import newtons as newtons1
from .secant import secant as secant1
from .regula_falsi import regular_falsi as regular_falsi1
from .falsi_fpi import falsi_fpi as falsi_fpi1
from .num_diff import num_diff as num_diff1
from .lagrange_poly import lagrange_poly as lagrange_poly1
from .Rectangle_rule import Rectangle as rectangle_rule1
from .Trapezoidal_rule import trapezoidal as trapezoidal_rule1
from .Simpson_rule import simpson as simpson_rule1

# from sympy import *
from sympy import symbols, sympify, lambdify
import math
import numpy as np



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
        criterion = 1e-6 #float(request.POST.get('criterion'))
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


def lagrange_poly(request):
    if request.method == 'POST':

        x = request.POST.get('x').split(',')
        y = request.POST.get('y').split(',')
        x = [float(i) for i in x]
        y = [float(i) for i in y]
        x0 = float(request.POST.get('x0'))
        f0 = float(request.POST.get('f0'))
        float_digits = int(request.POST.get('float_digits'))

        context = {
            'result': lagrange_poly1(x, y, x0, f0, float_digits),
        }
        return render(request, 'lagrange_poly.html', context)

    return render(request, 'lagrange_poly.html')


def num_diff(request):
    if request.method == 'POST':

        x0 = np.pi/4 #float(request.POST.get('x0'))
        h = float(request.POST.get('h'))
        order = int(request.POST.get('order'))
        float_digits = int(request.POST.get('float_digits'))

        x = symbols('x')
        func = sympify(request.POST.get('func'))
        func = lambdify(x, func)

        context = {
            'result': num_diff1(x0, h, order, float_digits, func),
        }
        return render(request, 'num_diff.html', context)
    return render(request, 'num_diff.html')


def rectangle_rule(request):
    if request.method == 'POST':
        
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        n = int(request.POST.get('n'))

        float_digits = int(request.POST.get('float_digits')) 

        x = symbols('x')
        func = sympify(request.POST.get('func'))
        func = lambdify(x, func)

        context = {
            'result': rectangle_rule1(a, b, n, float_digits, func),
        }
        return render(request, 'rectangle_rule.html', context)

    return render(request, 'rectangle_rule.html')


def trapezoidal_rule(request):
    if request.method == 'POST':
        
        a = float(request.POST.get('a'))
        b = np.pi/2 #float(request.POST.get('b'))
        n = int(request.POST.get('n'))

        float_digits = int(request.POST.get('float_digits'))

        x = symbols('x')
        func = sympify(request.POST.get('func'))
        func = lambdify(x, func)

        context = {
            'result': trapezoidal_rule1(a, b, n, float_digits, func)
        }
        return render(request, 'trapezoidal_rule.html', context)

    return render(request, 'trapezoidal_rule.html')


def simpson_rule(request):
    if request.method == 'POST':
        
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        n = int(request.POST.get('n'))

        float_digits = int(request.POST.get('float_digits'))

        x = symbols('x')
        func = sympify(request.POST.get('func'))
        func = lambdify(x, func)

        context = {
            'result': simpson_rule1(a, b, n, float_digits, func),
        }
        return render(request, 'simpson_rule.html', context)

    return render(request, 'simpson_rule.html')