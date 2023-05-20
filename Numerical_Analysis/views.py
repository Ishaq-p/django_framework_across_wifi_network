from django.shortcuts import render
from django.http import HttpResponse
from .bisection import bisect as bisection1
from .rounding import rounding
import sympy as sym

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

        x = sym.symbols('x')
        f = sym.sympify(request.POST.get('function'))
        f = sym.lambdify(x, f)

        # Perform the bisection method calculations
        result = bisection1(a, b, p0, f, tol)

        # Prepare context data to pass to the template
        context = {
            'result': result,
        }

        # Render the template with the results
        return render(request, 'bisection.html', context)

    # Render the initial form
    return render(request, 'bisection.html')


def horners(request):
    return render(request, 'horners.html')

def FPI(request):
    return render(request, 'FPI.html')

def newtons(request):
    return render(request, 'newtons.html')
