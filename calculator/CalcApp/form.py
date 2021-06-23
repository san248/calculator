from .models import Calculation
from django import forms
from .models import Calculation
 
INTEGER_CHOICES = [tuple([x,x]) for x in range(1,32)]
 
class CalculationForm(forms.ModelForm):
  class Meta:
      model = Calculation
      fields = ['num_one', 'num_two', 'operator', 'date']
    
  #calculation_type = forms.IntegerField(widget=forms.Select(
   #  choices=[(0, "+"), (1, "-"), (2, "*"), (3, "/")]))
