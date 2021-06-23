from django import forms
from django.shortcuts import render, redirect
from .form import CalculationForm
Meta=CalculationForm.Meta
from .models import Calculation
 
# Create your views here.
 
def calculate(request):
  if request.method == 'POST':
      form = CalculationForm(request.POST)
      operator = request.POST.get('operator')
      num_one = request.POST.get('num_one')
      num_two = request.POST.get('num_two')
      if form.is_valid():
          if(operator == '+'):
              result = int(num_one) + int(num_two)
          elif(operator == '-'):
              result = int(num_one) - int(num_two)
          elif(operator == '*'):
              result = int(num_one) * int(num_two)
          else:
           a = int(num_one)
           b = int(num_two)
           if (b == 0):
               return render(request, 'home.html', {'form':form})
           else:
               result = a/b
          calculation = form.save(commit=False)
          calculation.result = result
          calculation.save()
          return redirect('results')
  else:
      form = CalculationForm()
  return render(request, 'home.html', {'form':form})
 
def results(request):
  past = reversed(Calculation.objects.all())
  return render(request, 'results.html', {'past':past})
 
def home(request):
   return render(request, 'home.html', {'titles': 'Djang o', 'link' : 'http://127.0.0.1:8000/'})
